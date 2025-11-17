import React, { useState } from 'react';
import { fetchPropertyDetails } from './services/property';

const App: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [apiResponse, setApiResponse] = useState<any>(null);
  const backendApiUrl = import.meta.env.VITE_BACKEND_API_URL;

  const handleSearch = async () => {
    try {
      const data = await fetchPropertyDetails(backendApiUrl, searchTerm);
      setApiResponse(data);
    } catch (error) {
      setApiResponse({ error: 'Failed to fetch data' });
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-4xl font-bold text-gray-800 mb-6">Hometap Property Detail Search</h1>
      <div className="flex items-center space-x-4 mb-4">
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Enter full address, including street, city, state, and zip"
          className="p-3 border border-gray-300 rounded-md w-[600px]"
        />
        <button
          onClick={handleSearch}
          className="bg-blue-500 text-white px-6 py-3 rounded-md hover:bg-blue-600"
        >
          Search
        </button>
      </div>
      {apiResponse && (
      <div className="mt-6 w-full max-w-6xl">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {Object.entries(apiResponse).map(([provider, data]) => (
            <div key={provider} className="bg-white p-6 rounded-lg shadow-md">
              <h3 className="text-lg font-bold mb-4 text-blue-600">{provider}</h3>
              <div className="space-y-2 text-sm">
                <div><span className="font-semibold">Address:</span> {data["Normalized Address"]}</div>
                <div><span className="font-semibold">Square Footage:</span> {data["Square Footage"]}</div>
                <div><span className="font-semibold">Lot Size:</span> {data["Lot Size (Acres)"]} acres</div>
                <div><span className="font-semibold">Year Built:</span> {data["Year Built"]}</div>
                <div><span className="font-semibold">Type:</span> {data["Property Type"]}</div>
                <div><span className="font-semibold">Bed/Bath:</span> {data.Bedrooms}/{data.Bathrooms}</div>
                <div><span className="font-semibold">Sale Price:</span> ${data["Sale Price"].toLocaleString()}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    )}

    </div>
  );
};

export default App;
