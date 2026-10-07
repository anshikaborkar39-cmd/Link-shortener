import { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const shortenURL = async () => {
    if (!url.trim()) {
      alert("Please enter a URL");
      return;
    }

    setLoading(true);
    setShortUrl("");

    try {
      const response = await fetch(
       `https://link-shortener-5xh7.onrender.com/shorten?url=${encodeURIComponent(url)}`,
        {
          method: "POST",
        }
      );

      const data = await response.json();

      if (data.error) {
        alert(data.error);
        return;
      }

      setShortUrl(data.short_url);
    } catch (error) {
      console.error(error);
      alert("Backend is not connected");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>Linkly</h1>
      <p className="tagline">Fast • Simple • Secure</p>

      <div className="card">
        <h2>Shorten your link</h2>
        <p>Turn long URLs into short, easy-to-share links.</p>

        <label>Original URL</label>

        <input
          type="text"
          placeholder="https://www.youtube.com"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button onClick={shortenURL} disabled={loading}>
          {loading ? "Creating..." : "Create Short Link"}
        </button>

        {shortUrl && (
          <div className="result">
            <p>Your short URL:</p>

            <input value={shortUrl} readOnly />

            <button
              onClick={() => navigator.clipboard.writeText(shortUrl)}
            >
              Copy
            </button>
          </div>
        )}
      </div>

      <footer>© 2026 Linkly • URL Shortener</footer>
    </div>
  );
}

export default App;
