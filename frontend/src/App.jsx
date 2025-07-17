import React, { useState } from 'react';
import Chat from './components/Chat';
import Login from './components/Login';
import './App.css';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [username, setUsername] = useState('');

  const handleLogin = (username) => {
    setUsername(username);
    setLoggedIn(true);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {loggedIn ? <Chat username={username} /> : <Login onLogin={handleLogin} />}
    </div>
  );
}

export default App;
