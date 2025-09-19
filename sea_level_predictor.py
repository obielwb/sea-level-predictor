import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')
    
    # Create first line of best fit (using all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    line1_y = slope * years_extended + intercept
    plt.plot(years_extended, line1_y, 'r', label='Fit 1880-2014')
    
    # Create second line of best fit (using data from 2000 onward)
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    # Only plot from 2000 to 2050 for the second line
    years_recent_extended = pd.Series(range(2000, 2051))
    line2_y = slope_recent * years_recent_extended + intercept_recent
    plt.plot(years_recent_extended, line2_y, 'g', label='Fit 2000-2014')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()