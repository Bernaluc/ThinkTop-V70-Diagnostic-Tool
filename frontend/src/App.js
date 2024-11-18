import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Status from './Status';
import ManualControl from './ManualControl';
import Sidebar from './Sidebar';
import Troubleshooting from './Troubleshooting'
import './App.css';

function App() {
  return (
    <Router>
      <div className="relative min-h-screen">
        <Sidebar />
        <div className="ml-0 md:ml-64 transition-all duration-300">
          <Routes>
            <Route path="/" element={<Status />} />
            <Route path="/manual-control" element={<ManualControl />} />
            <Route Path="/troubleshooting" element={<Troubleshooting />} /> 
            {/* Add more routes as needed */}
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
