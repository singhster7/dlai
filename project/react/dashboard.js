// Dashboard.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [analytics, setAnalytics] = useState({});
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    // Fetch analytics data
    axios.get('/api/analytics')
      .then(res => setAnalytics(res.data))
      .catch(err => console.error(err));

    // Fetch posts
    axios.get('/api/posts')
      .then(res => setPosts(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Analytics</h2>
      {/* Display analytics data */}
      <h2>Posts</h2>
      {/* Display posts */}
    </div>
  );
};

export default Dashboard;
