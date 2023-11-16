import os
import subprocess
import random

import planetMaker
import exoPlanetAnalyzer

star_count = 6
star_1_name = ""
star_2_name = ""
star_3_name = ""
star_4_name = ""
star_5_name = ""
star_6_name = ""

star_1_num_planets = 0
star_2_num_planets = 0
star_3_num_planets = 0
star_4_num_planets = 0
star_5_num_planets = 0
star_6_num_planets = 0

star_1_size = 0
star_2_size = 0
star_3_size = 0
star_4_size = 0
star_5_size = 0
star_6_size = 0

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

    planetCount = input("Maximum number of planets per star: ")

    if planetCount == "r":
        planetCount = random.randrange(0, 3)
    else:
        planetCount = int(planetCount)

    counter = 0
    star_1_name = "BTC " + str(random.randrange(1000, 9000))
    star_2_name = "BTC " + str(random.randrange(1000, 9000))
    star_3_name = "BTC " + str(random.randrange(1000, 9000))
    star_4_name = "BTC " + str(random.randrange(1000, 9000))
    star_5_name = "BTC " + str(random.randrange(1000, 9000))
    star_6_name = "BTC " + str(random.randrange(1000, 9000))

    star_1_num_planets = random.randrange(0, planetCount)
    star_2_num_planets = random.randrange(0, planetCount)
    star_3_num_planets = random.randrange(0, planetCount)
    star_4_num_planets = random.randrange(0, planetCount)
    star_5_num_planets = random.randrange(0, planetCount)
    star_6_num_planets = random.randrange(0, planetCount)

    star_1_size = random.randrange(1, 100)
    star_2_size = random.randrange(1, 100)
    star_3_size = random.randrange(1, 100)
    star_4_size = random.randrange(1, 100)
    star_5_size = random.randrange(1, 100)
    star_6_size = random.randrange(1, 100)

    # Check if the user wants to create planets
    print("I will create six stars with the following information:")
    print("Star 1: " + star_1_name+ " with " + str(star_1_num_planets) + " planets and a size of " + str(star_1_size)+ " solar masses")
    print("Star 2: " + star_2_name+ " with " + str(star_2_num_planets) + " planets and a size of " + str(star_2_size)+ " solar masses")
    print("Star 3: " + star_3_name+ " with " + str(star_3_num_planets) + " planets and a size of " + str(star_3_size)+ " solar masses")
    print("Star 4: " + star_4_name+ " with " + str(star_4_num_planets) + " planets and a size of " + str(star_4_size)+ " solar masses")
    print("Star 5: " + star_5_name+ " with " + str(star_5_num_planets) + " planets and a size of " + str(star_5_size)+ " solar masses")
    print("Star 6: " + star_6_name+ " with " + str(star_6_num_planets) + " planets and a size of " + str(star_6_size)+ " solar masses")

    createPlanets = input("Is this correct? (y/n): ").lower()
    if createPlanets == "y":
        print("Starting The Creation of Stars and Planets... STANDBY")
        while counter < star_count:
            counter += 1
            planetMaker.create_planets()
elif choice == "2":
    pass
elif choice == "3":
    print("Exiting Starweaver. Goodbye!")
else:
    print("Invalid choice. Please enter a valid option.")
