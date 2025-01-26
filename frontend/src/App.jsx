// import "leaflet/dist/leaflet.css";

import { useState } from 'react';
import axios from 'axios';
import { MapContainer } from 'https://cdn.esm.sh/react-leaflet/MapContainer'
import { TileLayer } from 'https://cdn.esm.sh/react-leaflet/TileLayer'
import { useMap } from 'https://cdn.esm.sh/react-leaflet/hooks'

function App() {
  const [state, setState] = useState(null);
  // const [numbers, setNumbers] = useState("");
  // const [result, setResult] = useState(null);

  // const handleSubmit = async (e) => {
  //   e.preventDefault();
  //   const inputNumbers = numbers.split(",").map(Number);

  //   try {
  //     const response = axios.post("http://localhost:5000/analyze", {
  //       numbers: inputNumbers,
  //     }).then((response) => {
  //       console.log(response);
  //       setResult(response.data);
  //     });
  //   } catch(error) {
  //     console.error("Error analyzing data: ", error);
  //   }
  // };
  return (
    <div>
      <h1>Leaflet Map</h1>
      <MapContainer
        center={[51.505, -0.09]}
        zoom={13}
        style={{ height: "100vh", backgroundColor: "grey" }}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

      </MapContainer>
      {/* <h1>Data Analysis App</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter numbers (comma separated):
          <input
            type="text"
            value={numbers}
            onChange={(e) => setNumbers(e.target.value)}
            style={{ marginLeft: "10px", padding: "5px" }}
          />
        </label>
        <button type="submit" style={{ marginLeft: "10px", padding: "5px" }}>
          analyze
        </button>
      </form>
      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Analysis result: </h2>
          <p>Mean: {result.mean}</p>
          <p>Sum: {result.sum}</p>
          <p>Count: {result.count}</p>
        </div>
      )} */}
    </div>
  );
}

export default App;
