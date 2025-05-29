# habit.py

"""
HABIT MODULE

- This file is first to be created because this file defines the Habit class, 
  which is the core structure that every other file depends on.

- The Habit class creates and manages different individual habits.

- Each habit includes a name, description, periodicity (daily/weekly),
  date created, last completed date, and a streak count.

"""

import datetime #Required for capturing when a habit is created or completed

class Habit:
    """
    - Class representing a habit with attributes and utility methods.
    - A blueprint for each habit to be created.
    - This class will hold all the data and logic related to a single habit.   
    
    """

    def __init__(self, name, description, periodicity):
        """
        Initialize a new Habit object.

        Argument: Parameters used with their datatype
            name (str): Name of the habit.
            description (str): Description of the habit.
            periodicity (str): Frequency of the habit ('daily' or 'weekly').
            date_created : stores the date
            last_completed : stores the latest date when a habit is checked off 
        """
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.date_created = datetime.date.today().strftime("%Y-%m-%d") # Automatically sets the creation date when the habit is made.
        #                                                                strftime formats the date as a string like "2025-05-28".
        self.last_completed = None # starts as none because habit hasn't been checked-off yet
        self.streak = 0  #starts at 0 and gradually increases as habit is checked-off

    def to_dict(self):
        #Returns the habit attributes.
        #converts the object into dictionary
        # For saving data to JSON file or displaying it
        return {
            'name': self.name,
            'description': self.description,
            'periodicity': self.periodicity,
            'date_created': self.date_created,
            'last_completed': self.last_completed,
            'streak': self.streak
        }
    
    # Now that a habit is created, the next logical step is to save it into a file and retrieve it later. So I will start building database.py next.
