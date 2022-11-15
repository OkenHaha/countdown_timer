import { useState, useEffect  } from 'react'
import './App.css'

function App() {
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
  const d = date.toLocaleTimeString()
  return (
    <div>
    <h1>{d}</h1>
    </div>
  );
}

export default App
