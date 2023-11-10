import pandas as pd
import matplotlib.pyplot as plt

def plot_star_data():
    # Read in the CSV file
    df = pd.read_csv('star_data.csv')

    # Plot the data
    plt.plot(df['time'], df['luminosity'])
    plt.xlabel('Time')
    plt.ylabel('Luminosity')
    plt.title('Luminosity vs. Time')

    plt.ylim(0, 100)

    plt.show()

if __name__ == "__main__":
    print("Arrived at dataPlotter.py")
    plot_star_data()
