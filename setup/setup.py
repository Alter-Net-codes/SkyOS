# Path to the kernel script in the KERNEL folder
kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')

# setup.py

# Prompt the user for their username
username = input("Enter your username: ")

# Prompt the user for their password
password = input("Enter your password: ")

# Create a file named 'username.txt' and write the username in it
with open("username.txt", "w") as user_file:
    user_file.write(username)

# Create a file named 'password.txt' and write the password in it
with open("password.txt", "w") as password_file:
    password_file.write(password)

print("setup finished! thank you for using SkyOS!")
print("going to the kernel file...")
    
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