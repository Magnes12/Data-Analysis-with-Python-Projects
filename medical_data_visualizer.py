import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('./medical_examination.csv')


df['BMI'] = df['weight'] / ((df['height'] / 100)**2)
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop(columns=['BMI'], inplace=True)

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1


def draw_cat_plot():

    df_cat = pd.melt(df,
                     id_vars=['cardio', 'id'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                     )

    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    fig = g.fig

    fig.savefig('catplot.png')
    return fig


def draw_heat_map():

    df_heat = df.copy()
    df_heat = df_heat[df_heat['ap_lo'] <= df_heat['ap_hi']]
    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]
    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    corr = df_heat.corr().round(1)

    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(10, 8))

    g = sns.heatmap(
        corr,
        annot=True,
        cmap='coolwarm',
        fmt='.1f',
        mask=mask
    )

    fig = g.figure

    fig.savefig('heatmap.png')
    return fig
