// API Configuration
const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'http://localhost:8000'  // Production URL (change this to your production domain)
  : 'http://localhost:8000'; // Development URL

export const API_ENDPOINTS = {
  AUTH_LOGIN: `${API_BASE_URL}/auth/login/`,
  CHAT_API: `${API_BASE_URL}/chat/api/`,

  TEST: `${API_BASE_URL}/test/`,
};

export default API_BASE_URL; 