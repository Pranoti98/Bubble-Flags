#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import csv
import sys
from tkinter import Tk, Frame, Label, Entry, Button, messagebox
from datetime import datetime

class BubblesApp(Tk):
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
            messagebox.showerror("Invalid Input", "Please enter a valid number")
            return

        epoch_offset = 2082844800
        start_time = datetime.fromtimestamp(start_time_seconds - epoch_offset)
        now = datetime.utcnow()
        current_time_seconds = (now - start_time).seconds

        file_path = os.path.join(os.path.expanduser("~"), "Bubbles.csv")
        file_exists = os.path.isfile(file_path)

        csv_data = [
            ["Time (seconds)", "Concentration"],
            [current_time_seconds, "Bubble"]
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

       

if __name__ == "__main__":
    app = BubblesApp()
    app.mainloop()


# In[ ]:




