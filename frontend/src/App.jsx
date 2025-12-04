import { useState } from "react";
import Navbar from "./components/Navbar";
import EmotionForm from "./components/EmotionForm";
import Result from "./components/Result";
import Footer from "./components/Footer";

function App() {
  const [result, setResult] = useState(null);

  async function handleResult(apiData, textInput) {
    if (!textInput.trim()) {
    alert("Please enter some text before submitting.");
    return;
  }

    setResult({
      text: textInput,
      emotion: apiData.predicted_emotion,
      confidence: apiData.confidence,
      movies: apiData.movies,
    });
  }

  return (
    <>
    <div className="flex flex-col bg-amber-100 min-h-screen">
      <Navbar />
      
      <div className="flex-grow max-w-2xl mx-auto mt-10 p-4">
        {!result ? (
          <EmotionForm onResult={handleResult} />
        ) : (
          <Result
            text={result.text}
            emotion={result.emotion}
            confidence={result.confidence}
            movies={result.movies}
            onBack={() => setResult(null)}
          />
        )}
      </div>
      <Footer/>
      </div>
    </>
  );
}

export default App;