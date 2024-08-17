# setup.py

# Prompt the user for their username
username = input("Enter your username: ")

# Prompt the user for their password
password = input("Enter your password: ")

# Create a file named 'username.txt' and write the username in it
with open("username.txt", "w") as user_file:
    user_file.write(username)

# Create a file named 'password.txt' and write the password in it
with open("password.txt", "w") as password_file:
    password_file.write(password)

print("setup finished! thank you for using SkyOS!")
