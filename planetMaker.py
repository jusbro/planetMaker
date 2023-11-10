# Import statements for dataTableMaker and dataPlotter

import subprocess
import dataTableMaker
import dataPlotter

# Function to create planets
def create_planets():
    # Your existing code for creating planets goes here
    print("Starting dataTableMaker.py")
    subprocess.call(["python", r"C:\Users\jusbro\Python Projects\starMaker\dataTableMaker.py"])
    print("Finished running dataTableMaker.py")
    print("Starting dataPlotter.py")
    subprocess.call(["python", r"C:\Users\jusbro\Python Projects\starMaker\dataPlotter.py"])
    print("Finished running dataPlotter.py")
    print("Finished running planetMaker.py")
# Execution guard
if __name__ == "__main__":
    print("Arrived at planetMaker.py")
    create_planets()
