# Debugging Guide - CyberSecurity Tutor AI

This guide shows you how to see JSON responses and debug communication between frontend and backend.

## 🔍 Methods to See JSON Responses

### 1. **Browser Developer Tools (Recommended)**

**Steps:**
1. Open your browser (Chrome, Firefox, Edge)
2. Press `F12` or right-click → "Inspect"
3. Go to the **Console** tab
4. Try logging in or sending a chat message
5. You'll see detailed logs including:
   - Request data being sent
   - Response status codes
   - Response headers
   - Response JSON data

**What you'll see:**
```
Response status: 200
Response headers: {content-type: "application/json", ...}
Response data: {status: "success", message: "Login successful"}
```

### 2. **Backend Console Logs**

**Steps:**
1. Start your Django server: `python manage.py runserver`
2. Watch the terminal/console where Django is running
3. Try logging in - you'll see detailed backend logs

**What you'll see:**
```
=== AUTHENTICATION REQUEST ===
Username: admin
Password: ******** (length: 8)
User found: admin
Password match: SUCCESS
RESPONSE: {'status': 'success', 'message': 'Login successful'}
```

### 3. **API Debug Script**

**Steps:**
1. Make sure Django server is running
2. Run: `python debug_api.py`
3. This will test all API endpoints and show responses

**What you'll see:**
```
=== TESTING AUTHENTICATION API ===

--- Valid credentials ---
Request data: {'username': 'admin', 'password': 'admin123'}
Status Code: 200
Response JSON: {
  "status": "success",
  "message": "Login successful"
}
```

### 4. **Network Tab in Developer Tools**

**Steps:**
1. Open Developer Tools (`F12`)
2. Go to the **Network** tab
3. Try logging in or sending a message
4. Click on the request to see:
   - Request headers and body
   - Response headers and body
   - Timing information

## 🐛 Common Issues and Solutions

### Issue: "Invalid credentials!" error
**Debug steps:**
1. Check browser console for request/response logs
2. Check Django console for backend logs
3. Verify user exists in database
4. Check password matching

### Issue: Network error
**Debug steps:**
1. Ensure Django server is running on port 8000
2. Check if frontend is making requests to correct URL
3. Verify CORS settings in Django

### Issue: Database connection error
**Debug steps:**
1. Run `python manage.py migrate` to set up database
2. Add test users using the provided scripts
3. Check if `db.sqlite3` file exists

## 📊 Expected JSON Responses

### Authentication Success:
```json
{
  "status": "success",
  "message": "Login successful"
}
```

### Authentication Failure:
```json
{
  "error": "Invalid credentials!"
}
```

### Chat API Success:
```json
{
  "message": "AI response content here...",
  "role": "assistant"
}
```

### Chat API Error:
```json
{
  "error": "Error message here"
}
```

## 🛠️ Tools Created for Debugging

1. **`debug_api.py`** - Standalone script to test APIs
2. **Enhanced logging** in both frontend and backend
3. **Console logs** in browser and Django terminal


## 📝 Quick Debug Checklist

- [ ] Django server running on port 8000
- [ ] Frontend running on port 5173
- [ ] Database migrated and test users added
- [ ] Browser developer tools open
- [ ] Console tab selected
- [ ] Network tab monitoring requests
- [ ] Backend console visible

## 🆘 Getting Help

If you're still having issues:
1. Check the browser console for JavaScript errors
2. Check the Django console for Python errors
3. Verify all environment variables are set
4. Ensure all dependencies are installed