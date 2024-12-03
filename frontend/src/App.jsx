import { useState } from 'react';
import axios from 'axios';
import WeeklyMileageChart from './components/WeeklyMileageChart';
import './App.css';

function App() {
  const [syncing, setSyncing] = useState(false);

  const handleSync = async () => {
    try {
      setSyncing(true);
      await axios.post('http://127.0.0.1:5000/activities/sync');
      window.location.reload();
    } catch (error) {
      console.error('Sync failed:', error);
      alert('Failed to sync with Strava');
    } finally {
      setSyncing(false);
    }
  };

  return (
    <div className="App">
      <h1>Running Dashboard</h1>
      <button 
        onClick={handleSync}
        disabled={syncing}
        style={{
          padding: '10px 20px',
          backgroundColor: syncing ? '#cccccc' : '#2196F3',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: syncing ? 'not-allowed' : 'pointer',
          margin: '10px 0'
        }}
      >
        {syncing ? 'Syncing...' : 'Sync with Strava'}
      </button>
      <WeeklyMileageChart />
    </div>
  );
}

export default App;
