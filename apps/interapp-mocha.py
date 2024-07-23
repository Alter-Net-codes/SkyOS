# InterApp Mocha
# A better version of InterApp that runs JARs. In Scratch OSes, it needs TurboWarp to work, and it needs Java installed

import subprocess
import os
import sys

def main():
    print("InterApp Mocha v1.0")
    print("Note that you WILL need Oracle Java installed to use this.")

    jar = input("Enter the file name of the JAR> ")

    print("Launching JAR...")
    
    try:
      subprocess.run(["java"], ["-jar"], [jar], check=True)
    except subprocess.CalledProcessError as error:
      print(f"Error launching JAR: {error}")
    except Exception as error:
      print(f"An unexpected error occured: {error}")

    print("The JAR should hopefully be launched. If you don't see a 'java' process on your host machine, things may be busted, or you may need to install Java. Either one.")
    print("What do I know? I'm just a disembodied voice in a Python OS simulation made by users of a coding website meant for teaching kids how to code.")
    
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

if __name__ == "__main__":
    main()
