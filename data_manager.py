import pandas as pd
from datetime import date
import os

class DataManager:
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            self.data = pd.read_csv(self.filename)
        else:
            self.data = pd.DataFrame(columns=["Date", "Meal", "Calories"])

    def add_meal(self, meal, calories):
        new_record = {"Date": date.today().strftime("%Y-%m-%d"), "Meal": meal, "Calories": calories}
        new_df = pd.DataFrame([new_record])
        self.data = pd.concat([self.data, new_df], ignore_index=True)
        self.save_data()

    def get_records(self):
        if os.path.exists(self.filename):
            return self.data
        return None

    def save_data(self):
        self.data.to_csv(self.filename, index=False)