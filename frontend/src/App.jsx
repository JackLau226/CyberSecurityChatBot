import React, { useState } from 'react';
import Chat from './components/Chat';
import Login from './components/Login';
import './App.css';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <div className="min-h-screen bg-gray-100">
      {loggedIn ? <Chat /> : <Login onLogin={() => setLoggedIn(true)} />}
    </div>
  );
}

export default App;
