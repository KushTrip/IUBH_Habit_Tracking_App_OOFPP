import os
import json
import pytest
import datetime

from habit import Habit
from database import HabitDatabase
import analytics


# ---------- FIXTURES ----------

@pytest.fixture
def sample_habits():
    today = datetime.date.today().strftime("%Y-%m-%d")
    return [
        {
            "name": "exercise",
            "description": "morning workout",
            "periodicity": "daily",
            "date_created": today,
            "last_completed": today,
            "streak": 3
        },
        {
            "name": "journal",
            "description": "write journal",
            "periodicity": "weekly",
            "date_created": today,
            "last_completed": today,
            "streak": 1
        },
        {
            "name": "broken",
            "description": "missed habit",
            "periodicity": "daily",
            "date_created": today,
            "last_completed": (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y-%m-%d"),
            "streak": 5
        }
    ]


@pytest.fixture
def temp_db_file(tmp_path):
    return tmp_path / "test_habits.json"


# ---------- HABIT CLASS TEST ----------

def test_habit_creation():
    h = Habit("read", "Read a book", "daily")
    assert h.name == "read"
    assert h.description == "Read a book"
    assert h.periodicity == "daily"
    assert h.last_completed is None
    assert h.streak == 0
    assert isinstance(h.to_dict(), dict)


# ---------- DATABASE MODULE TEST ----------

def test_save_and_load_habits(sample_habits, temp_db_file):
    db = HabitDatabase(temp_db_file)
    db.save_habits(sample_habits)
    loaded = db.load_habits()
    assert loaded == sample_habits


def test_load_empty_file(temp_db_file):
    db = HabitDatabase(temp_db_file)
    assert db.load_habits() == []


# ---------- ANALYTICS MODULE TEST ----------

def test_habits_list(sample_habits):
    assert analytics.habits_list(sample_habits) == sample_habits


def test_same_periodicity_habits(sample_habits):
    daily = analytics.same_periodicity_habits(sample_habits, "daily")
    assert all(h["periodicity"] == "daily" for h in daily)


def test_longest_streak(sample_habits):
    assert analytics.longest_streak(sample_habits) == 3


def test_habit_longest_streak(sample_habits):
    assert analytics.habit_longest_streak(sample_habits, "exercise") == 3
    assert analytics.habit_longest_streak(sample_habits, "journal") == 1
    assert analytics.habit_longest_streak(sample_habits, "nonexistent") == 0


def test_reset_broken_streaks(sample_habits):
    analytics.reset_broken_streaks(sample_habits)
    for h in sample_habits:
        if h["name"] == "broken":
            assert h["streak"] == 0
        else:
            assert h["streak"] > 0
