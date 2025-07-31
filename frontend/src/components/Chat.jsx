import React, { useState } from 'react';
import Banner from './Banner';
import ChatWindow from './ChatWindow';
import ChatInput from './ChatInput';
import { API_ENDPOINTS } from '../config';
import './Chat.css';

const Chat = ({ username }) => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (content) => {
    try {
      setIsLoading(true);
      
      // Immediately add user message to UI
      setMessages(prev => [
        ...prev,
        { type: 'user', content }
      ]);

      // Prepare messages for API (include the new user message)
      const apiMessages = messages.map(msg => ({
        role: msg.type === 'user' ? 'user' : 'assistant',
        content: msg.content
      }));
      // Add new user message to payload
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
      // Add only assistant message to UI state (user message already added)
      setMessages(prev => [
        ...prev,
        { type: 'assistant', content: data.message }
      ]);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => [
        ...prev,
        { type: 'assistant', content: 'Sorry, I encountered an error. Please try again.' }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <Banner />
      <ChatWindow messages={messages} />
      <ChatInput onSendMessage={handleSendMessage} isDisabled={isLoading} />
    </div>
  );
};

export default Chat; 