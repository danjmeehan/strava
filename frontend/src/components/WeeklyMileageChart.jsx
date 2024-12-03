import { useEffect, useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const CustomTooltip = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    console.log('Tooltip payload:', payload);
    
    // Convert the week start date to a Date object
    const weekStart = new Date(label);
    // Calculate the week end date (6 days after start)
    const weekEnd = new Date(weekStart);
    weekEnd.setDate(weekEnd.getDate() + 6);
    
    // Format dates as "MMM D"
    const formatDate = (date) => {
      return date.toLocaleDateString('en-US', { 
        month: 'short', 
        day: 'numeric'
      });
    };

    return (
      <div className="custom-tooltip" style={{
        backgroundColor: 'white',
        padding: '10px',
        border: '1px solid #ccc',
        borderRadius: '4px'
      }}>
        <p>Week of {formatDate(weekStart)} - {formatDate(weekEnd)}</p>
        <p>Miles: {payload[0].value}</p>
        <p>Longest Run: {payload[0].payload.longest_run} miles</p>
        <p>Average Pace: {payload[0].payload.avg_pace}/mi</p>
      </div>
    );
  }
  return null;
};

function WeeklyMileageChart() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/activities/stats/weekly?weeks=12');
        setData(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div style={{ width: '100%', height: 400 }}>
      <h2>Weekly Running Mileage</h2>
      <ResponsiveContainer>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="week" 
            tickFormatter={(date) => {
              return new Date(date).toLocaleDateString('en-US', { 
                month: 'short', 
                day: 'numeric' 
              });
            }}
          />
          <YAxis />
          <Tooltip content={<CustomTooltip />} />
          <Bar dataKey="miles" name="Weekly Miles" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default WeeklyMileageChart;