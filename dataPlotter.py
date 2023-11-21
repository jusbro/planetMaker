import pandas as pd
import matplotlib.pyplot as plt

def plot_star_data(starname1, starname2, starname3, starname4, starname5, starname6, output_filename="star_plot.jpg"):
    star_names = [starname1, starname2, starname3, starname4, starname5, starname6]
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))  # 2 rows, 3 columns for 6 plots

    for i in range(6):
        star = star_names[i]
        filename = f'starMaker/{star}.csv'  # Construct filename for each star
        row = i // 3
        col = i % 3
        ax = axs[row, col]

        # Read in the CSV file
        df = pd.read_csv(filename)

        # Plot the data in the corresponding subplot
        ax.plot(df['time'], df['luminosity'])
        ax.set_title(f'{star} Data')
        ax.set_xlabel('Time')
        ax.set_ylabel('Luminosity')
        ax.set_ylim(0, 100)  # Limit y-axis to 0-100 for consistency

    # Adjust layout and display the plots
    plt.tight_layout()

    # Save the plot as a JPG file with the specified output filename
    plt.savefig(f"starMaker/{output_filename}")

    # Show the plot (optional)
    plt.show()
