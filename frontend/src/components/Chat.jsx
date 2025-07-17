import React, { useState } from 'react';
import Banner from './Banner';
import ChatWindow from './ChatWindow';
import ChatInput from './ChatInput';
import { API_ENDPOINTS } from '../config';
import './Chat.css';

const Chat = ({ username }) => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = async (content) => {
    try {
      // Prepare messages for API (do NOT include the new user message yet)
      const apiMessages = messages.map(msg => ({
        role: msg.type === 'user' ? 'user' : 'assistant',
        content: msg.content
      }));
      // Add the new user message to the API payload
      apiMessages.push({ role: 'user', content });

      const response = await fetch(API_ENDPOINTS.CHAT_API, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          messages: apiMessages,
          username: username 
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      // Only now add both user and assistant messages to UI state
      setMessages(prev => [
        ...prev,
        { type: 'user', content },
        { type: 'assistant', content: data.message }
      ]);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => [
        ...prev,
        { type: 'assistant', content: 'Sorry, I encountered an error. Please try again.' }
      ]);
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