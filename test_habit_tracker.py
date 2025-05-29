import os
import json
import pytest
import datetime

from habit import Habit
from database import HabitDatabase
import analytics

# test_habit_tracker.py

# Fixtures are reusable functions that help set up test scenarios.

@pytest.fixture
def example():
    """
    Fixture that returns a list of example habits.
    
    - Gives various frequencies to test different scenarios.
    - Contains a habit with a broken streak to verify streak resetting functionality.
    - Uses today's date to dynamically generate values.
    """

    today = datetime.date.today().strftime("%Y-%m-%d")
    return [
        {
            "name": "exercise",
            "description": "morning workout",
            "periodicity": "daily",
            "date_created": today,
            "last_completed": today,
            "streak": 3             # Habit has been completed successfully for 3 consecutive days


        },
        {
            "name": "journal",
            "description": "write journal",
            "periodicity": "weekly",
            "date_created": today,
            "last_completed": today,
            "streak": 1            # Habit has been completed successfully for 1 week
        },
        {
            "name": "broken",
            "description": "missed habit",
            "periodicity": "daily",
            "date_created": today,
            "last_completed": (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y-%m-%d"),
            "streak": 5           # Habit was last completed 3 days ago, so it should reset to 0
        }
    ]


@pytest.fixture
def tempfile(tmp_path):   
    """
    it is a fixture that returns a temporary file path to be used for testing database operations.

    - makes an isolated file for testing to prevent disturbing real data.
    - Ensures tests do not rely on actual user data or files.
    """
    # Create a temporary file in the provided tmp_path
    return tmp_path / "test_habits.json"


# ---------- HABIT CLASS TEST ----------

# Testing the Habit class to ensure individual habit attributes work correctly.

def test_addhabit():      
    """
    Tests creating a Habit object and checks its attributes.

    - Ensures all initialized values are correct.
    - Checks dictionary conversion via `to_dict()`.
    """
    # Create a Habit object with specific attributes
    h = Habit("read", "Read a book", "daily")
    assert h.name == "read"
    assert h.description == "Read a book"
    assert h.periodicity == "daily"
    assert h.last_completed is None   # Newly created habit should have no completion history.

    assert h.streak == 0   # Newly created habit should start with a streak of 0.
    assert isinstance(h.to_dict(), dict) # Ensure to_dict() returns a dictionary representation of the habit.


# ---------- DATABASE MODULE TEST ----------

# Tests saving and loading operations within the HabitDatabase.


def test_saveload(example, tempfile):
    """
    Tests saving and loading habits in the HabitDatabase.

    - Saves the example habit data into a file.
    - Loads the data back to verify correctness.
    - checks that the saved and loaded data match exactly.
    """
    # Create a HabitDatabase instance with the temporary file path
    db = HabitDatabase(tempfile)                   # tempfile is a fixture that provides a temporary file path for testing.
    # Save the example habits to the file
    db.save_habits(example)
    loaded = db.load_habits()            # Load the habits back from the file
    assert loaded == example


def test_emptyfileload(tempfile):   
    """
    Tests loading habits from an empty file.

    - Ensures an empty habit database returns an empty list.
    """
    # Create a HabitDatabase instance with the temporary file path
    # and check if it returns an empty list when no habits are saved.
    db = HabitDatabase(tempfile)
    assert db.load_habits() == []


# ---------- ANALYTICS MODULE TEST ----------

# Tests various analytics functions to ensure they correctly analyze habits.

def test_habits_list(example):                      
    """
    Tests that the habits list is returned correctly.
    checks if the analytics function returns all example habits.
    """

    assert analytics.habits_list(example) == example 


def test_same_periodicity_habits(example):
    """
    Tests filtering habits based on periodicity.
    checks if function correctly filter habits with the same periodicity.
    """

    daily = analytics.same_periodicity_habits(example, "daily")
    assert all(h["periodicity"] == "daily" for h in daily)


def test_longest_streak(example):
    """
    Tests identifying the longest streak among habits.
    - locates the habit with the highest streak count.
    - checks if the result matches the expected streak.
    """

    assert analytics.longest_streak(example) == 3


def test_habit_longest_streak(example):
    """
    Tests retrieving the longest streak for a specific habit.
    - Checks known habits.
    - checks if function returns 0 for non-existent habits.
    """

    assert analytics.habit_longest_streak(example, "exercise") == 3
    assert analytics.habit_longest_streak(example, "journal") == 1
    assert analytics.habit_longest_streak(example, "nonexistent") == 0


def test_reset_broken_streaks(example):
    """
    Tests resetting streaks for habits that have been broken.
    - Resets streaks for habits if it is not checked off on time.
    - checks if streaks are reset only for those that have broken it.
    """
    # Reset broken streaks in the example habits
    # This will set the streak of the "broken" habit to 0, while others remain unchanged.
    analytics.reset_broken_streaks(example)
    for h in example:
        if h["name"] == "broken":
            assert h["streak"] == 0
        else:
            assert h["streak"] > 0
