import os
import subprocess

import planetMaker
import exoPlanetAnalyzer

os.system("cls")
print("Welcome Starweaver!")
print("Let's make some stars!")
print("What would you like to do?")

print("1. Create a new star")
print("2. View existing stars")
print("3. Exit")

choice = input("Enter your choice: ")

os.system("cls")

if choice == "1":
    print("You have chosen to create a new star, Starweaver.")
    print("Please enter the following information:")
    print("")
    print("For any data field, enter 'r' to create a random number for this variable.")
    print("")
    numberOfStars = input("Number of stars: ")
    starName = input("Star Name: ")
    starSize = input("Star Size (relative to our sun's mass(0.1-100)): ")
    planetCount = input("Number of planets: ")

    # Check if the user wants to create planets
    createPlanets = input("Do you want to create planets for this star? (y/n): ").lower()
    if createPlanets == "y":
        print("Calling planetMaker.py")
        subprocess.call(["python", r"C:\Users\jusbro\Python Projects\starMaker\planetMaker.py"])
elif choice == "2":
    
elif choice == "3":
    print("Exiting Starweaver. Goodbye!")
else:
    print("Invalid choice. Please enter a valid option.")
