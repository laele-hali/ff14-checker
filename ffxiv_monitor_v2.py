import socket
import time
from datetime import datetime
import requests

# === Configuration ===
server_ip = "204.2.29.75"         # Replace with Halicarnassus IP
server_port = 54992               # Replace with confirmed port
check_interval = 60               # How often to check (seconds)
discord_webhook = "https://discord.com/api/webhooks/..."  # REPLACE with your webhook

# === Discord Notification Function ===
def send_discord_notification(message):
    data = {"content": message}
    try:
        response = requests.post(discord_webhook, json=data)
        if response.status_code != 204:
            print(f"Discord webhook failed: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Error sending Discord notification: {e}")

# === Port Check ===
def is_port_open(ip, port, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

# === Main Monitoring Loop ===
def monitor():
    last_status = None
    print(f"Monitoring Halicarnassus @ {server_ip}:{server_port} every {check_interval} seconds...")
    while True:
        status = is_port_open(server_ip, server_port)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status_str = "✅ ONLINE" if status else "❌ OFFLINE"
        print(f"[{now}] {status_str} - {server_ip}:{server_port}")

        # Notify only if status has changed
        if status != last_status:
            msg = f"**Halicarnassus** status changed: {status_str}\n({server_ip}:{server_port})"
            send_discord_notification(msg)
            last_status = status

        time.sleep(check_interval)

# === Run ===
if __name__ == "__main__":
    monitor()
