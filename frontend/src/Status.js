import React, { useEffect, useState } from 'react';
import './Status.css';

function Status() {
  const [statusData, setStatusData] = useState(null); // Initial state as null
  const [loading, setLoading] = useState(true);        // State to track loading status

  useEffect(() => {
    let intervalId; // Variable to store interval ID for cleanup

    const fetchStatus = async () => {
      try {
        const response = await fetch("http://10.20.16.195:5000/api/status");
        const data = await response.json();
        console.log("Fetched data:", data); // Log the data to verify
        setStatusData(data);
      } catch (error) {
        console.error("Error fetching status data:", error);
      } finally {
        setLoading(false);
      }
    };

    // Fetch data initially
    fetchStatus();

    // Set up polling to fetch data every 1s
    intervalId = setInterval(fetchStatus, 10);

    // Cleanup interval on component unmount
    return () => clearInterval(intervalId);
  }, []);

  if (loading) return <p>Loading...</p>; // Show loading text while fetching
  if (!statusData) return <p>No data available.</p>; // Handle case where data is not available

  return (
    <div className="Status">
      <h2>ThinkTop V70 Status</h2>

      {/* PLC Inputs Section */}
      <section>
        <h3>PLC Inputs</h3>
        <div className="indicator-container">
          <div className={`indicator-box ${statusData.SV1 ? "active" : "inactive"}`}>
            SV1 (Main Valve): {statusData.SV1 ? "Active" : "Inactive"}
          </div>
          <div className={`indicator-box ${statusData.SV2 ? "active" : "inactive"}`}>
            SV2 (Upper Seat): {statusData.SV2 ? "Active" : "Inactive"}
          </div>
          <div className={`indicator-box ${statusData.SV3 ? "active" : "inactive"}`}>
            SV3 (Lower Seat): {statusData.SV3 ? "Active" : "Inactive"}
          </div>
        </div>
      </section>

      {/* Valve Feedback Section */}
      <section>
        <h3>Valve Feedback</h3>
        <div className="indicator-container">
          <div className={`indicator-box ${statusData.EN ? "active" : "inactive"}`}>
            EN (Main Valve): {statusData.EN ? "Active" : "Inactive"}
          </div>
          <div className={`indicator-box ${statusData.USL ? "active" : "inactive"}`}>
            USL (Upper Seat): {statusData.USL ? "Active" : "Inactive"}
          </div>
          <div className={`indicator-box ${statusData.LSP ? "active" : "inactive"}`}>
            LSP (Lower Seat): {statusData.LSP ? "Active" : "Inactive"}
          </div>
        </div>
      </section>
    </div>
  );
}

export default Status;
