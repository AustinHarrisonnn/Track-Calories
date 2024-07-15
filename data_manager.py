import pandas as pd
from datetime import date
import os

class DataManager:
    def __init__(self, filename):
        self.filename = filename  #Stores the filename
        if os.path.exists(self.filename):  #Checking if file exists
            self.data = pd.read_csv(self.filename)   #Loading data from file
        else:
            self.data = pd.DataFrame(columns=["Date", "Meal", "Calories"]) #Creates new data frame if file does not exist

    def add_meal(self, meal, calories):
        #Creates a new record with the current date, meal, and calories
        new_record = {"Date": date.today().strftime("%Y-%m-%d"), "Meal": meal, "Calories": calories}
        new_df = pd.DataFrame([new_record])  #Creates a DataFrame from new record
        self.data = pd.concat([self.data, new_df], ignore_index=True)  #Appends the new record to the existing data
        self.save_data()

    def get_records(self):
        if os.path.exists(self.filename):
            return self.data
        return None

    def save_data(self):
        self.data.to_csv(self.filename, index=False)  #Saves the data to the file