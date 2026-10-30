import os
import time
import threading
import tkinter as tk
from tkinter import filedialog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from winotify import Notification, audio

# ==========================================
# নোটিফিকেশন পাঠানোর ফাংশন
# ==========================================
def send_notification(title, message):
    # winotify লাইব্রেরি ব্যবহার করে উইন্ডোজ নোটিফিকেশন
    toast = Notification(
        app_id="Arguslens FIM",
        title=title,
        msg=message,
        duration="short" # কতক্ষণ থাকবে
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()

# ==========================================
# ফাইল চেঞ্জ ডিটেক্ট করার ক্লাস
# ==========================================
class FileMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            print(f"\033[93m[⚠️ MODIFIED]\033[0m {filename}")
            send_notification("File Modified!", f"Changes detected in: {filename}")

    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            print(f"\033[92m[✅ CREATED]\033[0m {filename}")
            send_notification("File Created!", f"New file added: {filename}")

    def on_deleted(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            print(f"\033[91m[❌ DELETED]\033[0m {filename}")
            send_notification("File Deleted!", f"File removed: {filename}")

    def on_moved(self, event):
        if not event.is_directory:
            old_name = os.path.basename(event.src_path)
            new_name = os.path.basename(event.dest_path)
            print(f"\033[96m[🔄 RENAMED]\033[0m {old_name} -> {new_name}")
            send_notification("File Renamed/Moved!", f"{old_name} -> {new_name}")

# ==========================================
# মেইন ফাংশন (ফোল্ডার সিলেক্ট এবং মনিটরিং)
# ==========================================
def main():
    print("\033[96m" + "="*50)
    print("      ARGUSLENS - FILE INTEGRITY MONITOR")
    print("="*50 + "\033[0m")
    
    # GUI পপ-আপ ওপেন করা (ফোল্ডার সিলেক্ট করার জন্য)
    root = tk.Tk()
    root.withdraw() # মেইন উইন্ডো হাইড করে রাখা
    print("[*] Please select a folder to monitor...")
    
    # ফোল্ডার সিলেক্ট ডায়ালগ
    folder_path = filedialog.askdirectory(title="Select Folder to Monitor")
    
    if not folder_path:
        print("\033[91m[-] No folder selected. Exiting...\033[0m")
        return

    print(f"\033[92m[+] Monitoring Started: {folder_path}\033[0m")
    print("[*] Press Ctrl+C to stop monitoring.\n")
    
    # ওয়াচডগ সেটআপ
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n\033[91m[-] Monitoring stopped.\033[0m")
    
    observer.join()

if __name__ == "__main__":
    main()