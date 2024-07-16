import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from data_manager import DataManager

class CalorieTrackerApp:
    def __init__(self):
        self.root = tk.Tk()  # Creates main window
        self.root.title("Calorie Tracker")
        self.root.geometry("500x400")
        self.root.configure(bg='#596e79')
        
        style = ttk.Style()
        style.theme_use('clam')  # Choose a theme for ttk widgets
        style.configure('TFrame', background='#596e79')  # Configure style for TFrame
        
        self.data_manager = DataManager("calories.csv")  # Initialize DataManager with the file name

        self.setup_ui()  # Calling method to set up user interface

    def setup_ui(self):
        # Creating a frame for the input fields to move where they are located in window
        input_frame = tk.Frame(self.root, bg='#596e79')
        input_frame.pack(pady=20)

        # Creating and placing label and entry for the meal user input
        tk.Label(input_frame, text="Meal:", font=("Verdana", 14), fg='#f0ece2', bg='#596e79').grid(row=0, column=0, padx=10)
        self.meal_entry = tk.Entry(input_frame)
        self.meal_entry.grid(row=0, column=1, padx=10)

        # Creating and placing label and entry for the calories user input
        tk.Label(input_frame, text="Calories:", font=("Verdana", 14), fg='#f0ece2', bg='#596e79').grid(row=1, column=0, padx=10)
        self.calories_entry = tk.Entry(input_frame)
        self.calories_entry.grid(row=1, column=1, padx=10)

        button_frame = ttk.Frame(self.root, style='TFrame')
        button_frame.pack(side=tk.BOTTOM, pady=20)

        # Button to add new meal
        add_button = ttk.Button(button_frame, text="Add Meal", command=self.new_meal)
        add_button.grid(row=0, column=0, padx=10)

        # Button to view meal history
        view_button = ttk.Button(button_frame, text="View History", command=self.view_records)
        view_button.grid(row=0, column=1, padx=10)

        # Window closing protocol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def new_meal(self):
        meal = self.meal_entry.get().strip()
        calories = self.calories_entry.get().strip()
        
        if meal and calories:  # Check if both input fields are filled
            try:
                calories = int(calories)
                self.data_manager.add_meal(meal, calories)  # Adding meals and calories to the data manager
                
                # Clearing input fields
                self.meal_entry.delete(0, tk.END)
                self.calories_entry.delete(0, tk.END)
                
                messagebox.showinfo("Successful Update", "Meal added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for calories.")
        else:
            messagebox.showerror("Error", "Make sure all fields are filled in.")

    def view_records(self):
        records = self.data_manager.get_records()  # Obtains meal records
        if records is not None:
            records_window = tk.Toplevel(self.root)  # Creates a new window to display meal records
            records_window.title("View Meals")
            
            records_text = tk.Text(records_window, wrap=tk.WORD)  # Creates a text widget to display records
            records_text.insert(tk.INSERT, records.to_string(index=False))  # Insert records into the text widget
            records_text.pack()  # Packing the text widget
        else:
            messagebox.showerror("Error", "No records found.")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()
