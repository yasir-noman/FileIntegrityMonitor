# Argus File Integrity Monitor (FIM)

A real-time File Integrity Monitoring tool built in Python. It monitors a selected folder and sends Windows Desktop Notifications instantly if any file is created, modified, deleted, or renamed.

Features:
- Real-Time Monitoring: Uses watchdog to track file system events instantly.
- Desktop Notifications: Uses winotify to send Windows Toast Notifications.
- Terminal Logs: Displays color-coded alerts in the terminal (Green for created, Red for deleted, Yellow for modified).
- GUI Folder Selector: Easy-to-use pop-up window to select the target folder.

Technologies Used:
- Python 3
- watchdog (For real-time file monitoring)
- winotify (For Windows notifications)
- tkinter (For folder selection GUI)

How to Install and Run:
1. Open terminal in the project folder.
2. Install dependencies: pip install -r requirements.txt
3. Run the script: python monitor.py
4. A pop-up window will appear. Select the folder you want to monitor.
5. Try creating or deleting a file in that folder to see the notification.

Note:
The winotify library is specifically designed for Windows OS.

Developed by YASIR ARAFAT NOMAN