# Program 12.12: Write Python Program to read 'Tennis_Summary.csv' file. Sample
# contents of 'Tennis_Summary.csv' file is given below. Using the Heatmap, display the
# number of Grand Slam Tournaments won by different players

import altair as alt
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('Tennis_Summary.csv')
    chart = alt.Chart(df).mark_rect().encode(
        alt.X('Tennis_Player:N'),
        alt.Y('Grand_Slam_Tournaments:N'),
        alt.Color('Wins:Q')).properties(
        title="Grand Slam Tournaments Won by Tennis Players",
        width=350, height=400)
    chart.save('Tennis.json')


if __name__ == "__main__":
    main()
