import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")
daily_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
totalcase_df = daily_df.sum().reset_index(name="Count")
totalcase_df = totalcase_df.rename(columns={"index": "condition", "Count": "count"})
countries_df = daily_df.groupby("Country_Region").sum().reset_index()


def make_df(condition):
    df = pd.read_csv(f"data/time_series_{condition}.csv")
    df = (
        df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1)
        .sum()
        .reset_index(name=condition)
    )
    df = df.rename(columns={"index": "date"})
    return df


conditions = ["confirmed", "death", "recovered"]

condition_df = []
for c in conditions:
    condition_df.append(make_df(c))

merged = condition_df[0]
merged = pd.merge(condition_df[1], merged, how="left", on="date")
merged = pd.merge(condition_df[2], merged, how="left", on="date")