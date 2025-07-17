#!/usr/bin/env python
"""
Debug script to test API endpoints and see JSON responses
Run this script to test the authentication and chat APIs
"""

import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_authentication():
    """Test the authentication endpoint"""
    print("=== TESTING AUTHENTICATION API ===")
    
    # Test data
    test_cases = [
        {
            "name": "Valid credentials",
            "data": {"username": "admin", "password": "admin123"},
            "expected_status": 200
        },
        {
            "name": "Invalid username",
            "data": {"username": "nonexistent", "password": "password"},
            "expected_status": 401
        },
        {
            "name": "Invalid password",
            "data": {"username": "admin", "password": "wrongpassword"},
            "expected_status": 401
        },
        {
            "name": "Missing username",
            "data": {"password": "admin123"},
            "expected_status": 400
        },
        {
            "name": "Missing password",
            "data": {"username": "admin"},
            "expected_status": 400
        },
        {
            "name": "Empty data",
            "data": {},
            "expected_status": 400
        }
    ]
    
    for test_case in test_cases:
        print(f"\n--- {test_case['name']} ---")
        print(f"Request data: {test_case['data']}")
        
        try:
            response = requests.post(
                f"{BASE_URL}/auth/login/",
                json=test_case['data'],
                headers={'Content-Type': 'application/json'}
            )
            
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {dict(response.headers)}")
            
            try:
                response_data = response.json()
                print(f"Response JSON: {json.dumps(response_data, indent=2)}")
            except json.JSONDecodeError:
                print(f"Response Text: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("ERROR: Could not connect to server. Make sure Django is running on localhost:8000")
        except Exception as e:
            print(f"ERROR: {str(e)}")

def test_chat_api():
    """Test the chat API endpoint"""
    print("\n=== TESTING CHAT API ===")
    
    # Test data
    test_message = {
        "messages": [
            {"role": "user", "content": "Hello, what is cybersecurity?"}
        ],
        "username": "admin"
    }
    
    print(f"Request data: {json.dumps(test_message, indent=2)}")
    
    try:
        response = requests.post(
            f"{BASE_URL}/chat/api/",
            json=test_message,
            headers={'Content-Type': 'application/json'}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        try:
            response_data = response.json()
            print(f"Response JSON: {json.dumps(response_data, indent=2)}")
        except json.JSONDecodeError:
            print(f"Response Text: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to server. Make sure Django is running on localhost:8000")
    except Exception as e:
        print(f"ERROR: {str(e)}")

def check_server_status():
    """Check if the server is running"""
    print("=== CHECKING SERVER STATUS ===")
    
    try:
        response = requests.get(f"{BASE_URL}/test/")
        print(f"Server is running! Status: {response.status_code}")
        
        try:
            data = response.json()
            print(f"Test endpoint response: {data}")
        except:
            print(f"Response text: {response.text}")
        
        return True
    except requests.exceptions.ConnectionError:
        print("ERROR: Server is not running. Please start Django with: python manage.py runserver")
        return False
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    print("API Debug Tool")
    print("=" * 50)
    
    # Check if server is running
    if check_server_status():
        # Test authentication
        test_authentication()
        
        # Test chat API
        test_chat_api()
    else:
        print("\nPlease start the Django server first:")
        print("1. Activate virtual environment: venv\\Scripts\\activate")
        print("2. Start server: python manage.py runserver")
        print("3. Run this script again") 