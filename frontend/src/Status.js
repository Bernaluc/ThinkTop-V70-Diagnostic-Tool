import React, { useEffect, useState } from 'react';
import './Status.css';

function Status() {
  const [statusData, setStatusData] = useState({
    SV1: null,
    SV2: null,
    SV3: null,
    EN: null,
    USL: null,
    LSP: null
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await fetch("localhost:5000/api/status");

        
        if (!response.ok) {
          throw new Error(`Error ${response.status}: ${response.statusText}`);
        }
        
        const data = await response.json();
        console.log("Fetched data:", data);
        setStatusData(data);
        setError(null);
      } catch (err) {
        console.error("Error fetching status data:", err);
        setError("Could not load status data.");
      } finally {
        setLoading(false);
      }
    };

    fetchStatus();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="Status">
      <h2>ThinkTop V70 Status</h2>

      {/* PLC Inputs Section */}
      <section>
        <h3>PLC Inputs</h3>
        <div className="indicator-container">
          <div className={`indicator-box ${statusData.SV1 === null ? "no-data" : (statusData.SV1 ? "active" : "inactive")}`}>
            SV1 (Main Valve): {statusData.SV1 === null ? "No Data" : (statusData.SV1 ? "Active" : "Inactive")}
          </div>
          <div className={`indicator-box ${statusData.SV2 === null ? "no-data" : (statusData.SV2 ? "active" : "inactive")}`}>
            SV2 (Upper Seat): {statusData.SV2 === null ? "No Data" : (statusData.SV2 ? "Active" : "Inactive")}
          </div>
          <div className={`indicator-box ${statusData.SV3 === null ? "no-data" : (statusData.SV3 ? "active" : "inactive")}`}>
            SV3 (Lower Seat): {statusData.SV3 === null ? "No Data" : (statusData.SV3 ? "Active" : "Inactive")}
          </div>
        </div>
      </section>

      {/* Valve Feedback Section */}
      <section>
        <h3>Valve Feedback</h3>
        <div className="indicator-container">
          <div className={`indicator-box ${statusData.EN === null ? "no-data" : (statusData.EN ? "active" : "inactive")}`}>
            EN (Main Valve): {statusData.EN === null ? "No Data" : (statusData.EN ? "Active" : "Inactive")}
          </div>
          <div className={`indicator-box ${statusData.USL === null ? "no-data" : (statusData.USL ? "active" : "inactive")}`}>
            USL (Upper Seat): {statusData.USL === null ? "No Data" : (statusData.USL ? "Active" : "Inactive")}
          </div>
          <div className={`indicator-box ${statusData.LSP === null ? "no-data" : (statusData.LSP ? "active" : "inactive")}`}>
            LSP (Lower Seat): {statusData.LSP === null ? "No Data" : (statusData.LSP ? "Active" : "Inactive")}
          </div>
        </div>
      </section>
    </div>
  );
}

export default Status;
