import subprocess
import os
import sys
import platform
import time
import hashlib
from datetime import datetime
import requests
import urllib.request

# hashed password for secutity purposes.
# Okay, I should explain what a SkyOS Aurora 1.2+ app is.
# A SkyOS Aurora 1.2+ app is a Python script that is located in in the apps folder,
# That can be ran by the kernel.
# Same, same. But diffrent.
# You can now run multiple files (in a folder inside the apps folder. So the launcher you make will run something like ./apps/myapp/script1.py and ./apps/myapp/script2.py)
# from a single app, for devs, this means you can port a whole game or app to SkyOS Aurora, without haing to make it a single file.
# Of course, each file has to fall back to the main file, which will have to fall back to the kernel.
# I might make a guide for how to make a SkyOS Aurora 1.2+ app, but for now, you can just follow the current sturcture, then add mutltiple files in the folder you run it from.
# Installers and stuff will soon be suported.
# okay well i am now doing this as a class project so i guess i have motivation now, uhhh lets go!

valid_version = "1.1.09s2725"

colors = {
    "sky_blue": "\033[38;5;39m",
    "bright_cyan": "\033[96m",
    "bright_magenta": "\033[95m",
    "bright_yellow": "\033[93m",
    "reset": "\033[0m",
    "clear": "\033[2J\033[H"
}

current_hour = datetime.now().hour
version = "SkyOS" # Yeahhhhhhhhhh.... the deafault will be SkyOS, so will it be when the user dowloads it. And I am lazy. Soooooooooooo... YEAH
treevalue = None

def print_boot_screen():
    print(colors["clear"], end="")

    skyos_art = r"""

   _____ _           ____   _____                                     
  / ____| |         / __ \ / ____|     /\                             
 | (___ | | ___   _| |  | | (___      /  \  _   _ _ __ ___  _ __ __ _ 
  \___ \| |/ / | | | |  | |\___ \    / /\ \| | | | '__/ _ \| '__/ _` |
  ____) |   <| |_| | |__| |____) |  / ____ \ |_| | | | (_) | | | (_| |
 |_____/|_|\_\\__, |\____/|_____/  /_/    \_\__,_|_|  \___/|_|  \__,_|
               __/ |                                                  
              |___/                                                               
    
"""

    print(colors["sky_blue"] + skyos_art + colors["reset"])
    print(f"{colors['bright_magenta']}Loading SkyOS Aurora 1.1...{colors['reset']}")
    time.sleep(5)
    os.system('cls' if platform.system() == "Windows" else 'clear')
    print(colors["clear"], end="")

# Function to get the username based on the OS
def get_username():
    if platform.system() == "Windows":
        return os.getlogin()  # or os.environ['USERNAME']
    else:
        return os.getenv('USER')

username = get_username()

this_dir = os.path.dirname(os.path.abspath(__file__))

root_path = os.path.abspath(os.path.join(this_dir, '..'))  # Go up two levels to get the root directory

RED = "\033[31m"
RESET = "\033[0m"

# User files at root
username_file = os.path.join(root_path, "username.txt")
password_file = os.path.join(root_path, "password.txt")
signed_in_file = os.path.join(root_path, "signed_in.txt")

def panic(errorCode):   
    print(f"SkyOS Aurora has crashed. Error code: {errorCode}")
    print("Please report this error to the SkyOS Aurora development team.")
    print("The system will now shut down to prevent further issues.")
    print("Shutting down in 10 seconds...")
    with open(signed_in_file, "w") as session_file:
        session_file.write("0")
    time.sleep(10)
    os._exit(0)

# Setup paths based on root_path
setup_script_path = os.path.join(root_path, 'setup', 'setup.py')
BIOS_location = os.path.join(root_path, 'BIOS')
apps_dir = os.path.join(root_path, 'apps')
bios_log_location = os.path.join(root_path, 'bios_log.txt')
path_location = os.path.join(root_path, 'path.txt')
skypkg_path = os.path.join(root_path, "skypkg", "skypkg.py")

# write all the programs launchers or 1fileapps to the path file
open(path_location, 'w').close()  # Clear the file first
for app in os.listdir(apps_dir):
    with open(path_location, 'a') as path_file:
        # now avoids writing folders for multi file apps, and writes only 1fileapps and launchers.
        path_file.write(f"{os.path.join(apps_dir, app)}\n")

