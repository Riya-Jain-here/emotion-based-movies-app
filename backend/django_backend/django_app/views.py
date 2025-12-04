import os
import pickle
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .constants import recommend
from django.views.decorators.csrf import csrf_exempt
import re

# Build absolute paths to model files
ML_DIR = os.path.join(settings.BASE_DIR, "django_app", "ml_files")
MODEL_PATH = os.path.join(ML_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(ML_DIR, "vectorizer.pkl")

# Load model and vectorizer once
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
except Exception as e:
    
    model = None
    vectorizer = None
    print("Warning: Could not load ML files:", e)

def home(request):
    return render(request, "index.html")

def is_meaningful(text):
    # Check if input has at least one word with letters
    return bool(re.search(r"[a-zA-Z]", text))

@csrf_exempt
def predict_view(request):
    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if not text:
            return render(request, "result.html", {"error": "Please enter a sentence."})

        if model is None or vectorizer is None:
            return render(request, "result.html", {"error": "Model not loaded."})

        X = vectorizer.transform([text])
        pred = model.predict(X)[0]

        confidence = None
        try:
            if hasattr(model, "predict_proba"):
                confidence = float(model.predict_proba(X).max())
        except Exception:
            confidence = None

         # Confidence threshold check
        if confidence is not None and confidence < 0.3:
            pred = "Unknown / No clear emotion"

        movies = recommend(pred, k=5) if pred != "Unknown / No clear emotion" else []

        context = {
            "text": text,
            "predicted_emotion": pred,
            "confidence": confidence,
            "movies": movies
        }
        return render(request, "result.html", context)

    return render(request, "index.html")

# JSON API endpoint (for React)
@csrf_exempt
def predict_api(request):
    # Accept POST with JSON {"text": "..."}
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    try:
        import json
        body = json.loads(request.body)
        text = body.get("text", "").strip()
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    if not text:
        return JsonResponse({"error": "text required"}, status=400)
    if not is_meaningful(text):
        return JsonResponse({"error": "Please enter meaningful text."}, status=400)

    if model is None or vectorizer is None:
        return JsonResponse({"error": "model not loaded"}, status=500)

    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    confidence = None
    try:
        if hasattr(model, "predict_proba"):
            confidence = float(model.predict_proba(X).max())
    except Exception:
        confidence = None

    if confidence is not None and confidence < 0.3:
        pred = "Unknown / No clear emotion"
        movies = []
    else:
        movies = recommend(pred, k=5)
        
    return JsonResponse({
        "text": text,
        "predicted_emotion": pred,
        "confidence": confidence,
        "movies": movies
    })