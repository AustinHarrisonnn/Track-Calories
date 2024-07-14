from tkinter import *
from tkinter import messagebox
from datetime import date
import pandas as pd

# Function to add a new meal input into the CSV
def new_meal():
    meal = meal_entry.get().strip()            #Retrieves user input
    calories = calories_entry.get().strip()
    if meal and calories:
        try:
            calories = int(calories)
            update_record = {"Date": date.today().strftime("%Y-%m-%d"), "Meal": meal, "Calories": calories}  #Creates a new record with date, meal, and calorie information
            try:
                df = pd.read_csv("calories.csv")
            except FileNotFoundError:
                df = pd.DataFrame(columns=["Date", "Meal", "Calories"])
            df = df.append(update_record, ignore_index=True)
            df.to_csv("calories.csv", index=False)        #Save updated DataFrame back to CSV file
            meal_entry.delete(0, END)
            calories_entry.delete(0, END)  #Clearing input fields
            messagebox.showinfo("Successful Update", "Meal added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for calories.")
    else:
        messagebox.showerror("Error", "Make sure all fields are filled in.")

def view_records():
    try:
        df = pd.read_csv("calories.csv")
        records_window = Toplevel(root)  #Creates child of main window
        records_window.title("View Meals")
        records_text = Text(records_window, wrap=WORD)  #Creates text widget to display records and enabling word wrapping
        records_text.insert(INSERT, df.to_string(index=False))  #Inserts the DataFrame content as a string into the widget text
        records_text.pack()
    except:
        messagebox.showerror("Error", "No records found.")

root = Tk()
root.title("Calorie Tracker")

Label(root, text="Meal:").grid(row=0, column=0)
meal_entry = Entry(root)
meal_entry.grid(row=0, column=1)

Label(root, text="Calories:").grid(row=1, column=0)
calories_entry = Entry(root)
calories_entry.grid(row=1, column=1)

add_button = Button(root, text="Add Meal", command=new_meal)
add_button.grid(row=2, column=0, columnspan=2)

view_button = Button(root, text="View History", command=view_records)
view_button.grid(row=3, column=0, columnspan=2)

root.mainloop()