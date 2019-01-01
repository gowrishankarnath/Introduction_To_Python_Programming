# Program 12.11: Write Python Program to read 'Height_Weight_Ratio.csv' file. Sample
# contents of 'Height_Weight_Ratio.csv' file is given below. Using the Scatterplot,
# display the relation between height and weight in adult male and female

import altair as alt
import pandas as pd


def main():
    df = pd.read_csv('Height_Weight_Ratio.csv')
    chart = alt.Chart(df).mark_point().encode(
        alt.X('Height:N', axis=alt.Axis(title='Height (ft.in.)')),
        alt.Y('Weight:Q', axis=alt.Axis(title='Weight (kg)')),
        alt.Color('Sex:N')).properties(
        title="Height to Weight Ratio in Adult Male and Female",
        width=350, height=400)
    chart.save('Height_Weight_Ratio.json')


if __name__ == "__main__":
    main()
