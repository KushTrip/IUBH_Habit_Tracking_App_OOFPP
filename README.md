# IUBH_Habit_Tracking_App_OOFPP
***
# Table of Contents
- [What is a habit tracking Application ?](#What-is-a-habit-tracking-Application-?)
  * [Core Features of the Application](#Core-Features-of-the-Application)
    + [Analytics](#Analytics)
- [Guide to the installation of the application](#Guide-to-the-installation-of-the-application)
  * [Tools required ](#Tools-required)
  * [Installing the tools](#Installing-the-tools)
    + [Packages for running tests](#packages-for-running-tests)
  * [How To Run the Program](#how-to-run-the-program)
- [Usage](#usage)
  * [1. Creating a new habit](#1.-Creating-a-new-habit)
  * [2. Remove a Habit](#2.-Remove-a-Habit)
  * [3. Mark your habit as completed(Check-off habit)](#3.-Mark-your-habit-as-completed-(Check-offhabit))
  * [4. Analyze your habit](#4.-Analyze-your-habit)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Contact](#contact)

# What is a habit tracking Application ?

 A habit monitoring/tracking application is a command-line interface (CLI) application built with Python which helps users create and maintain healthy routines, allowing them to monitor their development by tracking their streaks and enhance their general well-being and productivity.The app allows users to keep track of their daily routines and habits by creating a new habit , and keep track of good habits to form and bad ones to break.

 This work is developed as  a part of *IU University of applied Science's* *object oriented and functional programming with python* module.


## Core Features of the Application
The habit tracker essentially allows a user to:

* Create a habit 
* Remove a habit 
* Set Periodicity of habits (Daily or weekly)
* Mark the habit as completed
* Delete a habit

### Analytics
Moreover, the user will also be able to:
* View all of their created habits
* Among all defined habits, view habits which are of the same periodicity.
* Among all defined habits, view the habit which has the longest streak.
* Among all defined habits, view the longest streak of a specific habit.



# Guide to the installation of the application

## Tools required 
* Python 3.7+ : Python is a high-level, interpreted programming language known for its simplicity and readability.
* Pytest : Pytest is a Python code testing framework that makes it easy to write and execute tests, making it easier to ensure the quality and correctness of your code.

## Installing the tools
 Make sure that Python 3.7 + is installed on your OS. You can download the latest version of Python from [this link.](https://www.python.org/downloads/)<br>
<br> To check wheter you have successfully installed python or not, you can open command prompt and type python --version, it should should then tell the python version you have installed in your pc.
```
C:\Users\username>python --version
Python 3.13.3
```
<br> After installing Python, you can proceed and install the following libraries. <br>



### Packages for running tests
To run the tests, you will need the following packages installed:
<br>Pytest - For testing functions:<br>
```
pip install pytest
```


## How To Run the Program
After installing the required tools, download the files from this repository and store them in a separate folder.
<br>
To clone the repository, navigate to the desired directory. Click this link to clone the repository and download the habit tracker application:
```
https://github.com/KushTrip/IUBH_Habit_Tracking_App_OOFPP.git
```

Open your command/terminal window and change directory [cd] to your downloaded folder.By changing directories, you can navigate to the specific location where the files or folders are located and perform operations on them.<br>
<br>
<br>Install it by running the below command:<br>
```
cd C:\Users\username\Downloads\IU-Habit-Tracking-Application-OOFPP
```
After that, type the following command to execute the program:
```
python main.py
```

Doing so will launch the CLI and then you'll be able to see and choose from the following options in your Habit Tracker:

```
                                        ===== HABIT TRACKING APPLICATION =====

                                        Welcome! What would you like to do?

                                        1. Add a new habit

                                        2. Check off a habit

                                        3. Habit Analysis

                                        4. Delete a habit

                                        5. Exit

                                        Enter your choice:

```


# HOW TO USE THE APP


## 1. Creating a new habit
Your first action should start by creating a habit and you can do so by launching the program and entering 1 to add a new habit:

It will further expose the user to a sub-menu, where you'll have to enter name, description of the habit and also enter its periodicity to either daily or weekly.
```

                                                                ========== HABIT TRACKER ==========

                                                                Welcome! What would you like to do?

                                                                1. Add a new habit

                                                                2. Check off a habit

                                                                3. Habit Analysis

                                                                4. Delete a habit

                                                                5. Exit

                                                                Your choice: 1

                                                                --- CREATE A NEW HABIT ---
                                                                Enter the name of your habit: example
                                                                Write a short description: example
                                                                How often will you do this Habit? (daily/weekly): weekly


                                                                HABIT 'example' ADDED!
```


## 2. Mark your habit as completed(Check-off )
To check-off or mark habit as complete, enter 2 to choose " Check off a habit" from the main screen, then enter the name of the habit you completed.
```
                                                              ========== HABIT TRACKER ==========

                                                                Welcome! What would you like to do?

                                                                1. Add a new habit

                                                                2. Check off a habit

                                                                3. Habit Analysis

                                                                4. Delete a habit

                                                                5. Exit

                                                                Your choice: 2

                                                                --- MARK A HABIT AS COMPLETED ---
                                                                Which habit did you complete? :  example


                                                                WELL DONE! 'example' COMPLETED.
```


## 3. Analyze your habit
The application also  provides the functionality to the users to analyze their habits. Enter 3 choose "Habit Analysis" from the main screen and then four analytical options are displayed to choose from.
```
                                                              ========== HABIT TRACKER ==========

                                                                Welcome! What would you like to do?

                                                                1. Add a new habit

                                                                2. Check off a habit

                                                                3. Habit Analysis

                                                                4. Delete a habit

                                                                5. Exit

                                                                Your choice: 3

                                                               --- HABIT ANALYSIS ---
                                                                1. Show all habits
                                                                2. Show habits by periodicity
                                                                3. Show habit with the longest streak
                                                                4. Show streak for a specific habit

                                                                Choose one:
```

## 4. Remove a Habit
Enter 4 to Choose "Delete a habit" option from the main screen and type the name of the habit you wish to remove.
```
                                                              ========== HABIT TRACKER ==========

                                                                Welcome! What would you like to do?

                                                                1. Add a new habit

                                                                2. Check off a habit

                                                                3. Habit Analysis

                                                                4. Delete a habit

                                                                5. Exit

                                                                Your choice: 4
                                                                --- REMOVE A HABIT ---
                                                                Enter name of the habit to delete: example
                                                                'example' HAS BEEN REMOVED.
```

# Running tests
To run the test: navigate to the test folder (included with the repository) through command/terminal by using [cd](https://www.alphr.com/change-directory-in-cmd/) and then type ```pytest```. 

# Contributing

Contributions are eagerly welcomed! If you have any suggestions, troublesome bug reports, or awe-inspiring feature requests, please feel free to open an issue. Your feedback will be greatly appreciated!

# Contact

Kush Tripathi - [Email](tripathikush10@gmail.com)

Project Link: [(https://github.com/KushTrip/IU-Habit-Tracking-Application-OOFPP)](https://github.com/KushTrip/IUBH_Habit_Tracking_App_OOFPP.git)
