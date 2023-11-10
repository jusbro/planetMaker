import csv

def read_star_data():
    rows = []
    with open("star_data.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    print(header)
    print(rows)

if __name__ == "__main__":
    read_star_data()
