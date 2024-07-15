from tkinter import *
from tkinter import messagebox
import pandas as pd
from data_manager import DataManager

class CalorieTrackerApp:
    def __init__(self):
        self.root = Tk()  #Creates main window
        self.root.title("Calorie Tracker")
        self.data_manager = DataManager("calories.csv")  #Initialize DataManager with the file name

        self.setup_ui()  #Calling method to set up user interface

    def setup_ui(self):
        #Creating and placing label and entry for the meal user input
        Label(self.root, text="Meal:").grid(row=0, column=0)
        self.meal_entry = Entry(self.root)
        self.meal_entry.grid(row=0, column=1)

        #Creating and placing label and entry for the calories user input
        Label(self.root, text="Calories:").grid(row=1, column=0)
        self.calories_entry = Entry(self.root)
        self.calories_entry.grid(row=1, column=1)

        #Button to add new meal
        add_button = Button(self.root, text="Add Meal", command=self.new_meal)
        add_button.grid(row=2, column=0, columnspan=2)

        #Button to view meal history
        view_button = Button(self.root, text="View History", command=self.view_records)
        view_button.grid(row=3, column=0, columnspan=2)

        #Window closing protocol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def new_meal(self):
        meal = self.meal_entry.get().strip()
        calories = self.calories_entry.get().strip()
        
        if meal and calories:  #Check if both input fields are filled
            try:
                calories = int(calories)
                self.data_manager.add_meal(meal, calories)  #Adding meals and calories to the data manager
                
                #Clearing input fields
                self.meal_entry.delete(0, END)
                self.calories_entry.delete(0, END)
                
                messagebox.showinfo("Successful Update", "Meal added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for calories.")
        else:
            messagebox.showerror("Error", "Make sure all fields are filled in.")

    def view_records(self):
        records = self.data_manager.get_records()  #Obtains meal records
        if records is not None:
            records_window = Toplevel(self.root)  #Creates a new window to display meal records
            records_window.title("View Meals")
            
            records_text = Text(records_window, wrap=WORD)  #Creates a text widget to display records
            records_text.insert(INSERT, records.to_string(index=False))  #Insert records into the text widget
            records_text.pack()  #Packing the text widget
        else:
            messagebox.showerror("Error", "No records found.")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()