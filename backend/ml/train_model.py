from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import pickle

data=pd.read_csv('dataset.csv')
# Count how many samples per emotion
counts = data['emotion'].value_counts()
print("Samples per emotion:\n", counts)

# Check for any classes with less than 5 samples
for emotion, count in counts.items():
    if count < 5:
        print(f"Emotion '{emotion}' has only {count} samples. You should add more.")

X=data["description"]
y=data["emotion"]

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2, random_state=42, stratify=y)

vectorizer=TfidfVectorizer()
X_train_vector=vectorizer.fit_transform(X_train)
X_test_vector=vectorizer.transform(X_test)

model=LogisticRegression(max_iter=2000)
model.fit(X_train_vector,y_train)

pred=model.predict(X_test_vector)

print(accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

pickle.dump(model, open("model.pkl","wb" ))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))