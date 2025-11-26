import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    const trimmed = question.trim();

    if (!trimmed) {
      setError("Palun sisesta küsimus");
      setAnswer("");
      return;
    }

    setError("");
    setAnswer("");

    setLoading(true);

    try {
      const res = await fetch(`${API_URL}/ask`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: trimmed }),
      });

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`Serveri viga (${res.status}): ${text}`);
      }

      const data = await res.json();

      setAnswer(data.answer || "Vastus puudub.");
    } catch (err) {
      console.error(err);
      setError(err.message || "Midagi läks valesti.");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
      e.preventDefault();
      handleAsk();
    }
  };


  return (
    <div>
      <h1>Tehisintellekt.ee Q&A</h1>

      <div>
        <label>Küsimus:</label>
        <br />
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Sisesta küsimus siia..."
          rows={5}
          cols={50}
        />
      </div>

      <br />

      <button onClick={handleAsk} disabled={loading}>
        {loading ? "Küsin..." : "Küsi"}
      </button>

      {error && (
        <div>
          <p style={{ color: "red" }}>{error}</p>
        </div>
      )}

      {answer && (
        <div>
          <h3>Vastus:</h3>
          <pre>{answer}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
