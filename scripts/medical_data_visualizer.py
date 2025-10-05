import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data from medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# 2. Add an 'overweight' column to the data
# Calculate BMI and determine if overweight (BMI > 25)
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # 5. Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()
    df_cat.rename(columns={'size': 'total'}, inplace=True)

    # 7. Convert the data into long format and create a chart that shows the value counts of the categorical features using sns.catplot()
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig

    # 8. Get the figure for the output and store it in the fig variable
    # 9. Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# 10. Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # 11. Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
    # - diastolic pressure is higher than systolic (Keep the correct data with df['ap_lo'] <= df['ap_hi'])
    # - height is less than the 2.5th percentile (Keep the correct data with df['height'] >= df['height'].quantile(0.025))
    # - height is more than the 97.5th percentile
    # - weight is less than the 2.5th percentile
    # - weight is more than the 97.5th percentile
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calculate the correlation matrix and store it in the corr variable
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle and store it in the mask variable
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Plot the correlation matrix using sns.heatmap()
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    # 16. Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


# Execute the functions to generate the visualizations
if __name__ == '__main__':
    print("Generating categorical plot...")
    draw_cat_plot()
    print("Categorical plot saved as 'catplot.png'")
    
    print("\nGenerating heat map...")
    draw_heat_map()
    print("Heat map saved as 'heatmap.png'")
    
    print("\nData shape:", df.shape)
    print("\nFirst few rows of processed data:")
    print(df.head())
