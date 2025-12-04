export default function MovieCard({ title }) {
  return (
    <div className="p-4 bg-white rounded-xl border border-gray-100 shadow-sm hover:shadow-lg transition">
      <h4 className="text-lg font-semibold text-gray-900">{title}</h4>
    </div>
  );
}