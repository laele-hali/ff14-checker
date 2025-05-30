# ff14-checker
discord integration for checking server status for ff14




nano /etc/systemd/system/halicarnassus-monitor.service

[Unit]
Description=ffxiv_monitor_v2
After=network.target

[Service]
ExecStart=/usr/bin/python3 /root/ffxiv_monitor_v2.py
WorkingDirectory=/root
Restart=always
User=root

[Install]
WantedBy=multi-user.target






sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable --now ffxiv_monitor_v2
