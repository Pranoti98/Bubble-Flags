#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#****

#imported required packages
import csv
import os
import tkinter as tk
from datetime import datetime
from tkinter import Frame, Button, Label, Entry, Tk, messagebox
from pathlib import Path

class App(Tk):

    def __init__(self):
        super().__init__()

        self.title("Bubbles")

        frame = Frame(self)
        frame.pack(padx=20, pady=20)

        # Start Time
        start_time_label = Label(frame, text="Start Time (seconds):")
        start_time_label.grid(row=0, column=0, padx=10, pady=10)

        self.start_time_entry = Entry(frame, width=20)
        self.start_time_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button
        bubble_button = Button(frame, text="BUBBLE", command=self.generate_csv)
        bubble_button.grid(row=1, column=0, columnspan=2, pady=10)

    def generate_csv(self):
        start_time_str = self.start_time_entry.get()

        try:
            start_time_seconds = int(start_time_str)
        except ValueError:
            messagebox.showerror("Invalid ", "Please enter a valid number")
            return

        current_time_seconds = int(datetime.utcnow().timestamp())
        offset = 2082844800
        adjusted_time_seconds = current_time_seconds - offset - start_time_seconds

        file_path = os.path.join(Path.home(), "Bubbles.csv")
        file_exists = os.path.isfile(file_path)

        csv_data = [
            ["Time (seconds)", "Concentration"],
            [adjusted_time_seconds, "Bubble"]
        ]

        try:
            with open(file_path, 'a', newline='') as csvfile:  # Use 'a' to append to existing file
                writer = csv.writer(csvfile)
                if not file_exists or os.stat(file_path).st_size == 0:  # Check if file is new or empty
                    writer.writerow(csv_data[0])  # Write headers
                writer.writerow(csv_data[1])  # Write the data row
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write CSV file: {str(e)}")
            return

        messagebox.showinfo("CSV Generated", f"Data appended to CSV file:\n{file_path}")

        # Opening CSV file after append
        if os.name == 'nt':
            os.startfile(file_path)
        else:
            os.system('open %s' % file_path)


if __name__ == '__main__':
    app = App()
    app.mainloop()

