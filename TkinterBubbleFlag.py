#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#formulas from tkinter.ipynb file

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

        # Start Time label and the grid 
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

        now = datetime.now()
        #fixed offset value
        epoch_offset = 2082844800

        try:
            start_time = datetime.fromtimestamp(start_time_seconds - epoch_offset)
            current_time = (now - start_time).seconds
        except Exception as e:
            messagebox.showerror("Error", f"Error in time calculation: {str(e)}")
            return

        file_path = os.path.join(Path.home(), "Bubbles.csv")
        file_exists = os.path.isfile(file_path)

        csv_data = [
            ["Time (seconds)", "Concentration"],
            [current_time, "Bubble"]
        ]

        try:
            with open(file_path, 'a', newline='') as csvfile:  
                writer = csv.writer(csvfile)
                # Checking if file is exit or need to create one
                if not file_exists or os.stat(file_path).st_size == 0: 
                    #header
                    writer.writerow(csv_data[0])  
                    #row
                writer.writerow(csv_data[1])  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write CSV file: {str(e)}")
            return
        
        #box of message after creating file with its path
        messagebox.showinfo("CSV Generated", f"Data appended to CSV file:\n{file_path}")

        # Opening CSV file 
        if os.name == 'nt':
            os.startfile(file_path)
        else:
            os.system('open %s' % file_path)


if __name__ == '__main__':
    app = App()
    app.mainloop()

