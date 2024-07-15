from tkinter import *
from tkinter import messagebox
import pandas as pd
from data_manager import DataManager

class CalorieTrackerApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calorie Tracker")
        self.data_manager = DataManager("calories.csv")

        self.setup_ui()

    def setup_ui(self):
        Label(self.root, text="Meal:").grid(row=0, column=0)
        self.meal_entry = Entry(self.root)
        self.meal_entry.grid(row=0, column=1)

        Label(self.root, text="Calories:").grid(row=1, column=0)
        self.calories_entry = Entry(self.root)
        self.calories_entry.grid(row=1, column=1)

        add_button = Button(self.root, text="Add Meal", command=self.new_meal)
        add_button.grid(row=2, column=0, columnspan=2)

        view_button = Button(self.root, text="View History", command=self.view_records)
        view_button.grid(row=3, column=0, columnspan=2)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def new_meal(self):
        meal = self.meal_entry.get().strip()
        calories = self.calories_entry.get().strip()
        
        if meal and calories:
            try:
                calories = int(calories)
                self.data_manager.add_meal(meal, calories)
                
                self.meal_entry.delete(0, END)
                self.calories_entry.delete(0, END)
                
                messagebox.showinfo("Successful Update", "Meal added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for calories.")
        else:
            messagebox.showerror("Error", "Make sure all fields are filled in.")

    def view_records(self):
        records = self.data_manager.get_records()
        if records is not None:
            records_window = Toplevel(self.root)
            records_window.title("View Meals")
            
            records_text = Text(records_window, wrap=WORD)
            records_text.insert(INSERT, records.to_string(index=False))
            records_text.pack()
        else:
            messagebox.showerror("Error", "No records found.")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()