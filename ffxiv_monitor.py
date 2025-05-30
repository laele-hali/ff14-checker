import socket
import time
from datetime import datetime

# List of game server IPs to monitor
ips = [f"204.2.29.{i}" for i in range(70, 81)]

# FF14 relevant TCP ports
ports = [54992, 54993, 54994, 55006, 55007]

# Time between checks (seconds)
interval = 60

def is_port_open(ip, port, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def check_servers():
    print(f"[{datetime.now()}] Checking FF14 game servers...")
    for ip in ips:
        for port in ports:
            if is_port_open(ip, port):
                print(f"✅ {ip}:{port} is OPEN")
            else:
                print(f"❌ {ip}:{port} is CLOSED")

if __name__ == "__main__":
    while True:
        check_servers()
        print("-" * 40)
        time.sleep(interval)
