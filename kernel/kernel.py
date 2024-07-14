import subprocess
import os
import sys
from datetime import datetime
import pytz

treevalue = 1
print("Welcome to the skyOS! Thank you to all those contributors who worked on this!")
print("Hope you find this OS useful!")
print("SkyOS v2.0 OScore python3")

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
        print("helloworld.app - run the helloworld application")
        print("simpletext.app - run the simple text app by scratch_fakemon!")
        print("tree - create a value for tree. use the -p command to print the value.")
        print("history - show all command history")
        print("time - see the time in 12hr format")
    
    elif command == "time":
        # Specify the timezone.
        timezone = pytz.timezone('America/Los_Angeles')

        # Get the current time in the specified timezone
        now = datetime.now(timezone)

        # Format the date and time as a 12-hour clock with AM/PM
        current_time = now.strftime("%I:%M %p")

        # Print the current date and time
        print(current_time)
    
    elif command == "info":
        print("Developed by the SCA and Alter Net codes. All rights reserved.")
        print("This kernel may not be reproduced in any way.")
        print("You can archive (make sure the archive is public).")
        print("v2.0 python3, c23")
        
    
    elif command == "echo":
        echotxt = input("Echo what: ").strip()
        print(echotxt)

    elif command == "tree":
        treevalue = input("tree:")
        print("the value of tree is set.")
    elif command == "tree -p":
        print(treevalue)

    elif command == "helloworld.app":
        script_path = os.path.join(apps_dir, 'helloworldapp.py')
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("helloworldapp.py not found in the 'apps' directory.")
      
    elif command == "simpletext.app":
        script_path = os.path.join(apps_dir, 'simpletextapp.py')
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("simpletextapp.py not found in the 'apps' directory.")
    
    elif command == "history":
        print("Command History:")
        for index, cmd in enumerate(command_history, start=1):
            print(f"{index}: {cmd}")
    
    else:
        print("Not a valid command. Type 'help' for a list of commands.")
