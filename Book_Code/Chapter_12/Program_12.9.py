# Program 12.9: Write Python Program to Read 'Endangered_Species.csv' File. Sample
# Contents of 'Endangered_Species.csv' File Is Given Below. Plot Grouped Bar Chart to
# Display the Population Growth of These Endangered Species

import altair as alt
import pandas as pd


def main():
    df = pd.read_csv('Endangered_Species.csv')
    chart = alt.Chart(df).mark_bar().encode(
        alt.X('Species:N'),
        alt.Y('Population:Q'),
        alt.Column('Year'),
        alt.Color('Species:N')).properties(
        title="Endangered Species Population")
    chart.save('Endangered_Species_Population.json')


if __name__ == "__main__":
    main()
