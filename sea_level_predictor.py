import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    df = pd.read_csv('./epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots(figsize=(12, 6))
    plt.scatter(x, y)

    y2 = linregress(x, y)
    x_pred = pd.Series([i for i in range(x.min(), 2050)])
    y_pred = y2.intercept + y2.slope * x_pred
    plt.plot(x_pred, y_pred, color="red")

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
