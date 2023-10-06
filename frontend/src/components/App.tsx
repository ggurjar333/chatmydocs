import React from 'react';
import logo from './logo.svg';
import './App.css';
// @ts-ignore
import Counter from './Counter';

const App: React.FC = () => {
  return (
    <div className="App">
      <Counter /> {/* Render the Counter component */}
    </div>
  );
};


export default App;
