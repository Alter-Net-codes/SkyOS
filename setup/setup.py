import os
import subprocess
import sys

# Path to the kernel script in the KERNEL folder
kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')

# File paths for storing username and password
username_file = "username.txt"
password_file = "password.txt"

# If files exist, prompt user if they want to delete them to allow setting up a new username and password.
todel = input("are you running this to reset your password and/or username [yes/no]: ").lower()
if os.path.isfile(username_file):
    if todel == "yes"
        os.remove(username_file)
        print(f"{username_file} has been deleted.")
    else:
        print("okay now leaving...")
        sys.exit()

if os.path.isfile(password_file):
    if todel == "yes"
        os.remove(password_file)
        print(f"{password_file} has been deleted.")
    else:
        print("okay now leaving...")
        sys.exit()

# Prompt the user for their username
username = input("Enter your username: ")

# Prompt the user for their password
password = input("Enter your password: ")

# Create a file named 'username.txt' and write the username in it
with open(username_file, "w") as user_file:
    user_file.write(username)

# Create a file named 'password.txt' and write the password in it
with open(password_file, "w") as password_file:
    password_file.write(password)

print("Setup finished! Thank you for using SkyOS!")
print("Going to the kernel file...")

# Check if the kernel script exists before trying to run it
if os.path.isfile(kernel_script):
    try:
        # Run the kernel script as a subprocess
        subprocess.run([sys.executable, kernel_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the kernel script: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
else:
    print("Kernel script not found. Please ensure it is located in the 'KERNEL' directory.")
