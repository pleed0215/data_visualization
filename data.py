import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")
daily_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
totalcase_df = daily_df.drop(["Country_Region"], axis=1).sum().reset_index(name="Count")
totalcase_df = totalcase_df.rename(columns={"index": "condition", "Count": "count"})
countries_df = daily_df.groupby("Country_Region").sum().reset_index()

print (totalcase_df)
print (countries_df)

conditions = ["confirmed", "death", "recovered"]


def global_df():
    def make_df(condition):
        df = pd.read_csv(f"data/time_series_{condition}.csv")
        df = (
            df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1)
            .sum()
            .reset_index(name=condition)
        )
        df = df.rename(columns={"index": "date"})
        return df
    condition_df = []
    for c in conditions:
        condition_df.append(make_df(c))

    merged = condition_df[0]
    merged = pd.merge(condition_df[1], merged, how="left", on="date")
    merged = pd.merge(condition_df[2], merged, how="left", on="date")
    return merged


def country_df(country):
    def make_country_df (country, condition):
        c_df = pd.read_csv(f"data/time_series_{condition}.csv")
        c_df = c_df.loc[c_df["Country/Region"] == country]
        c_df = c_df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name=condition)
        c_df = c_df.rename(columns={"index":"date"})
        return c_df

    condition_df = []
    for c in conditions:
        condition_df.append(make_country_df(country, c))

    merged = condition_df[0]
    merged = pd.merge(condition_df[1], merged, how="left", on="date")
    merged = pd.merge(condition_df[2], merged, how="left", on="date")
    return merged

