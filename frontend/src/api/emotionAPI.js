export async function getEmotionPrediction(text) {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/predict/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      throw new Error("API Error");
    }

    return await response.json();
  } catch (error) {
    console.error("Prediction Error:", error);
    return { error: "Unable to fetch prediction" };
  }
}