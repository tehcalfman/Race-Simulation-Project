# Author: Niall Cowman
# Description: A program for tracking and displaying stats to do with a group of runners

from functions import *


def main():
    # create a variable for the loop
    loop = True
    # create the loop
    while loop:
        # print the menu
        print(f"""
1. Show results for a race
2. Add results for a race
3. Show all competitors by county
4. Show the winner each race
5. Show all the race times for each competitor
6. Show all competitors who have won a race
7. Quit""")
        # give the user a choice
        choice = int(input("Choice > "))
        if choice == 1:
            # display the results
            display_results()
        elif choice == 2:
            # allow the user to add a new race
            create_race()
        elif choice == 3:
            # list the runners by country
            list_competitors()
        elif choice == 4:
            # show the winner for each race
            determine_winners()
        elif choice == 5:
            # list the time for a competitor
            competitor_times()
        elif choice == 6:
            # list the winners of each race
            list_winners()
        elif choice == 7:
            # quit the menu
            loop = False
        elif choice <= 0 or choice > 7:
            # if the user's choice is out of the range of options print this
            print("Error: Choice out of range")




main()