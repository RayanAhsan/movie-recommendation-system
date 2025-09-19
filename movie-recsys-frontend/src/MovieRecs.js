import React, { useState } from "react";

function MovieRecs() {
  const [userId, setUserId] = useState("");
  const [recs, setRecs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const getRecommendations = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`https://movie-recsys-api-latest.onrender.com/recommend/${userId}`);
      if (!res.ok) throw new Error(`API error: ${res.statusText}`);
      const data = await res.json();
      setRecs(data.recommendations);
    } catch (err) {
      setError(err.message);
      setRecs([]);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial, sans-serif" }}>
      <h1>Movie Recommendations</h1>
      <input
        type="number"
        placeholder="Enter User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        style={{ padding: 8, fontSize: 16, width: 200 }}
      />
      <button
        onClick={getRecommendations}
        disabled={!userId || loading}
        style={{ marginLeft: 10, padding: "8px 16px", fontSize: 16 }}
      >
        {loading ? "Loading..." : "Get Recommendations"}
      </button>

      {error && <p style={{ color: "red" }}>Error: {error}</p>}

      <ul>
        {recs.map((movie) => (
          <li key={movie.movie_id}>
            {movie.title} (Estimated rating: {movie.estimated_rating.toFixed(2)})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MovieRecs;
