import { useState } from "react";
import TextInput from "./TextInput";
import Loader from "./Loader";
import { getEmotionPrediction } from "../api/emotionAPI";

export default function EmotionForm({ onResult }) {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);

    const result = await getEmotionPrediction(text);
    setLoading(false);

    onResult(result, text);  
  }

  return (
    <div className="flex flex-col items-center justify-center p-6">
     <h6 className="text-2xl md:text-2xl font-semibold text-center mt-8 mb-6">
      Enter some text to analyze your emotion and get some movie recommendations:
    </h6>
    <form onSubmit={handleSubmit} className="space-y-4 p-4">
     
      <TextInput value={text} onChange={setText} />
      <button
        type="submit"
        className="w-full bg-violet-900 text-white py-3 rounded-xl shadow hover:bg-violet-700 transition"
      >
        Get Recommendations
      </button>

      {loading && <Loader />}
    </form>
    </div>
  );
}