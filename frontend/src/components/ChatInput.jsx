import React, { useState } from 'react';
import './ChatInput.css';

const ChatInput = ({ onSendMessage, isDisabled = false }) => {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim() && !isDisabled) {
      onSendMessage(message);
      setMessage('');
    }
  };

  return (
    <div className="chat-input">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask about cybersecurity..."
          disabled={isDisabled}
        />
        <button type="submit" disabled={isDisabled}>
          {isDisabled ? 'Sending...' : 'Send'}
        </button>
      </form>
    </div>
  );
};

export default ChatInput; 