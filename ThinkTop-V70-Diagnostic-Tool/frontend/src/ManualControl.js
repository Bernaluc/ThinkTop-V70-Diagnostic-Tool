import React, { useState } from 'react';
import './ManualControl.css';

function ManualControl() {
  const [manualMode, setManualMode] = useState(false);

  // Handler to toggle manual mode
  const toggleManualMode = () => {
    setManualMode(!manualMode);
  };

  // Functions to send control signals to the backend
  const sendControlSignal = async (output, value) => {
    try {
      await fetch(`/api/control`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ output, value }),
      });
      console.log(`Sent control signal to ${output} with value: ${value}`);
    } catch (error) {
      console.error("Error sending control signal:", error);
    }
  };

  return (
    <div className="ManualControl">
      <h2>Manual Control</h2>
      <button onClick={toggleManualMode}>
        {manualMode ? "Disable Manual Mode" : "Enable Manual Mode"}
      </button>

      {manualMode && (
        <div className="controls">
          <h3>Control Outputs</h3>
          <button onClick={() => sendControlSignal('SV1', true)}>Activate SV1 (Main Valve)</button>
          <button onClick={() => sendControlSignal('SV1', false)}>Deactivate SV1 (Main Valve)</button>
          
          <button onClick={() => sendControlSignal('SV2', true)}>Activate SV2 (Upper Seat)</button>
          <button onClick={() => sendControlSignal('SV2', false)}>Deactivate SV2 (Upper Seat)</button>
          
          <button onClick={() => sendControlSignal('SV3', true)}>Activate SV3 (Lower Seat)</button>
          <button onClick={() => sendControlSignal('SV3', false)}>Deactivate SV3 (Lower Seat)</button>
        </div>
      )}
    </div>
  );
}

export default ManualControl;
