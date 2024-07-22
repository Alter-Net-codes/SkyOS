# skyOS 2.1 doesn't need C code to shut down the computer.
# why a shell command?

import subprocess
import os
import sys
from datetime import datetime
import pytz
import platform

treevalue = 1

print("Welcome to skyOS! Thank you to all those contributors who worked on this!")
print("Hope you find this OS useful!")
print("SkyOS v2.1 OSCore python3")

# Assuming the apps directory is one level up from the KERNEL directory
apps_dir = os.path.join(os.path.dirname(os.getcwd()), 'apps')

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
        print("time - see the time in 12hr format")
        print("shutdown - shut down the system")
        print("reboot - reboot the system")
        print("shell - run a shell command")
        print("applescript - Run AppleScript code (needs a Mac)")
    
    elif command == "time":
        # Specify the timezone.
        timezone = pytz.timezone(input("Enter your time zone (for example, 'America/New_York' is best used in US states like Kentucky or New York): "))

        # Get the current time in the specified timezone
        now = datetime.now(timezone)

        # Format the date and time as a 12-hour clock with AM/PM
        current_time = now.strftime("%I:%M %p")

        # Print the current date and time
        print(current_time)
    
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
        script_path = os.path.join(apps_dir, input("Enter the app name: (with a .py i belive if youre testing this go to the SkyOS repo and tell me if otherwise"))
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
        os_option = input("Are you sure? Type 'yes' to confirm.")
        if os_option == "yes":
            if system.platform() == "Darwin":
                os.system("shutdown -h now")
            elif system.platform() == "Linux":
                os.system("shutdown -h now")
            elif system.platform() == "Windows":
                os.system("shutdown /s")
        else:
            print("Shutdown cancelled.")
            continue
    elif command == "reboot":
        os_option = input("Are you sure? Type 'yes' to confirm.")
        if os_option == "yes":
            if system.platform() == "Darwin":
                os.system("shutdown -r now")
            elif system.platform() == "Linux":
                os.system("shutdown -r now")
            elif system.platform() == "Windows":
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

    elif command == "BIOS":
     script_path = os.path.join('kernel_dir', 'BIOS_dir', 'BIOS.py')
            if os.path.isfile(script_path):
                try:
                    subprocess.run([sys.executable, script_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing the script: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                print("App not found in the 'bios' directory.")
        

    else:
        print(command + " is not a valid command. Type 'help' for a list of commands.")
