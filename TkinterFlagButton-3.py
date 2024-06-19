#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, font
from datetime import datetime

class BubblesApp(Tk):
    def __init__(self):
        super().__init__()

        self.title("BUBBLES")
        #set starting window size
        self.geometry("400x200")  

        # Configure fonts
        label_font = font.Font(family="Helvetica", size=12, weight="bold")
        entry_font = font.Font(family="Helvetica", size=12)
        button_font = font.Font(family="Helvetica", size=12, weight="bold")
        
        #frame sizes
        frame = Frame(self)
        frame.pack(padx=20, pady=20)

        # Start Time
        start_time_label = Label(frame, text="Start Time (seconds):", font=label_font)
        start_time_label.grid(row=0, column=0, padx=10, pady=10)

        self.start_time_entry = Entry(frame, width=20, font=entry_font)
        self.start_time_entry.grid(row=0, column=1, padx=10, pady=10)

        # Flag Name
        flag_name_label = Label(frame, text="Flag Name:", font=label_font)
        flag_name_label.grid(row=1, column=0, padx=10, pady=10)

        self.flag_name_entry = Entry(frame, width=20, font=entry_font)
        self.flag_name_entry.insert(0, "BUBBLE")  # Default value
        self.flag_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button
        flag_button = Button(frame, text="FLAG", command=self.generate_csv, font=button_font)
        flag_button.grid(row=2, column=0, columnspan=2, pady=20)

        # Light gray colour for background
        frame.configure(bg="#f0f0f0") 
        # Slightly darker gray colour background
        self.configure(bg="#e0e0e0")   

    def generate_csv(self):
        start_time_str = self.start_time_entry.get()

        try:
            start_time_seconds = int(start_time_str)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
            return
        
        #fixed offset number
        epoch_offset = 2082844800
        start_time = datetime.fromtimestamp(start_time_seconds - epoch_offset)
        now = datetime.utcnow()
        current_time_seconds = (now - start_time).seconds

        flag_name = self.flag_name_entry.get()
        
        #saving file on desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "Bubbles.csv")

        file_exists = os.path.isfile(file_path)
        
        #csv data
        csv_data = [
            ["Time (seconds)", "Concentration"],
            [current_time_seconds, flag_name]
        ]

        try:
            #appending 
            with open(file_path, 'a', newline='') as csvfile:  
                writer = csv.writer(csvfile)
                if not file_exists or os.stat(file_path).st_size == 0:  
                    #header
                    writer.writerow(csv_data[0]) 
                    #row
                writer.writerow(csv_data[1])  
        #messagebox
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write CSV file: {str(e)}")
            return
        
        messagebox.showinfo("CSV Generated", f"Data appended to CSV file:\n{file_path}")

if __name__ == "__main__":
    app = BubblesApp()
    app.mainloop()


# In[ ]:




