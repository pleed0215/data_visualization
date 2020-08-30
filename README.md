# Data Visualization - nomad coders

## Using Packages

### Pandas - python data analysis tools.

1. installation
   ```sh
       pipenv install pandas
   ```

- pandas는 data 중에서도 csv다루는데 아주 좋다.
- dataframe이라는 오브젝트를 만들어서 사용 한다고 한다.
- jupyter notebook에서

```python
    import pandas as pd
    daily_df = pd.read_csv("data/daily_report.csv")
    daily_df
```

- python language를 통하여 원하는 데이터를 추출할 수도 있다.
- jupyter notebook에서 뿐만 아니라 그냥 console에서 python으로 위 코드를 똑같이 해봐도 데이터가 아주 잘 출력이 된다.
  이 짧은 코드만 입력해도 어마어마하게 강력하게 데이터를 출력해준다.

```python
    daily_df["Country_Region"]
    daily_df[["Confirmed", "Deaths", "Recovered"]]
```

- method들도 있다.

```python
    daily_df[["Confirmed", "Deaths", "Recovered"]].sum()
```

- 결과는 jupyter notebook에서 바로 확인.
- .sum()의 결과를 보면 DataFrame이 아니다. Series 클래스(오브젝트)이다.
- type(daily_df.sum())
- series타입에서 reset_index()를 해주면 다시 data_frame 형태로 가는 모양이다.

  - series 타입보다 dataframe을 이용하려하는 이유는, dash에서 dataframe만 이용하기 때문이다.

  - 추측컨데 series라는 네이밍에서 추론할 수 있듯이.. 데이터를 순서대로 표시한 것, 그리고 reset_index()를 하면 다시 이를 cell형태로 만들어주는 것.. 이라고 생각이 든다.
  - reset_index의 결과로 나온 것들도 약간의 조작이 가능한데.
    <code>.reset_index(name="count")</code>

- rename() method

```python
    daily_df.rename(columns={'index', 'condition'})
```

    - column의 이름을 바꿔줄 수 있는 모양이다.

```
    daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index()
```

- dataframe을 건들지 않는다, 따라서 return value를 누군가에게 줘야 한다.

- groupby() method

```python
    daily_df = daily_df.groupby("Country_Region")
```

출력을 하게 되면 dataframe, series와는 다르게 출력이 안되고 오브젝트 타입만 나온다.

```python
    daily_df = daily_df.groupby("Country_Region").sum().reset_index()
```

- 이렇게 해주면 나라별로의 통계 데이터를 얻을 수 있다.

- drop(array, axis=?) method
  데이터프레임의 일부분을 잘라내는 ...

```python
    df = df.drop (["Province/State", "Country/Region", "Lat", "Long"], axis=1)
```

### data merging

- time series의 confirmed, death, recovered에서 얻어온 데이터를 합치고 싶으면..?

  - merge()

  - concat()
    사용방법은 문서를 참고하자.

### Plotly/Dash - python open source graphing library

- pipenv install dash==0.14.0

### Jupyter-Notebook

- pipenv install jupyterlab
- Try in Your Browser. No Installation Needed.
