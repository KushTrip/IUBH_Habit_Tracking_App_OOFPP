# main.py

"""
Habit Tracker Application - Main Module
This File: main.py is basically the FACE of the Habit Tracker application.
The codes here serve as the entry point for the Habit Tracker application.
It enables users to create, check-off, analyze, and delete habits.
Habit data is stored and retrieved from a JSON file using the HabitDatabase class.

Module files:
- habit: Has the Habit class for creating habit objects.
- database: Oversees the loading and saving of habits to a JSON file.
- analytics: Provides analytics functions for evaluating habit performance.
"""

import datetime
from habit import Habit
from database import HabitDatabase
import analytics
from colorama import Fore            # Used for colored terminal output to enhance user experience.

#------------------------------------------- TO DISPLAY CREATED HABIT ---------------------------------------

# A function to show[s] details of a habit [h]
def s(h):
    
    print(f"{Fore.YELLOW}\t\t\t\t\t\t\t\tname: {h['name']}")
    print(f"\t\t\t\t\t\t\t\tdescription: {h['description']}")
    print(f"\t\t\t\t\t\t\t\tperiodicity: {h['periodicity']}")
    print(f"\t\t\t\t\t\t\t\tdate created: {h['date_created']}")
    print(f"\t\t\t\t\t\t\t\tlast completed: {h.get('last_completed', 'N/A')}")
    print(f"\t\t\t\t\t\t\t\tstreak: {h['streak']}\n")


    # Logic To Display a warning if the habit's streak is broken
    if analytics.streak_evaluate(h) == 0 and h['streak'] == 0:                   # If the habit's streak is broken and the streak is zero

        print(f"{Fore.RED}\t\t\t\t\t\t\t\tCAUTION: Streak of habit '{h['name']}' is broken and was reset to 0 due to not checking-off on time.\n")
    else:
        print()  # Just a newline for clean spacing



#------------------------------------------- TO CREATE A NEW HABIT ---------------------------------------

# TO get input from user to create a new habit and append it to the list of habits.
def add(list):                                           # list = list of habits
    """
    User is prompted to enter details for a new habit,
    create a Habit object, and add it to the list.
    """
    print(Fore.CYAN + "\t\t\t\t\t\t\t\t--- CREATE A NEW HABIT ---")
    name = input("\t\t\t\t\t\t\t\tEnter the name of your habit: ")
    info = input("\t\t\t\t\t\t\t\tWrite a short description: ")
    freq = input("\t\t\t\t\t\t\t\tHow often will you do this Habit? (daily/weekly): ")
    habit_obj = Habit(name, info, freq)
    list.append(habit_obj.to_dict())
    print("\n")
    print(f"{Fore.GREEN}\t\t\t\t\t\t\t\tHABIT '{name}' ADDED!\n")


#------------------------------------------- TO CHECK-OFF A HABIT ---------------------------------------

# Marks a habit as completed and updates the streak based on time.
# To Display check-off of a habit
def checkoff(list):
    """
    Mark a habit as completed by updating its streak
    based on periodicity (daily/weekly).
    """
    print(Fore.CYAN + "\t\t\t\t\t\t\t\t--- MARK A HABIT AS COMPLETED ---")
    target = input("\t\t\t\t\t\t\t\tWhich habit did you complete? :  ")
    for h in list:
        if h['name'] == target:              # If the habit with the given name is found
            today = datetime.date.today()        # Get today's date
            last_completed = h.get('last_completed')         # If the habit has been completed before, get the last completed date

            if last_completed:
                # Parse the last completed date
                last_completed = datetime.datetime.strptime(last_completed, "%Y-%m-%d").date()        # Convert the string date to a datetime.date object
                # Calculate the difference in days between today and last completed date
                diff = (today - last_completed).days

                # Reset streak if missed more than 1 day (daily) or 7 days (weekly)
                if h['periodicity'] == 'daily':
                    h['streak'] = 1 if diff > 1 else h['streak'] + 1         # If the habit is daily and more than 1 day has passed since last completion, reset streak to 1, otherwise increment by 1
                elif h['periodicity'] == 'weekly':
                    h['streak'] = 1 if diff > 7 else h['streak'] + 1        # If the habit is weekly and more than 7 days have passed since last completion, reset streak to 1, otherwise increment by 1
            else:
                # First time marking as completed
                h['streak'] = 1

            h['last_completed'] = today.strftime("%Y-%m-%d")# Update the last completed date to today
            print("\n")
            print(f"{Fore.GREEN}\t\t\t\t\t\t\t\tWELL DONE! '{target}' COMPLETED.\n")
            return
    print("\nCOULDN'T FIND THAT HABIT.\n")


#------------------------------------------- HABIT ANALYSIS ---------------------------------------

