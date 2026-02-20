users = {
    "admin": "1234",
    "user": "password"
}

username = input("Username: ")
password = input("Password: ")

if users.get(username) == password :
    print("Login successful!")
else:
    print("Invalid username or password!")
