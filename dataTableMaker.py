import csv
import random


if __name__ == "__main__":
    print("Arrived at dataTableMaker.py")
    filename = "starMaker\star_data.csv"

    min_transit_luminosity = 74
    max_transit_luminosity = 80

    fields = ['time', 'luminosity']

    time_counter = 0
    time_step = 0.5
    time_max = 100

    transit_begin = 33
    transit_end = 66

    def make_luminosity(min_luminosity=90, max_luminosity=100):
        return random.randrange(min_luminosity, max_luminosity)

    def make_transit_luminosity(min_transit_luminosity, max_transit_luminosity):
        return random.randrange(min_transit_luminosity, max_transit_luminosity)

    def make_row():
        return [time_counter, make_luminosity()]

    def make_transit_row():
        return [time_counter, make_transit_luminosity(min_transit_luminosity, max_transit_luminosity)]

    def pick_transit_length():
        return random.randrange(0, 100)
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        while time_counter < time_max:
            if time_counter < transit_begin or time_counter > transit_end:
                csvwriter.writerow(make_row())
                time_counter += time_step
            else:
                csvwriter.writerow(make_transit_row())
                time_counter += time_step
