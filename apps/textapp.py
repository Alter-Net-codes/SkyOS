import os
import subprocess
import sys

def exit_app():
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
        print("yay! sucsess!")

def create_file(filename):
    with open(filename, 'w') as file:
        print("Enter content for the file (end with an empty line):")
        while True:
            line = input()
            if line == "":
                break
            file.write(line + "\n")
    print(f"File '{filename}' created successfully.")

def read_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':")
            print(file.read())
    else:
        print(f"File '{filename}' does not exist.")

def edit_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'a') as file:
            print("Enter content to append to the file (end with an empty line):")
            while True:
                line = input()
                if line == "":
                    break
                file.write(line + "\n")
        print(f"File '{filename}' updated successfully.")
    else:
        print(f"File '{filename}' does not exist.")

def main():
    print("Welcome to TextApp!")
    while True:
        command = input("Enter command (create, read, edit, exit): ").strip().lower()
        if command == "create":
            filename = input("Enter filename to create: ").strip()
            create_file(filename)
        elif command == "read":
            filename = input("Enter filename to read: ").strip()
            read_file(filename)
        elif command == "edit":
            filename = input("Enter filename to edit: ").strip()
            edit_file(filename)
        elif command == "exit":
            print("Exiting TextApp. Goodbye!")
            exit_app()
            break  # Add this line to actually exit the loop
        else:
            print("Invalid command. Please enter 'create', 'read', 'edit', or 'exit'.")

if __name__ == "__main__":
    main()
