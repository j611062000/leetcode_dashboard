import './App.css';
import React, { useEffect, useState } from 'react';

function getProblems(problemSet) {
  return (
    <div>
      {JSON.stringify(problemSet[1])}
    </div>
  )
}

function App() {
  const [problemSet, setProblemSet] = useState({"problems": []})

  useEffect(() => {
    fetch('http://127.0.0.1:5000/problems', { mode: 'cors' , contentType: 'application/json'})
      .then(response => response.json())
      .then(responseJson => {
        setProblemSet(responseJson)
      }).catch(error => {
        console.log(error)
      })
  }, [])


  return (
    <div className="App">
      <header className="App-header">
        {problemSet ? getProblems(problemSet) : "Loading..."}
      </header>
    </div>
  );
}

export default App;
