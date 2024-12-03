import { useEffect, useState } from 'react';
import axios from 'axios';

function RunsTable() {
  const [runs, setRuns] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRuns = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/activities/runs');
        setRuns(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchRuns();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div style={{ padding: '20px' }}>
      <h2>My Runs</h2>
      <table style={{ 
        width: '100%', 
        borderCollapse: 'collapse', 
        marginTop: '20px',
        backgroundColor: 'white',
        boxShadow: '0 1px 3px rgba(0,0,0,0.2)'
      }}>
        <thead>
          <tr style={{ backgroundColor: '#f5f5f5' }}>
            <th style={{ padding: '12px', textAlign: 'left', borderBottom: '2px solid #ddd' }}>Date</th>
            <th style={{ padding: '12px', textAlign: 'right', borderBottom: '2px solid #ddd' }}>Miles</th>
            <th style={{ padding: '12px', textAlign: 'right', borderBottom: '2px solid #ddd' }}>Average Pace</th>
            <th style={{ padding: '12px', textAlign: 'left', borderBottom: '2px solid #ddd' }}>Comments</th>
          </tr>
        </thead>
        <tbody>
          {runs.map((run) => (
            <tr key={run.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={{ padding: '12px' }}>
                {new Date(run.start_date).toLocaleDateString()}
              </td>
              <td style={{ padding: '12px', textAlign: 'right' }}>
                {(run.distance * 0.000621371).toFixed(2)}
              </td>
              <td style={{ padding: '12px', textAlign: 'right' }}>
                {run.avg_pace}
              </td>
              <td style={{ padding: '12px' }}>
                {run.comments || 'No comments'}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default RunsTable;
