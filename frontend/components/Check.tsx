// components/Check.tsx

"use client"; // This directive marks the component as a Client Component

import { useState } from 'react';

const Check = () => {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUrl(e.target.value);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult('');

    // Replace with your local backend API endpoint
    const apiUrl = 'http://localhost:5000/check-url';

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setResult(data.message); // Display the result message from the backend
    } catch (error) {
      setError('There was an error checking the URL.');
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center py-20 bg-gray-100" id="check">
      <h2 className="text-2xl font-bold mb-4">Check a URL</h2>
      <form onSubmit={handleSubmit} className="flex flex-col items-center">
        <input
          type="text"
          value={url}
          onChange={handleInputChange}
          className="px-4 py-2 border rounded-md mb-4 w-80"
          placeholder="Enter URL to check"
        />
        <button
          type="submit"
          className="px-6 py-2 bg-blue-600 text-white rounded-md"
          disabled={loading}
        >
          {loading ? 'Checking...' : 'Check URL'}
        </button>
      </form>

      {/* Display the result or any error */}
      {result && <p className="mt-4 text-green-600">{result}</p>}
      {error && <p className="mt-4 text-red-600">{error}</p>}
    </div>
  );
};

export default Check;
