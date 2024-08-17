import subprocess
import os
import sys
import platform

treevalue = 1
panicErrorCode = None

def panic(errorCode):
    print(f"skyOS has crashed. Error code: {errorCode}")

# Define the path to the setup.py script in the setup directory
setup_script_path = os.path.join(os.getcwd(), 'setup', 'setup.py')

# Check if the required files exist
if not os.path.isfile("username.txt") or not os.path.isfile("password.txt"):
    print("Username or password file is missing. Running setup...")
    
    if os.path.isfile(setup_script_path):
        try:
            subprocess.run([sys.executable, setup_script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the setup script: {e}")
            sys.exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit()
    else:
        print("Setup script not found. Please ensure 'setup.py' is in the 'setup' directory.")
        sys.exit()

# After setup, check again for username and password
with open("username.txt", "r") as user_file:
    stored_username = user_file.read().strip()

with open("password.txt", "r") as password_file:
    stored_password = password_file.read().strip()

# Check if the user has used SkyOS before
used_before = input("Have you used SkyOS before? (yes/no): ").strip().lower()

if used_before == "yes":
    password = input(f"Enter your password, {stored_username}: ").strip()
    
    if password == stored_password:
        print(f"Welcome, {stored_username}!")
    else:
        print("Incorrect password. Please run the setup again.")
        sys.exit()
else:
    print("Please run the setup to create a username and password.")
    sys.exit()

# Continue with the SkyOS boot process
print("Welcome to SkyOS! Thank you to all those contributors who worked on this!")
print("Hope you find this OS useful!")
print("SkyOS v2.4 architecture written in Python3")

# Assuming the apps directory is one level up from the KERNEL directory
apps_dir = os.path.join(os.path.dirname(os.getcwd()), 'apps')
BIOS_location = os.path.join(os.path.dirname(os.getcwd()), "BIOS")

command_history = []

while True:
    command = input("command: ").strip().lower()
    command_history.append(command)
    
    if command == "help":
        print("Available commands:")
        print("help - show this help message")
        print("info - show information about this program")
        print("echo - echo back what you type")
        print("app - run an application")
        print("tree - create a value for tree. use the -p command to print the value.")
        print("history - show all command history")
        print("shutdown - shut down the system")
        print("reboot - reboot the system")
        print("shell - run a shell command")
        print("applescript - Run AppleScript code (needs a Mac)")
        print("bios - run the bios")
    
    elif command == "info":
        print("Developed by the SCA. All rights reserved.")
        print("This kernel may be reproduced in any way under the MIT License.")
        print("You can archive (make sure the archive is public).")
    
    elif command == "echo":
        echotxt = input("Echo what: ").strip()
        print(echotxt)

    elif command == "tree":
        treevalue = input("tree:")
        print("the value of tree is set.")
    elif command == "tree -p":
        print(treevalue)
        
    elif command == "app":
        script_path = os.path.join(apps_dir, input("Enter the app name (with a .py):"))
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("App not found in the 'apps' directory.")
            
    elif command == "history":
        print("Command History:")
        for index, cmd in enumerate(command_history, start=1):
            print(f"{index}: {cmd}")

    elif command == "shutdown":
        os_option = input("Are you sure? Type 'yes' to confirm: ")
        if os_option == "yes":
            if platform.system() == "Darwin":
                os.system("shutdown -h now")
            elif platform.system() == "Linux":
                os.system("shutdown -h now")
            elif platform.system() == "Windows":
                os.system("shutdown /s")
        else:
            print("Shutdown cancelled.")
            continue
            
    elif command == "reboot":
        os_option = input("Are you sure? Type 'yes' to confirm: ")
        if os_option == "yes":
            if platform.system() == "Darwin":
                os.system("shutdown -r now")
            elif platform.system() == "Linux":
                os.system("shutdown -r now")
            elif platform.system() == "Windows":
                os.system("shutdown /r")
        else:
            print("Reboot cancelled.")
            continue

    elif command == "shell":
        os.system(input("Enter a shell command: "))
    elif command == "applescript":
        if platform.system() == "Darwin":
            os.system("oascript" + input("Enter your AppleScript file or command: "))
        else:
            print("You need a Mac for this!")

    elif command == "bios":
        script_path = os.path.join(BIOS_location, 'BIOS.py')
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            panicErrorCode = "MISSING_BIOS"
            break
            
    else:
        print(command + " is not a valid command. Type 'help' for a list of commands.")

panic(panicErrorCode)
