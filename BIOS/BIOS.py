import os
import subprocess
import sys
import logging
import platform
import shutil
from datetime import datetime

kernelState = None

logging.basicConfig(filename='bios_log.txt', level=logging.INFO)


def log_and_print(message):
    logging.info(message)
    print(message)


def display_system_info():
    log_and_print(f"System Info - Date/Time: {datetime.now()}")
    log_and_print(f"System Info - OS: {platform.system()} {platform.release()}")
    total, used, free = shutil.disk_usage("/")
    log_and_print(f"System Info - Disk space: {free // (2 ** 30)} GB free")


def main():
    global kernelState
    display_system_info()

    while True:
        answer = input("exit? (yes/no): ").strip().lower()
        if answer == "no":
            log_and_print("SkyOS v2.7")
            log_and_print("This device is running SkyOS")
            log_and_print("/bios/bios.py/")
            log_and_print(" ^ BIOS is running here")
        elif answer == "yes":
            kernel_script = os.path.join(os.getcwd(), 'kernel', 'kernel.py')

            if os.path.isfile(kernel_script):
                try:
                    subprocess.run([sys.executable, kernel_script], check=True)
                except subprocess.CalledProcessError as e:
                    log_and_print(f"Error executing the kernel script: {e}")
                except Exception as e:
                    log_and_print(f"An unexpected error occurred: {e}")
            else:
                log_and_print("Success!")
                kernelState = "gone"
            break
        else:
            log_and_print("Invalid input. Please type 'yes' or 'no'.")

    if kernelState == "gone":
        log_and_print("The SkyOS kernel is missing or has a defect. Please reinstall SkyOS or replace the kernel script.")


if __name__ == "__main__":
    main()
