import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'



function App() {
  const [problemSet, setProblemSet] = useState({})

  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/health').then(response => {
      alert("SUCCESS", response.data)
      setProblemSet(response.data)
    }).catch(error => {
      console.log(error)
    })
  }, [])


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {problemSet.data}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
