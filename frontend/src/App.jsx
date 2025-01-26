import "leaflet/dist/leaflet.css";
import 'bulma/css/bulma.min.css';

import { useEffect, useState } from 'react';
import axios from 'axios';
import { MapContainer } from 'react-leaflet/MapContainer'
import { TileLayer } from 'react-leaflet/TileLayer'
import { Marker } from 'react-leaflet/Marker'
import { Icon } from 'leaflet'
import { useMapEvents } from 'react-leaflet/hooks'
import { LatLngBounds } from 'leaflet';
import 'leaflet-rotatedmarker'
// import { useMap } from 'react-leaflet/hooks'


function MapEventsComponent({ranges}) {
  const [flights, setFlights] = useState([]);
  const [fireCoordinates, setFireCoordinates] = useState([]);
  const [flightsDisplayed, setFlightsDisplayed] = useState([]);
  const [currentBounds, setCurrentBounds] = useState(null);
  
  const fireIcon = new Icon({
    iconUrl: 'assets/exclamation.png',
    iconSize: [25, 25]
  });

  const planeIcon = new Icon({
    iconUrl: 'assets/plane.png',
    iconSize: [40, 40]
  });

  const map = useMapEvents({
    moveend: () => {
      setCurrentBounds(map.getBounds());
    },
  });

  const fetchFlights = async () => {
    console.log('ranges', ranges)
    try {
      const response = await axios.post("http://localhost:5000/flights", {
          // bounds: () => {
          //   bounds = map.getBounds();
          //   print(bounds);
          //   return [[bounds._southWest.lat, bounds._southWest.lng], [bounds._northEast.lat, bounds._northEast.lng]];
          // },
          conf_ranges: ranges['conf']
        });
      setFireCoordinates(response.data.fireCoordinates);
      setFlights(response.data.fireFlights);
      // const response = await axios.get('https://opensky-network.org/api/states/all');
      // setFlights(response.data.states);
      // setFlights(response.data);
    } catch (error) {
      console.error("Error fetching flights: ", error);
    }
  };

  useEffect(() => {
    fetchFlights();
    setCurrentBounds(map.getBounds());
    const intervalId = setInterval(fetchFlights, 120000);
    return () => clearInterval(intervalId);
  }, []);

  // useEffect(() => {
  //     console.log("currentBounds", currentBounds);
  //     if (flights?.length){
          
  //         const flightsWithinBounds = flights.filter((flight) => {
  //             if (!currentBounds || !flight[5] || !flight[6]) {
  //                 return false;
  //             }
  //             return currentBounds.contains([flight[6],flight[5]]);
  //         });
  //         setFlightsDisplayed(flightsWithinBounds);
  //     }
  //   }, [currentBounds, flights]);
  console.log(fireCoordinates)
  console.log(flights[0])
  return (<div>
      {fireCoordinates.map((fireCoordinate, index) => (
        <div key={index}>
          <Marker position={[fireCoordinate['lat'], fireCoordinate['lon']]} 
                  icon={fireIcon} 
          />
        </div>
      ))}
      {flights.map((flight, index) => (
        <div key={1200 + index}>
          <Marker position={[flight[0], flight[1]]} 
                  rotationAngle={flight[2]}
                  zIndexOffset={1000}
                  icon={planeIcon}
          />
        </div>
      ))}
    </div>);
}

