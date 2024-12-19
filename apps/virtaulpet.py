import subprocess
import os
import sys
import random

def main():
    status = "happy"
    hunger = 0
    tired = 0

    print("Welcome to the virtual pet game!")
    print("Keep your pet happy by feeding it...")
    print("Play with it...")
    print("Make it rest...")
    print("And buy it toys")
    print("Enjoy this simple command line game by Alter Net codes!")
    input("Press Enter to continue...")
    for i in range(20):
        print(" ")

    while True:
        print("Looks like your dog is", status)
        print("You can FEED, PLAY, REST, BUY TOYS, EXIT")
        if tired > 4:
            print("Your dog is tired.")
        if hunger > 4:
            print("Your dog is hungry.")
    
        task = input("What would you like to do? ").lower()

        if task == "play":
            hunger += 2
            tired += 2
            print("You go to the park to play with your dog!")
            status = "excited"
            print("Your dog is", status, "to be at the park")
            number = random.randint(1, 100)
            try:
                numberpicked = int(input("Pick a number from 1-100: "))
                if numberpicked < number:
                    print("Oh, not quite! The right number was:", number)
                    print("You throw the ball about 20 feet!")
                    print("Nice throw!")
                    print(" ")
                    status = "satisfied"
                elif numberpicked > number:
                    print("Not quite! Still good! The right number was:", number)
                    print("Nice! You throw the ball about 20 feet")
                    print("Nice throw!")
                    print(" ")
                    status = "satisfied"
                else:
                    print("YES! YOU GOT IT!!!")
                    print("You throw the ball 50 feet!")
                    print("ELEGANT!!!!!!!!")
                    print("")
                    status = "VERY happy"
            except ValueError:
                print("Please enter a valid number.")
            
        elif task == "feed":
            tired += 2
            print("Good idea to feed him; he was at", hunger, "hunger points!")
            print("You feed your dog.")
            hunger = 0
            status = "happy"
            print("Your dog is now cured of its hunger.")
            print(" ")

        elif task == "rest":
            hunger += 2
            print("Good idea; your dog was at", tired, "tired points!")
            print("You put your dog to sleep.")
            tired = 0
            status = "happy"
            print("Your dog is now cured of its tiredness.")
            print(" ")

        elif task == "buy toys":
            tired += 2
            print("You buy a few toys for your dog.")
            status = "playful"
            print(" ")

        elif task == "exit":
            print("Goodbye!")
            print("See you later.")
            print("Saving and quitting...")

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
                print("Kernel Script Not found or has a defect. Please reinstall SkyOS or replace the kernel file.")

            break

        else:
            print("That is not a valid action!")

if __name__ == "__main__":
    main()
