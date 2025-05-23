import React, { useState } from 'react';
import Banner from './Banner';
import ChatWindow from './ChatWindow';
import ChatInput from './ChatInput';
import './Chat.css';

const Chat = () => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = async (content) => {
    // Add user message to UI with type for display
    setMessages(prev => [...prev, { type: 'user', content }]);

    try {
      // Convert messages to the format expected by the API
      const apiMessages = messages.map(msg => ({
        role: msg.type === 'user' ? 'user' : 'assistant',
        content: msg.content
      }));

      // Add the new message
      apiMessages.push({ role: 'user', content });

      const response = await fetch('/chat/api/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ messages: apiMessages }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setMessages(prev => [...prev, { type: 'assistant', content: data.message }]);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => [...prev, { 
        type: 'assistant', 
        content: 'Sorry, I encountered an error. Please try again.' 
      }]);
    }
  };

  return (
    <div className="chat-container">
      <Banner />
      <ChatWindow messages={messages} />
      <ChatInput onSendMessage={handleSendMessage} />
    </div>
  );
};

export default Chat; 