def run_setup():
    if os.path.isfile(setup_script_path):
        try:
            subprocess.run([sys.executable, setup_script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the setup script: {e}")
            os._exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            os._exit(0)
    else:
        panic("COULD_NOT_FIND_SETUP")
        os._exit(0)

def welcome():
    with open(signed_in_file, "w") as session_file:
        session_file.write("1")  # Mark signed in
    if current_hour < 12:
        print(f"Good morning, {stored_username} welcome back.")
    else:
        print(f"Good afternoon, {stored_username} welcome back.")

    print("Welcome back to SkyOS Aurora! Thank you to all those contributors who worked on this!")
    print(f"SkyOS Aurora {valid_version} written in Python 3.13.7")
    print("ALWAYS USE EXIT COMMAND TO EXIT THE OS, DO NOT CLOSE THE WINDOW!")
    print("For more info on the project type: info, help (commands) or copyright.")
    today = datetime.today()
    if today.month == 10 and today.day == 31:
        print("HAPPY HALLOWEEN 🎃")
    if today.month == 12 and today.day == 25:
        print("MERRY CHRISTMAS 🎅")
    if today.month == 4 and today.day == 1:
        print("APRIL FOOLS 😏")

# Check if required files exist, if not run setup
if not os.path.isfile(username_file) or not os.path.isfile(password_file) or not os.path.isfile(signed_in_file):
    print("An important file is missing. Running setup...")
    run_setup()

# Load stored username and password
with open(username_file, "r") as user_file:
    stored_username = user_file.read().strip()

with open(password_file, "r") as password_file_obj:
    stored_password = password_file_obj.read().strip()

authenticated = False

# Check sign-in status
with open(signed_in_file, "r") as session_file:
    signed_in_status = session_file.read().strip()

if signed_in_status == "0":
    print_boot_screen()
    while not authenticated:
        password = input(f"Enter your password, {stored_username}: ").strip()
        # Hash the input password for comparison
        hashed_input_password = hashlib.sha256(password.encode()).hexdigest()
        # Compare the hashed input password with the stored hashed password
        if hashed_input_password == stored_password:
            authenticated = True
            welcome()
        else:
            print("Incorrect password. try again")
else:
    authenticated = True  # already signed in

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
        print("app - run an application. you can also run an app by using the app's name. e.g. 'texteditor'")
        print("tree - create a value for tree. use the -p parameter to print the value.")
        print("history - show all command history")
        print("shutdown - shut down the system")
        print("reboot - reboot the system")
        print("bios - run the bios")
        print("time - show the current time")
        print("setup - run the setup script to reset your username and password")
        print("bios log - print out the bios log")
        print("afk - hold the os in a safe environment while you are 'afk'")
        print("exit - exit the OS (do not close the window! use this command instead!)")
        print("clear - clear the screen")
        print("cls - clear the screen (alias for clear)")
        print("version - show the current SkyOS version")
        print("uname - show system information")
        print("uname -a - show all system information")
        print("uname -h - show all parameters for uname plus more help")
        print("license - show the license information for SkyOS")

    # command to run an app
    elif command in [(name := os.path.splitext(os.path.basename(p))[0]) for p in open(path_location).read().splitlines()]:
        script_path = next(p for p in open(path_location).read().splitlines() if os.path.splitext(os.path.basename(p))[0] == command)
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    elif command == "update":
        response = requests.get('https://alter-net-codes.github.io/skyosweb/aurora/archive/version.txt')
        latest_version = response.text.strip()
        filepath = os.path.join(root_path)
        if latest_version != valid_version:
            print(f"A new version of SkyOS Aurora is available: {latest_version}")
            update_choice = input("Do you want to update? (yes/no): ").strip().lower()
            if update_choice == "yes":
                print("Updating SkyOS Aurora...")
                # Download the latest version
                listurlget = requests.get(f'https://alter-net-codes.github.io/skyosweb/aurora/archive/{latest_version}/files.txt')
                file_urls = listurlget.text.strip().splitlines()
                listfilepath = requests.get(f'https://alter-net-codes.github.io/skyosweb/aurora/archive/{latest_version}/filepath.txt')
                filepathsdownload = listfilepath.text.strip().splitlines()
                currentfilenum = -1
                for file_url in file_urls:
                    currentfilenum += 1
                    file_url = file_url.strip()
                    filename = file_url.split('/')[-1]
                    filepath = filepathsdownload[currentfilenum]
                    filepath = os.path.join(f'{root_path}/{filepath}/', filename)
                    urllib.request.urlretrieve(file_url, filepath)
                with open(signed_in_file, "w") as session_file:
                    session_file.write("0")
                    print("Exiting the OS...")
                    print("Please restart manually to finish the update.")
                    time.sleep(2)
                    sys.exit()
        else:
            print("You are up to date!")

    elif command == "time":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current time: {current_time}")

    elif command == "afk":
        os.system('cls' if platform.system() == "Windows" else 'clear')
        input("in afk mode... press enter to cancel ")

    elif command == "exit":
        os_option = input("Are you sure? Type 'yes' to confirm: ")
        if os_option == "yes":
            with open(signed_in_file, "w") as session_file:
                session_file.write("0")
            print("Exiting the OS...")
            time.sleep(2)
            os._exit(0)

    elif command == "bios log":
        try:
            with open(bios_log_location, 'r') as file:
                file_content = file.read()
                print("File Content:\n", file_content)
        except FileNotFoundError:
            print(f"File '{bios_log_location}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif command == "info":
        print("Developed by Alter Net codes. All rights reserved.")
        print("This kernel may be reproduced if it meets the licenses terms. More info in the copyright command.")
        print(f"Current SkyOS Aurora version: {valid_version}")

    elif command == "copyright":
        print("Copyright © 2024-2025 Alter Net codes")
        print("if you are adding on to this software, or want to hold a copy of this software,")
        print("then you can get info on copyright in the 'license' file in the root directory.")

    elif command == "echo":
        print()

    elif "echo" in command:
        echo_text = command.replace("echo ", "").strip()
        if echo_text:
            print(echo_text)

    elif command == "tree":
        treevalue = input("tree: ")
        print("The value of tree is set.")

    elif command == "tree -p":
        print(treevalue)

    elif command == "app":
        script_path = os.path.join(apps_dir, input("Enter the app name: ").strip())
        script_path = script_path + ".py"  # PYTHON
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
            with open(signed_in_file, "w") as session_file:
                session_file.write("0")
            print("Shutting down the system...")
            time.sleep(2)
            if platform.system() == "Darwin":
                os.system("shutdown -h now")
            elif platform.system() == "Linux":
                os.system("shutdown -h now")
            elif platform.system() == "Windows":
                os.system("shutdown /s")
        else:
            print("Shutdown cancelled.")

    elif command == "reboot":
        os_option = input("Are you sure? Type 'yes' to confirm: ")
        if os_option == "yes":
            with open(signed_in_file, "w") as session_file:
                session_file.write("0")
            print("Rebooting the system...")
            time.sleep(2)
            if platform.system() == "Darwin":
                os.system("shutdown -r now")
            elif platform.system() == "Linux":
                os.system("shutdown -r now")
            elif platform.system() == "Windows":
                os.system("shutdown /r")
        else:
            print("Reboot cancelled.")

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

    elif command == "clear":
        os.system('cls' if platform.system() == "Windows" else 'clear')
        print("Screen cleared.")
    
    elif command == "cls":
        os.system('cls' if platform.system() == "Windows" else 'clear')
        print("Screen cleared.")

    elif command == "version":
        print(f"SkyOS Aurora version: {valid_version}")
    
    elif command == "uname":
        print(f"SkyOS Aurora version: {valid_version}")
        print(f"Username: {username}")
        print(f"Platform: {platform.system()} {platform.release()}")

    elif command == "uname -a":
        print(f"SkyOS Aurora version: {valid_version}")
        print(f"Username: {username}")
        print(f"Platform: {platform.system()} {platform.release()}")
        print(f"Machine: {platform.machine()}")
        print(f"Processor: {platform.processor()}")
        print(f"Python version: {platform.python_version()}")

    elif command == "uname -v":
        print(f"SkyOS Aurora version: {valid_version}")
        print(f"Python version: {platform.python_version()}")

    elif command == "uname -m":
        print(f"Machine: {platform.machine()}")

    elif command == "uname -p":
        print(f"Processor: {platform.processor()}")

    elif command == "uname -o":
        print(f"Operating System: {platform.system()} {platform.release()}")
        
    elif command == "uname -r":
        print(f"Release: {platform.release()}")

    elif command == "uname -s":
        print(f"System: {platform.system()}")

    elif command == "uname -n":
        print(f"Node Name: {platform.node()}")

    elif command == "uname -i":
        print(f"Platform: {platform.platform()}")

    elif command == "uname -l":
        print(f"Platform: {platform.platform()}")

    elif command == "uname -c":
        print(f"Platform: {platform.platform()}")

    elif command == "uname -h":
        print("Usage: uname [OPTION]...\n"
              "Print system information.\n\n"
              "Options:\n"
              "  -a, --all          print all information\n"
              "  -s, --kernel-name  print the kernel name\n"
              "  -n, --nodename     print the network node hostname\n"
              "  -r, --kernel-release print the kernel release\n"
              "  -v, --kernel-version print the kernel version\n"
              "  -m, --machine      print the machine hardware name\n"
              "  -p, --processor    print the processor type\n"
              "  -i, --hardware-platform print the hardware platform\n"
              "  -o, --operating-system print the operating system\n"
              "  -h, --help         display this help and exit")
    
    elif command == "license":
        print("SkyOS is licensed under the BSD 3-Clause license.\n"
              "You are free to use, modify, and distribute this software as long as you include the original license text.\n"
              "For more details, please refer to the LICENSE file in the root dire ctory.")

    elif command == "":
        pass

    elif command.startswith("skypkg"):
        # Build the command by appending user input after 'skypkg'
        full_command = f'py "{skypkg_path}" {command[len("skypkg "):]}'
        # Run SkyPKG as a subprocess and print its output live
        subprocess.run(full_command, shell=True)

    else:
        print(f"{RED}{command} is not a valid command or executable. Type 'help' for a list of commands.{RESET}")

panic("NON-NORMAL SHUTDOWN! EMERGENCY!")  # in case the loop somehow breaks