function App() {
  // const [state, setState] = useState(null);
  // const [numbers, setNumbers] = useState("");
  // const [result, setResult] = useState(null);

  const [ranges , setRanges] = useState({
    //degErr: 35,
    conf: {
      high: 100.0,
      low: 50.0,
    }
  });

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
  // const map = useMapEvents({
  //     moveend: () => {
  //         setCurrentBounds(map.getBounds());
  //     },
  // })

  // bounds = new LatLngBounds(
  //             [-125, 25],
  //             [-64, 50]
  //           )
  // const hi = () => { console.log('hi'); }
  // Form() /************************************************** BIG FAT COMMENT FOR WHERE FORM IS AGHHHHHHHHHH ******************************************************************************/ 
  return (
    <div style={{height: "100vh", boxSizing: "border-box", overflow: "hidden"}}>
      <nav className="navbar has-background-dark p-2 border">
        {/* <div className="navbar-brand">
          <a className="navbar-item has-text-white has-text-weight-bold">
            City Dashboard
          </a>``
        </div> */}
        <div className="navbar-menu">
          <div className="navbar-start">
            <a className="navbar-item has-text-white">FireFlys</a>
            {/* <a className="navbar-item has-text-white">Performance</a> */}
          </div>
          {/* <div className="navbar-end">
            <a className="navbar-item has-text-white">Export</a>
            <a className="navbar-item has-text-white">Notifications</a>
          </div> */}
        </div>
      </nav>
      <div className="columns is-gapless" style={{height: "calc(100% - 52px)", width: "100vw"}}>
        {/* Left Sidebar */}
        {/* <aside className="column is-2 has-background-dark p-3 border">
          <p className="has-text-white has-text-weight-bold mb-2">NETWORK</p>
            <ul>
              <li className="has-text-white">Greenwood Village</li>
              <ul>
                <li className="has-text-grey-light">Holly</li>
                <li className="has-text-grey-light">Orchard</li>
                <li className="has-text-grey-light">Yosemite</li>
                <li className="has-text-grey-light">Belleview</li>
              </ul>
            </ul>
        </aside> */}
        {/* Main map area */}
        <div className="column is-9 border">
          <MapContainer
            center={[38.7946, -101.5348]}
            zoom={4.5}
            // maxBounds={bounds}
            style={{ height: "100%", width: "100%", backgroundColor: "grey" }}
          >
            <TileLayer
              attribution='&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}{r}.png"
            />
            <MapEventsComponent ranges={ranges} />
          </MapContainer>
        </div>
        {/* Right Sidebar */}
        <aside className="column is-3 p-5 has-background-dark border" style={{overflowY: "clip"}}>
          <div>
            {/* <p className="has-text-weight-bold has-text-white">Intersection</p> */}
            {/* <div className="box">
              <p><strong>Saturation:</strong> 62%</p>
              <p><strong>Volume:</strong> 1340/hr</p>
              <p><strong>Avg Delay:</strong> 73 sec</p>
              <p><strong>Travel Time:</strong> 95 sec</p>
            </div> */}
            <div className="box m-3">
              <Form ranges={ranges} setRanges={setRanges}/>
            </div>
          </div>
        </aside>
      </div>
      {/* <div id= */}
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

function Form({ ranges, setRanges }) {

  // function handleDegChange(e) {
  //   try{
  //     setRanges({
  //       ...ranges,
  //       deg: Number(e.target.value)
  //     });
  //   }
  //   catch{
  //     alert('Error: Invalid input. Please input a number.');
  //   }
  // }

  function handleConfHighChange(e)
  {
    try{
      setRanges({
        ...ranges,
        conf:
        {
          ...ranges.conf,
          high: Number(e.target.value)
        }
      });
    }
    catch{
      alert('Error: Invalid input. Please input a number.');
    }
  }

  function handleConfLowChange(e){
    try{
      setRanges({
        ...ranges,
        conf:{
          ...ranges.conf,
          low: Number(e.target.value)
        }
      });
    }
    catch{
      alert('Error: Invalid input. Please input a number.');
    }
  }
  return (
    <>
      {/* <label> Degrees of Error:
        <input 
          value={ranges.deg}
          onChange={handleDegChange}
        />
      </label> */}
      <label>
        Lower Confidence Bound:
        <input
          value = {ranges.conf.low}
          onChange ={handleConfLowChange}
        />
      </label>
      <br />
      <label>
        Upper Confidence Bound:
        <input 
          value={ranges.conf.high}
          onChange = {handleConfHighChange}

        />

      </label>
    </>
  )
}

export default App;
