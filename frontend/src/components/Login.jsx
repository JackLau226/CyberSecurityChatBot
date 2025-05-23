import React, { useState } from 'react';
import './Login.css';

const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const checkCredentials = (username, password) => {
    // Hardcoded check for now
    //return username === 'example@email.com' && password === 'Password';
    return true;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (checkCredentials(username, password)) {
      setError('');
      onLogin();
    } else {
      setError('Invalid username or password');
    }
  };

  return (
    <div className="login-bg">
      <form className="login-box" onSubmit={handleSubmit}>
        <h2 className="login-title">Login</h2>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={e => setUsername(e.target.value)}
          className="login-input"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          className="login-input"
        />
        {error && <div className="login-error">{error}</div>}
        <button type="submit" className="login-btn">Login</button>
      </form>
    </div>
  );
};

export default Login; 