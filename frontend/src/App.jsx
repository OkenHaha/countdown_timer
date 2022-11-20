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

  return (
    <Router>
      <div className="App">
      <button>
        <Link to="/timer">Start Timer</Link>
      </button>
      <Routes>
          <Route exact path="/timer" element={<Time/>}>Start Timer</Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App
