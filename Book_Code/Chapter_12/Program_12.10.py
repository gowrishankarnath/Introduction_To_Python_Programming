# Program 12.10. Write Python Program to read 'Company_Annual_Net_Income.csv' file.
# Sample contents of 'Company_Annual_Net_Income.csv'
# file is given below. Plot Line chart to display the annual net income of these companies.

import pandas as pd
import altair as alt


def main():
    company_net_income_df = pd.read_csv('Company_Annual_Net_Income.csv')
    chart = alt.Chart(company_net_income_df).mark_line().encode(
        alt.X('Year:N', axis=alt.Axis(title='Year')),
        alt.Y('Profit:Q', axis=alt.Axis(title='Profit (in Billions)')),
        alt.Color('Company:N')).properties(
        title="Annual Net Income",
        width=250, height=250)
    chart.save('Company_Net_Income.json')


if __name__ == "__main__":
    main()
