import MovieCard from "./MovieCard";

export default function Result({ emotion, confidence, movies, text, onBack }) {
  return (
    <div className="p-6 space-y-4">
      {/* Back link */}
      <div>
        <a
          onClick={onBack}
          className="text-indigo-600 hover:underline cursor-pointer"
        >
          ← Back
        </a>
      </div>

      <h2 className="text-2xl font-bold">Your Emotion: {emotion}</h2>
      <p className="text-gray-600">Input: {text}</p>
     {/* <p className="text-gray-700 font-medium">
        Confidence: {(confidence * 100).toFixed(2)}%
      </p>*/}

      <h3 className="text-xl font-semibold mt-4">Recommended Movies</h3>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {movies.map((m, i) => (
          <MovieCard key={i} title={m} />
        ))}
      </div>
    </div>
  );
}