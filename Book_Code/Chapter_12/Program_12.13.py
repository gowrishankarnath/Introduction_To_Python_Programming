# Program 12.13: Write Python Program to read 'Dinosaurs.csv' file. Sample contents
# of 'Dinosaurs.csv' file is given below. Create a Histogram displaying the length of
# different Dinosaurs

import altair as alt
import pandas as pd


def main():
    df = pd.read_csv('Dinosaurs.csv')
    chart = alt.Chart(df).mark_bar().encode(
        alt.X('Length:Q', bin=True, axis=alt.Axis(title='Dinosaurs Length in Meters (binned)')),
        alt.Y('count():Q', axis=alt.Axis(title='Total Number of Dinosaurs in each bin'))).properties(
        title="Length of Dinosaurs",
        width=350, height=400)
    chart.save("Dinosaurs.json")


if __name__ == "__main__":
    main()
