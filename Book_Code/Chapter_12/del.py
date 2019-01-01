import altair as alt
import pandas as pd
import numpy as np

def main():
    df = pd.DataFrame({'x': 200 + 25*np.random.randn(1000)})
    chart = alt.Chart(df).mark_bar().encode(
        alt.X('x:Q', bin = True),
        alt.Y('count():Q')).properties(
        title="Histogram",
        width=350, height=400)
    chart.save('del.json')


if __name__ == "__main__":
    main()
