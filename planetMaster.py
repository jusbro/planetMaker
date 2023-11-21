"""
planetMaster.py is the main file for the starMaker application. 
It is responsible for creating the stars and planets, and calling the dataPlotter and starfieldMaker modules.

The main purpose of this project is to help teach students how we search for exoplanets (planets located outside of our system).
Since exoplanets are so far away, we can't see them directly. 
Instead, we look for the dimming of light from a star as a planet passes in front of it.

Finding real data for students to work with was hard, so I decided to create a program that would generate random data for them to work with.

This program creates six stars with random masses, given in solar masses (mass relative to our sun).
Each star has a potential for planets to orbit it, and the number of planets can be assigned or randomly generated.

Star names are randomly generated using a catalog called BTC (Browntown Catalog of Stars) ranging from 0 to 9999.

"""

print("Starting Application, please standby...") # this is necessary as the importing of libraries takes a few seconds 

import os
import random
import csv
import dataPlotter
import starfieldMaker

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
filename = "starMaker\test.csv"

min_transit_luminosity = 74
max_transit_luminosity = 80

fields = ['time', 'luminosity']
global time_counter
#time_counter = 0
#time_step = 0.5
#time_max = 100

transit_begin = 33
transit_end = 66

def make_luminosity(min_luminosity=90, max_luminosity=100):
    return random.randrange(min_luminosity, max_luminosity)

def make_transit_luminosity(min_transit_luminosity, max_transit_luminosity):
    return random.randrange(min_transit_luminosity, max_transit_luminosity)

def make_row(time_counter):
    return [time_counter, make_luminosity()]

def make_transit_row(time_counter):
    return [time_counter, make_transit_luminosity(min_transit_luminosity, max_transit_luminosity)]

def pick_transit_length():
    return random.randrange(0, 100)

def createFile(filename):
    time_counter = 0
    time_step = 0.5
    time_max = 100
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        while time_counter < time_max:
            if time_counter < transit_begin or time_counter > transit_end:
                csvwriter.writerow(make_row(time_counter))
                time_counter += time_step
            else:
                csvwriter.writerow(make_transit_row(time_counter))
                time_counter += time_step
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
    star_1_name = "BTC_" + str(random.randrange(1, 9999))
    star_2_name = "BTC_" + str(random.randrange(1, 9999))
    star_3_name = "BTC_" + str(random.randrange(1, 9999))
    star_4_name = "BTC_" + str(random.randrange(1, 9999))
    star_5_name = "BTC_" + str(random.randrange(1, 9999))
    star_6_name = "BTC_" + str(random.randrange(1, 9999))

    star_1_num_planets = planetCount
    star_2_num_planets = planetCount
    star_3_num_planets = planetCount
    star_4_num_planets = planetCount
    star_5_num_planets = planetCount
    star_6_num_planets = planetCount

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
            if counter == 1:
                starName = star_1_name
            elif counter == 2:
                starName = star_2_name
            elif counter == 3:
                starName = star_3_name
            elif counter == 4:
                starName = star_4_name
            elif counter == 5:
                starName = star_5_name
            elif counter == 6:
                starName = star_6_name
            filename = f"starMaker/{starName}.csv"
            print("Creating"+ filename)
            createFile(filename)
        print("Calling data plotter with the following names"+ star_1_name+ star_2_name+ star_3_name+ star_4_name+ star_5_name+ star_6_name)
        dataPlotter.plot_star_data(star_1_name, star_2_name, star_3_name, star_4_name, star_5_name, star_6_name)
        starfieldMaker.main(star_1_name, star_2_name, star_3_name, star_4_name, star_5_name, star_6_name)
elif choice == "2":
    pass
elif choice == "3":
    print("Exiting Starweaver. Goodbye!")
else:
    print("Invalid choice. Please enter a valid option.")
