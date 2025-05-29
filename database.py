# database.py

"""
Database Module

- Now that Habit objects exist (from habit.py), we need a way to store them and load them later.

- Without database.py, the app could create habits but would lose them the moment the app is closed.

- HabitDatabase handles all file-based operations, keeping this logic separate from the user interface (main.py).

- This file is second to be created because now that we have the structure of a habit,
  we can define how to save/load it in this module.

- this file handles Loading/Saving of a habit data to/from a JSON file.

"""

import json   # to save/load habits in a .json file.
import os     # used to check if the file (habits.json) exists before trying to read it.

class HabitDatabase:
    # Class dedicated to handle all habit data storage applications like loading and saving habits to a JSON file.
    # Encapsulates the logic for reading and writing habit data to a file so main.py can focus on user interaction.

    def __init__(self, filename):
        """
        Initialize with a given filename.

        Argument:
            filename (str): Path to the JSON file used for storing habits.
        """
        self.filename = filename

    def load_habits(self):
        """
        Load the habits from the JSON file.

        Returns:
            list: A list of habit dictionaries.
        """
        if not os.path.exists(self.filename):   # Check if the file exists
            return []                           # If the file doesn’t exist yet (first run), return an empty list so the program doesn’t crash.
        with open(self.filename, 'r') as f:     # Opens the file in read mode and loads the contents
            return json.load(f)  # Load the habits from the JSON file and return them as a list of dictionaries.

    def save_habits(self, habits):
        """
        Save the habits to the JSON file [habits.JSON].

        Argument:
            habits (list): A list of habit dictionaries.
        """
        with open(self.filename, 'w') as f:    
            json.dump(habits, f, indent=4)     # serializes the list of dictionaries into a properly formatted JSON string
