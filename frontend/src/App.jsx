import { useState, useEffect  } from 'react'
import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom'
import axios from 'axios'

import './App.css'
import Time from './pages/Time.jsx'
/*function App() {
  const [date, setDate] = useState(new Date());
  
  function refreshClock() {
    setDate(new Date());
  }
  useEffect(() => {
    const timerId = setInterval(refreshClock, 1000);
    return function cleanup() {
      clearInterval(timerId);
    };
  }, []);

  const show = () => {
    const d = date.toLocaleTimeString()
    return d;
  }
  return (
    <div>
    <button onClick={show}>CLick me</button>
    <h1></h1>
    </div>
  );
}*/
function App() {
  const url = 'http://127.0.0.1:8000/timerapi/'

  const [ptime, setPtime] = useState(null)

  let config = {
    headers: {
      'Content-Type': 'application/json',
    }
  }
  const d = new Date()
  const iso = d.toISOString()
  console.log(iso)
  const end = d.setMinutes(d.getMinutes() + 3)
  //console.log(end)
  const s = new Date(end)
  console.log(s.toISOString())
  function setTime(){
    axios.post(url, {
      name: "oken",
      start_time: iso,
      end_time: iso + 10000
    }, config)
    .then((response) => {
      setPtime(response.data)
    })
    .catch(err => {
      if (err.response) {
        console.log(err.response.data)
        console.log(err.response.status)
        console.log(err.response.headers)
      }
      else if (err.request) {
        console.log(err.request)
      }
      else {
        console.log(err.message)
      }
    })
  }

/*const [date, setDate] = useState(new Date());
  
  function refreshClock() {
    setDate(new Date());
  }
  useEffect(() => {
    const timerId = setInterval(refreshClock, 1000);
    return function cleanup() {
      clearInterval(timerId);
    };
  }, []);

  const show = () => {
    const d = date.toLocaleTimeString()
    return d;
  }*/
  return (
    <div>
    <Router>
      <div className="App">
      <button onClick={setTime}>Post Date</button>
      <button >
        <Link to="/timer">Start Timer</Link>
      </button>
      <Routes>
          <Route exact path="/timer" element={<Time/>}>Start Timer</Route>
        </Routes>
      </div>
    </Router>
    </div>
  );
}

export default App
