import requests
import json

# Test the complete auth flow
print("Testing authentication flow...")

# 1. Signup
signup_data = {
    "name": "Test User",
    "email": "test@example.com",
    "password": "testpassword123"
}

print("1. Signing up...")
signup_response = requests.post("http://localhost:8000/api/auth/signup", json=signup_data)
print(f"Signup status: {signup_response.status_code}")
if signup_response.status_code == 200:
    print("Signup successful")
else:
    print(f"Signup failed: {signup_response.text}")

# 2. Login
login_data = {
    "username": "test@example.com",
    "password": "testpassword123"
}

print("\n2. Logging in...")
login_response = requests.post(
    "http://localhost:8000/api/auth/login",
    data=login_data,
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)
print(f"Login status: {login_response.status_code}")
if login_response.status_code == 200:
    token_data = login_response.json()
    token = token_data["access_token"]
    print(f"Login successful, token: {token[:20]}...")
else:
    print(f"Login failed: {login_response.text}")
    exit()

# 3. Access protected endpoint
print("\n3. Accessing protected endpoint...")
headers = {"Authorization": f"Bearer {token}"}
protected_response = requests.get("http://localhost:8000/api/users/me", headers=headers)
print(f"Protected endpoint status: {protected_response.status_code}")
if protected_response.status_code == 200:
    user_data = protected_response.json()
    print(f"User data retrieved: {user_data}")
else:
    print(f"Protected endpoint failed: {protected_response.text}")