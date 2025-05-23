import React, { useState } from 'react';
import './ChatInput.css';

const ChatInput = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');
  const [isDisabled, setIsDisabled] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim() && !isDisabled) {
      setIsDisabled(true);
      onSendMessage(message);
      setMessage('');
      setIsDisabled(false);
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
          Send
        </button>
      </form>
    </div>
  );
};

export default ChatInput; 