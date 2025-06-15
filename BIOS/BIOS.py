import os
import subprocess
import sys
import logging
import platform
import shutil
from datetime import datetime

try:
    import colorama
    colorama.init()
except ImportError:
    pass  # optional color support

kernelState = None

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

# Absolute path for log file to keep logs neat and in place
bios_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(bios_dir, '..')
log_path = os.path.join(root_dir, 'bios_log.txt')

logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_and_print(message, color=None):
    if color:
        print(color + message + Colors.RESET)
    else:
        print(message)
    logging.info(message)

def display_system_info():
    log_and_print(f"--- SkyOS BIOS v2.7 Boot ---", Colors.CYAN)
    log_and_print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", Colors.YELLOW)

    os_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
    log_and_print(f"OS: {os_info}", Colors.GREEN)

    # Set root dir depending on platform
    root_dir = "C:\\" if platform.system() == "Windows" else "/"
    total, used, free = shutil.disk_usage(root_dir)
    log_and_print(f"Disk: Total {total // (2**30)} GB, Used {used // (2**30)} GB, Free {free // (2**30)} GB", Colors.GREEN)

    cpu = platform.processor()
    if cpu:
        log_and_print(f"CPU: {cpu}", Colors.GREEN)

def ask_leave_bios():
    while True:
        choice = input("Leave the BIOS? [Y/N]: ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            log_and_print("Invalid input. Please enter 'Y' or 'N'.", Colors.RED)

def bios_app():
    global kernelState
    display_system_info()

    while True:
        answer = input("Type 'info' to see system info or 'leave' to exit BIOS: ").strip().lower()

        if answer == "info":
            display_system_info()

        elif answer == "leave":
            if ask_leave_bios():
                log_and_print("Leaving BIOS and returning to kernel...", Colors.CYAN)

                # Use absolute path based on this file's dir, to be safe
                kernel_script = os.path.join(bios_dir, '..', 'kernel', 'kernel.py')
                kernel_script = os.path.normpath(kernel_script)  # clean path

                if os.path.isfile(kernel_script):
                    try:
                        subprocess.run([sys.executable, kernel_script], check=True)
                    except subprocess.CalledProcessError as e:
                        log_and_print(f"Error running kernel script: {e}", Colors.RED)
                    except Exception as e:
                        log_and_print(f"Unexpected error: {e}", Colors.RED)
                else:
                    log_and_print("Kernel script missing! Please reinstall SkyOS.", Colors.RED)
                    kernelState = "gone"
                break
            else:
                log_and_print("Stayed in BIOS.", Colors.YELLOW)

        else:
            log_and_print("Invalid command. Use 'info' or 'leave'.", Colors.RED)

    if kernelState == "gone":
        log_and_print("SkyOS kernel missing or corrupted. Reinstallation needed.", Colors.RED)

if __name__ == "__main__":
    bios_app()
