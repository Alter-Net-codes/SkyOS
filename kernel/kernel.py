import subprocess
import os
import sys
import platform
import time
from datetime import datetime

current_hour = datetime.now().hour
version = "SkyOS"
treevalue = None

def panic(errorCode):   
    print(f"SkyOS has crashed. Error code: {errorCode}")
    time.sleep(10)
    sys.exit()


# Function to get the username based on the OS
def get_username():
    if platform.system() == "Windows":
        return os.getlogin()  # or os.environ['USERNAME']
    else:
        return os.getenv('USER')


username = get_username()

# Set up paths for setup, BIOS, and apps based on the OS
if platform.system() == "Windows":
    setup_script_path = rf'C:\Users\{username}\downloads\{version}\setup\setup.py'
    BIOS_location = rf'C:\Users\{username}\downloads\{version}\BIOS'
    apps_dir = rf'C:\Users\{username}\downloads\{version}\apps'
    bios_log_location = rf'C:\Users\{username}\downloads\{version}\bios_log.txt'

elif platform.system() == "Linux":
    setup_script_path = f'/home/{username}/downloads/{version}/setup/setup.py'
    BIOS_location = f'/home/{username}/downloads/{version}/BIOS'
    apps_dir = f'/home/{username}/downloads/{version}/apps'
    bios_log_location = f'/home/{username}/downloads/{version}/bios_log.txt'

elif platform.system() == "Darwin":
    setup_script_path = f'/Users/{username}/Downloads/{version}/setup/setup.py'
    BIOS_location = f'/Users/{username}/Downloads/{version}/BIOS'
    apps_dir = f'/Users/{username}/Downloads/{version}/apps'
    bios_log_location = f'/Users/{username}/Downloads/{version}/bios_log.txt'

else:
    raise Exception("Unsupported operating system. Please use Windows, Linux, or macOS.")


# Function to run the setup script
def run_setup():
    print(f"supposed setup path: {setup_script_path}")
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
        panic("COULD_NOT_FIND_SETUP")
        sys.exit()

# Check if the required files exist
if not os.path.isfile("username.txt") or not os.path.isfile("password.txt"):
    print("Username or password file is missing. Running setup...")
    run_setup()

# After setup, check again for username and password
with open("username.txt", "r") as user_file: # if you used the CFP control devtool in the setup script then change this .txt files name accordingly.
    stored_username = user_file.read().strip()

with open("password.txt", "r") as password_file:
    stored_password = password_file.read().strip() # if you used the CFP control devtool in the setup script then change this .txt files name accordingly.

authenticated = False

# password
while not authenticated:
    password = input(f"Enter your password, {stored_username}: ").strip()

    if password == stored_password:
        print(f"Welcome, {stored_username}!")
        authenticated = True
    else:
        print("Incorrect password. try again")

if current_hour < 12:
    print(f"Good morning, {sotred_username} welcome back.")
else:
    print(f"Good afternoon, {stored_username} welcome back.")

# Continue with the SkyOS boot process
print("Welcome back to SkyOS! Thank you to all those contributors who worked on this!")
print(f"{version} written in Python3")
print("for more info on the project type info, help or copyright")
today = datetime.today()
if today.month == 10 and today.day == 31:
    print("HAPPY HALLOWEEN 🎃")
if today.month == 12 and today.day == 25:
    print("MERRY CHRTISTMAS 🎅")
if today.month == 4 and today.day == 1:
    print("APRIL FOOLS 😏")

command_history = []

while True:
    command = input("command: ").strip().lower()
    command_history.append(command)

    if command == "help":
        print("Available commands:")
        print("help - show the help message")
        print("info - show information about SkyOS")
        print("copyright - copyright info")
        print("echo - echo back what you type")
        print("app - run an application")
        print("tree - create a value for tree. use the -p parameter to print the value.")
        print("history - show all command history")
        print("shutdown - shut down the system")
        print("reboot - reboot the system")
        print("bios - run the bios")
        print("setup - run the setup script to reset your username and password")
        print("bios log - print out the bios log")
        print("afk - hold the os in a safe envoirment while you are 'afk'")

    elif command == "afk":
        sys.clear()
        input("in afk mode... press enter to cancel ")
        
    elif command == "bios log":
        try:
            with open(bios_log_location, 'r') as file:
                # Read the content of the file
                file_content = file.read()

                # Print the content
                print("File Content:\n", file_content)

        except FileNotFoundError:
            print(f"File '{bios_log_location}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif command == "info":
        print("Developed by the SCA and Alter Net codes. All rights reserved.")
        print("This kernel may be reproduced if it meets the licenses terms. more info in the copyright command.")
        print(f"Current SkyOS version: {version}")

    elif command == "copyright":
        print("Copyright © 2024 Alter Net codes and the SCA all rights reserved")
        print("if you are adding on to this software, or want to hold a copy of this software,")
        print("then you can get info on copyright in the 'license' file in the root directory.")

    elif command == "echo":
        echotxt = input("Echo what: ").strip()
        print(echotxt)

    elif command == "tree":
        treevalue = input("tree: ")
        print("The value of tree is set.")
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

    elif command == "bios":
        if authenticated:
            script_path = os.path.join(BIOS_location, 'BIOS.py')
            if os.path.isfile(script_path):
                try:
                    subprocess.run([sys.executable, script_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing the script: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                panic("MISSING_BIOS")
                break
        else:
            print("You must be authenticated to run the BIOS.")

    elif command == "setup":
        run_setup()

    elif command == "135795":
        print("You found the easter egg")
        print("But... where did you find the password?")
    
    elif command == "panic":
        panic("test_panic")

    else:
        print(command + " is not a valid command. Type 'help' for a list of commands.")

panic()
