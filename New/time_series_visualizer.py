import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('./fcc-forum-pageviews.csv',
                 parse_dates=["date"],
                 index_col="date")

df = df[df['value'] > df['value'].quantile(0.024)]
df = df[df['value'] < df['value'].quantile(0.974)]


def draw_line_plot():

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.lineplot(data=df, ax=ax, color='red')

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    plt.xticks(rotation=45)

    fig.savefig('line_plot.png')

    return fig


def draw_bar_plot():

    df_bar = df.copy()

    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    df_bar = df_bar.groupby(["year", "month"])['value'].mean().reset_index()

    df_bar_pivot = df_bar.pivot(index='year', columns='month', values='value')

    fig = df_bar_pivot.plot.bar(legend=True,
                                figsize=(10, 5),
                                ylabel='Average Page Views',
                                xlabel='Years').figure

    months_in_order = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November',
                       'December']
    plt.legend(months_in_order, title='Months')

    fig.savefig('bar_plot.png')

    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(
        data=df_box,
    )

    ax.set_xlabel()
    ax.set_ylabel()
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