#To display analytics of habits 
#offfers the user different options to analyze their habits.
def analyze(list):
    """
    Display the needed analytics options to the user :
    - all habits
    - habits by frequency
    - longest streak of all
    - longest streak for a specific habit
    """
    analytics.reset_broken_streaks(list)  # Ensure outdated streaks are zeroed out, i.e reset back to 0

    print(Fore.CYAN + "\t\t\t\t\t\t\t\t--- HABIT ANALYSIS ---")
    print("\t\t\t\t\t\t\t\t1. Show all habits")
    print("\t\t\t\t\t\t\t\t2. Show habits by periodicity")
    print("\t\t\t\t\t\t\t\t3. Show habit with the longest streak")
    print("\t\t\t\t\t\t\t\t4. Show longest streak for a specific habit")

    option = input("\n\t\t\t\t\t\t\t\tChoose one: ")
    print()

    if option == '1':
        for h in analytics.habits_list(list):                                          # Get all habits
            s(h)                                                                    # Display each habit

    elif option == '2':
        freq = input(Fore.CYAN + "\t\t\t\t\t\t\t\tEnter frequency (daily/weekly): ")         # Get frequency from user
        matching = analytics.same_periodicity_habits(list, freq)                          # Filter habits by frequency
        for h in matching:
            s(h)                                                                        # Display each habit that matches the frequency

    elif option == '3':
        top_streak = analytics.longest_streak(list)                                    # Get the longest streak of all habits
        print(f"\t\t\t\t\t\t\t\tTop streak is: {top_streak}\n")                        # Display the longest streak

    elif option == '4':
        name = input("\t\t\t\t\t\t\t\tHabit name: ")                           # Get the name of the habit from the user 
        streak = analytics.habit_longest_streak(list, name)                    # Get the streak for the specified habit
        print(f"\t\t\t\t\t\t\t\t'{name}' streak: {streak}\n")                 # Display the streak for the specified habit

    # If the user enters an invalid option
    else:
        print(Fore.RED + "\t\t\t\t\t\t\t\tNOT A VALID CHOICE!")


#------------------------------------------- TO REMOVE A NEW HABIT ---------------------------------------


#To display habit removal
def remove(list):                                                                   #let the user remove a habit by name
    """
    Prompt the user to remove a habit by name,
    and delete it from the list if found.
    """
    print(Fore.CYAN + "\t\t\t\t\t\t\t\t--- REMOVE A HABIT ---")
    target = input("\t\t\t\t\t\t\t\tEnter name of the habit to delete: ")

    for h in list:                                                             # Iterate through the list of habits

        if h['name'] == target:                                                # If the habit with the given name is found

            list.remove(h)                                                     # Remove the habit from the list

            print(f"{Fore.GREEN}\t\t\t\t\t\t\t\t'{target}' HAS BEEN REMOVED.\n")

            return 
    print(f"Habit '{target}' was not found.\n")                                # If the habit is not found, print a message indicating that it was not found.



#----------------------------------------------------------------- MAIN FUNCTION --------------------------------------------------------------

# Main function to run the Habit Tracker application
def main():
    """
    Main loop for running the Habit Tracker application.
    Loads data, presents menu options, and processes user commands.
    """
    db = HabitDatabase('habits.json')                                             # Initialize the HabitDatabase with the filename 'habits.json'
    list = db.load_habits()                                                      # Load existing habits from the JSON file

    while True:
        print(Fore.RED + "\n\n\t\t\t\t\t\t\t\t========== HABIT TRACKER ==========")
        print(Fore.BLUE + "\n\t\t\t\t\t\t\t\tWelcome! What would you like to do?")
        print(Fore.MAGENTA + "\n\t\t\t\t\t\t\t\t1. Add a new habit")
        print("\n\t\t\t\t\t\t\t\t2. Check off a habit")
        print("\n\t\t\t\t\t\t\t\t3. Habit Analysis")
        print("\n\t\t\t\t\t\t\t\t4. Delete a habit")
        print("\n\t\t\t\t\t\t\t\t5. Exit")

        option = input("\n\t\t\t\t\t\t\t\tYour choice: ")
        print()

        if option == '1':
            add(list)
        elif option == '2':
            checkoff(list)
        elif option == '3':
            analyze(list)
        elif option == '4':
            remove(list)
        elif option == '5':
            db.save_habits(list)                                                       # Save the updated habits list to the JSON file
            print(Fore.RED + "\t\t\t\t\t\t\t\tThanks for using the Habit Tracker!")
            break
        else:
            print(Fore.RED + "\t\t\t\t\t\t\t\tInvalid choice, try again.")


# Program entry point
if __name__ == '__main__':
    main()
