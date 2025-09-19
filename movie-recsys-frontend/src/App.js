import React, { useState } from "react";

function App() {
  const [likedMovies, setLikedMovies] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchRecommendations = async () => {
    setLoading(true);
    setError("");
    setRecommendations([]);
    try {
      const titlesArray = likedMovies
        .split(",")
        .map((t) => t.trim())
        .filter((t) => t.length > 0);

      if (titlesArray.length === 0) {
        setError("Please enter at least one movie title.");
        setLoading(false);
        return;
      }

      const params = new URLSearchParams();
      titlesArray.forEach((t) => params.append("liked_movies", t));

      const res = await fetch(
        `https://movie-recsys-api-latest.onrender.com/recommend_by_movies?${params.toString()}&n=5`
      );
      if (!res.ok) throw new Error("Failed to fetch recommendations.");
      const data = await res.json();
      console.log("API response data:", data);
      if (data.error) {
        setError(data.error);
      } else if (data.recommendations && data.recommendations.length > 0) {
        setRecommendations(data.recommendations);
      } else {
        setError("No recommendations found.");
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🎬 Movie Recommendation App</h1>
      <section>
        <h2>Get Recommendations by Movie Titles</h2>
        <p>
          Enter movie titles separated by commas (e.g. The Matrix (1999), Toy
          Story (1995)):
        </p>
        <input
          type="text"
          placeholder="The Matrix (1999), Toy Story (1995)"
          value={likedMovies}
          onChange={(e) => setLikedMovies(e.target.value)}
          style={{ width: "400px" }}
        />
        <button
          onClick={fetchRecommendations}
          disabled={loading || !likedMovies.trim()}
          style={{ marginLeft: "10px" }}
        >
          {loading ? "Loading..." : "Get Recommendations"}
        </button>
        {error && <p style={{ color: "red" }}>{error}</p>}
        <ul>
          {recommendations.map((m) => (
            <li key={m.movie_id}>
              {m.title} — est. rating: {m.estimated_rating.toFixed(2)}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default App;
