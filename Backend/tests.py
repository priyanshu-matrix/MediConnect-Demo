import requests

# Create new auth
data = {
    "request_type": "new_auth",
    "email": "example@gmail.com",
    "password": "password",
}
response = requests.post("http://127.0.0.1:8000/api/auth", json=data)
print(response.json())

# Check auth
data = {
    "request_type": "check_auth",
    "email": "example@gmail.com",
    "password": "password",
}
response = requests.post("http://127.0.0.1:8000/api/auth", json=data)
print(response.json())
