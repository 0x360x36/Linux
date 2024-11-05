import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running command {command}: {e}")
        return ""

def check_processes():
    processes = run_command("ps aux")
    print("Running Processes:")
    print(processes)

def check_network_connections():
    connections = run_command("ss -tulnp")
    print("Network Connections:")
    print(connections)

if __name__ == "__main__":
    check_processes()
    check_network_connections()
