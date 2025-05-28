# analytics.py

"""
Analytics Module

Provides helper functions to analyze habit data, such as filtering by periodicity,
finding the longest streak, and specific habit streaks.
"""
import datetime    # Used to check streak status based on dates (last_completed vs today).

def habits_list(list):
    """Return all habits.

    Argument:
        habit_list (list): List of habit dictionaries.

    Returns:
        list: Same list of habits.
    """
    return list



def same_periodicity_habits(list, freq):
    """
    Filter and return habits by specified periodicity.

    Argument:
        habit_list (list): List of habit dictionaries.
        freq (str): Frequency to choose between ('daily' or 'weekly').

    Returns:
        list: Filtered list of habits.
    """
    return [h for h in list if h['periodicity'] == freq]



def streak_evaluate(habit, current_date=None):
    """
    - Core helper to evaluate whether a habit's current streak is still valid.
    - Used internally by the last two functions.
    """
    if not habit['last_completed']:
        return 0                                                                      #  If the habit has never been completed, return streak 0.

    
    if current_date is None:
        current_date = datetime.date.today()                                          # date of date_created
    last_date = datetime.datetime.strptime(habit['last_completed'], "%Y-%m-%d").date() # Parse the string date [For Ex: ("2025-05-27")] into a real datetime.date object.
    diff = (current_date - last_date).days                                              # Calculate how many days ago the habit was last completed.


    if habit['periodicity'] == 'daily' and diff > 1:                # If the habit is daily and more than 1 day has passed since last completion
        return 0                                                    # reset the streak to 0. 
    elif habit['periodicity'] == 'weekly' and diff > 7:            # If the habit is weekly and more than 7 days have passed since last completion
        return 0                                                  # reset the streak to 0.
    
    return habit['streak']                                       # Otherwise, return the current streak value if the habit is still valid.



def longest_streak(list):
    """
    Find the longest streak among all habits.

    Args:
        habit_list (list): List of habit dictionaries.

    Returns: Longest streak found.
    """
    if not list:
        return 0                                           # If the list is empty, return 0.
    return max(streak_evaluate(h) for h in list)  # Use streak_evaluate to get the streak for each habit and return the maximum value.



def habit_longest_streak(list, name):                       
    """
    Get the streak value for a specific habit by name.

    Args:
        habit_list (list): List of habit dictionaries.
        name (str): Name of the habit to search for.

    Returns:
        int: Streak value or 0 if not found.
    """
    for h in list:                            # Iterate through the list of habits
        
        if h['name'] == name:                 # Check if the habit's name matches the provided name
            return streak_evaluate(h)       # If a match is found, evaluate the streak
    return 0                          # If no match is found, return 0
	
	


def reset_broken_streaks(habit_list):
    """
    Resets the streak of habit to 0 if the user doesn't maintain the streak by not checking off a habit daily/weekly, making streak invalid.
    This avoids confusion when analyzing.
	Informs the user in the output when a streak is reset due to inactivity.
    """
    for habit in habit_list:
        if streak_evaluate(habit) == 0:
            habit['streak'] = 0

