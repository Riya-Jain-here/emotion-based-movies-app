export default function Navbar() {
  return (
    <nav className="w-full h-20 bg-violet-900">
      <div className="max-w-5xl mx-auto px-6 py-4 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <img
            src="/Logo_.png"
            alt="logo"
            className="w-10 h-10 object-contain"
          />
          <h1 className="text-lg md:text-2xl font-semibold text-white">
            Emotion-based Movie Recommender
          </h1>
        </div>
      </div>
    </nav>
  );
}
