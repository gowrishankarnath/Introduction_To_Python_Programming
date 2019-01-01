# Program 12.8: Write Python Program to Read 'WorldCups.csv' File. Sample Contents
# of 'WorldCups.csv' File Is Given Below. Plot Bar Chart to Display the Number of
# Times a Country Has Won Football WorldCup

import pandas as pd
import altair as alt


def main():
    worldcup_df = pd.read_csv('WorldCups.csv')
    winning_countries = worldcup_df['Winner'].value_counts()
    winners_total_df = pd.DataFrame({'Country': winning_countries.index.tolist(),
                                     'Number_of_Wins': winning_countries.values.tolist()})
    chart = alt.Chart(winners_total_df).mark_bar().encode(
        alt.X('Country:N'),
        alt.Y('Number_of_Wins:Q'),
        alt.Color('Country:N')).properties(
        title="Football WorldCup Winners")
    chart.save('WorldCup_Winners.json')


if __name__ == "__main__":
    main()

