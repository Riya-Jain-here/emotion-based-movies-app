export default function TextInput({ value, onChange }) {
  return (
    <textarea
      className="w-full p-4 text-gray-800 bg-white rounded-2xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-violet-500 shadow-sm resize-none"
      rows="4"
      placeholder="e.g. I am happy today"
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  );
}