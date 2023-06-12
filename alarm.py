from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())

    alarm_time = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
    current_time = datetime.now()

    if alarm_time <= current_time:
        alarm_time = alarm_time.replace(day=alarm_time.day + 1)

    time_difference = alarm_time - current_time
    seconds_difference = time_difference.total_seconds()

    root.after(int(seconds_difference * 1000), ring_alarm)

    message = f"Alarm set for {hour:02d}:{minute:02d}"
    messagebox.showinfo("Alarm Clock", message)

def ring_alarm():
    messagebox.showinfo("Alarm Clock", "Wake up!")

root = tk.Tk()
root.title("Alarm Clock by - SURAJ MAPARI")

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size and position
window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

hour_label = tk.Label(root, text="Hour (24-hour format):", font=("Arial", 16))
hour_label.pack(pady=10)

hour_entry = tk.Entry(root, font=("Arial", 16))
hour_entry.pack()

minute_label = tk.Label(root, text="Minute:", font=("Arial", 16))
minute_label.pack(pady=10)

minute_entry = tk.Entry(root, font=("Arial", 16))
minute_entry.pack()

set_button = tk.Button(root, text="Set Alarm", font=("Arial", 16), command=set_alarm)
set_button.pack(pady=20)

root.mainloop()
