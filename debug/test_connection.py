#!/usr/bin/env python
"""
Simple connection test script
"""

import requests
import json

def test_connection():
    """Test if the backend is accessible"""
    
    print("=== CONNECTION TEST ===")
    
    # Test 1: Basic connectivity
    try:
        response = requests.get("http://localhost:8000/test/")
        print(f"✓ Backend is accessible. Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Test endpoint response: {data}")
        else:
            print(f"✗ Unexpected status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to backend. Make sure Django is running on port 8000")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    # Test 2: Authentication endpoint
    try:
        response = requests.post(
            "http://localhost:8000/auth/login/",
            json={"username": "admin", "password": "admin123"},
            headers={"Content-Type": "application/json"}
        )
        
        print(f"✓ Authentication endpoint accessible. Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Authentication successful: {data}")
        elif response.status_code == 401:
            print("⚠ Authentication failed (expected if user doesn't exist)")
        else:
            print(f"✗ Unexpected status code: {response.status_code}")
            
    except Exception as e:
        print(f"✗ Authentication test failed: {e}")
    
    # Test 3: CORS headers
    try:
        response = requests.options(
            "http://localhost:8000/auth/login/",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type"
            }
        )
        
        print(f"✓ CORS preflight test. Status: {response.status_code}")
        print(f"  CORS headers: {dict(response.headers)}")
        
    except Exception as e:
        print(f"✗ CORS test failed: {e}")
    
    print("\n=== CONNECTION TEST COMPLETED ===")
    return True

if __name__ == "__main__":
    test_connection() 