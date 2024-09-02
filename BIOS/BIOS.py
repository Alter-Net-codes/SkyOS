import os
import subprocess
import sys
 
kernelState = None

print("SkyOS v2.6 bugfix + app update")
print("This device is running SkyOS")
print("/kernel/bios")
print(" ^ BIOS is running here")

def main():
    while True:
        answer = input("exit? (yes/no): ").strip().lower()
        if answer == "no":
            print("SkyOS v2.7 fully bugfixed update")
            print("This device is running SkyOS")
            print("/main/bios/")
            print(" ^ BIOS is running here")
        elif answer == "yes":
            # Path to the kernel script in the KERNEL folder
            kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
            
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
                print("sucsess!!!!!")
                kernelState = "gone"
            break  # Exit the loop after trying to run the kernel script
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
if kernelState == "gone":
 print("The skyOS kernel is missing. Please reinstall skyOS or replace the kernel script,")

if __name__ == "__main__":
    main()
