import subprocess
import os
import sys

def main():
    print("Hello, World!")
    print("Make an app in the app folder (with the same structure just modified to fit your app code).")
    
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
        print("Kernel script not found. Make sure 'kernel.py' exists in the 'KERNEL' directory.")

if __name__ == "__main__":
    main()
