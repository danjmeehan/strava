import { useState } from 'react';
import axios from 'axios';
import WeeklyMileageChart from './components/WeeklyMileageChart';
import RunsTable from './components/RunsTable';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('chart');
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
      
      <div style={{ marginBottom: '20px' }}>
        <button 
          onClick={() => setActiveTab('chart')}
          style={{
            padding: '10px 20px',
            marginRight: '10px',
            backgroundColor: activeTab === 'chart' ? '#4CAF50' : '#f0f0f0',
            color: activeTab === 'chart' ? 'white' : 'black',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Chart
        </button>
        <button 
          onClick={() => setActiveTab('table')}
          style={{
            padding: '10px 20px',
            marginRight: '10px',
            backgroundColor: activeTab === 'table' ? '#4CAF50' : '#f0f0f0',
            color: activeTab === 'table' ? 'white' : 'black',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Table
        </button>
        <button 
          onClick={handleSync}
          disabled={syncing}
          style={{
            padding: '10px 20px',
            backgroundColor: syncing ? '#cccccc' : '#2196F3',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: syncing ? 'not-allowed' : 'pointer'
          }}
        >
          {syncing ? 'Syncing...' : 'Sync with Strava'}
        </button>
      </div>

      {activeTab === 'chart' ? (
        <WeeklyMileageChart />
      ) : (
        <RunsTable />
      )}
    </div>
  );
}

export default App;
