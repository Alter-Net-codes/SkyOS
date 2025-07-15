import os
import subprocess
import sys
import hashlib

# Dev flag (set to False before release)
dev = False

# Use the script's directory, not cwd
this_dir = os.path.dirname(os.path.abspath(__file__))
kernel_script = os.path.join(this_dir, '..', 'kernel', 'kernel.py')

# File paths (SkyOS standard layout)
root_dir = os.path.join(this_dir, '..')
username_file = os.path.join(root_dir, 'username.txt')
password_file = os.path.join(root_dir, 'password.txt')
signed_in_file = os.path.join(root_dir, 'signed_in.txt')

if dev:
    print("Dev mode is ON. Be cautious.")
    dev_askfileset = input("Override default file paths? [yes/no]: ").strip().lower()
    if dev_askfileset == "yes":
        username_file = input("Enter custom username file path (include '.txt'): ").strip()
        password_file = input("Enter custom password file path (include '.txt'): ").strip()

# Ask if user wants to delete existing files (for reset)
todel = input("Are you here to reset your username/password? [yes/no]: ").strip().lower()

if os.path.isfile(username_file):
    if todel == "yes":
        os.remove(username_file)
        print("Username file deleted.")
    else:
        sys.exit()

if os.path.isfile(password_file):
    if todel == "yes":
        os.remove(password_file)
        print("Password file deleted.")
    else:
        sys.exit()

# Create new login info
username = input("Enter new username: ")
password = hashlib.sha256(input("Enter new password: ").encode()).hexdigest()

with open(username_file, "w") as f:
    f.write(username)

with open(password_file, "w") as f:
    f.write(password)

with open(signed_in_file, "w") as f:
    f.write("0")

print("Setup finished. Thank you for using SkyOS!")
print("Launching kernel...")

# Launch the kernel
if os.path.isfile(kernel_script):
    try:
        subprocess.run([sys.executable, kernel_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Kernel exited with error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
else:
    print("Kernel script not found. Make sure it exists at .\\kernel\\kernel.py")
