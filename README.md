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

### filtering??

```python
    df = pd.read_csv("data/time_series_confirmed.py")
    df["Country/Region"] == "Afghanistan"
```

    - loc property
        - loc[] is primarily label based, but may also be used with a boolean array.

```python
    df = df.loc[df["Country/Region"] == "Afghanistan"]
```

    - 이렇게 하면 아프가니스탄만 나옴.

### sorting?

- sort_values(by, ascending, ..)

### Plotly/Dash - python open source graphing library

- pipenv install dash==0.14.0

- 기본 프레임은 튜토리얼에서 따오자.
- 핵심 -> layout
  - <code>app.layout ( children = [ ...])</code>의 형식
  - style argument로 css style을 줄 수 있다. css naming 형식은 js에서 사용하는 camel case.
    ```python
        html.H1("Corona dashboard", style={"textAlign": "center"})
    ```
- table을 이용하네..

  - table column header를 따려면 df.columns를 하면 된다.
  - python 문법에서 정말 중요한 내용을 여기서 말해준다.

  ```python
    html.Th(column_name) for column_name in countries_df.columns
  ```

  - values에 접근을 하려면, df.values를 하면 된다.
    - python이 정말 강력하고 쉬운 문법을 가지고 있다.. 그래서 많이들 사용을 하는 모양이다.
    ```python
        html.Tbody(
            children=[
                html.Tr(children=[html.Td(column) for column in value])
                for value in countries_df.values
            ]
        ),
    ```
    아름다운 수준이다 진짜... 저 길어질 코드가 어떻게 단 두줄만에...

- plotly express

  - bubble map

    - scatter_geo
      - 어째 강의에 나온 레퍼런스를 잘 못 찾겠다.(찾았다)
      - [scatter_geo] (https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html#plotly.express.scatter_geo)
      - 위의 내용과 소스 코드 참고를 하고,,
      - https://plotly.com/python/templates/

    ```python
    px.scatter_geo(
        countries_df,
        size="Confirmed",
        size_max=50,
        hover_data={
            "Confirmed": ":,2f",
            "Deaths": ":,2f",
            "Recovered": ":,2f",
            "Country_Region": False,
        },
        hover_name="Country_Region",
        locations="Country_Region",
        locationmode="country names",
        color="Confirmed",
        template="plotly_dark",
        text="Deaths",
    )
    ```

    - projection (str) – One of 'equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'albers usa', 'winkel tripel', 'aitoff', or 'sinusoidal'`Default depends on `scope.

    - color_continuous_scale (list of str) – Strings should define valid CSS-colors This list is used to build a continuous color scale when the column denoted by color contains numeric data. Various useful color scales are available in the plotly.express.colors submodules, specifically plotly.express.colors.sequential, plotly.express.colors.diverging and plotly.express.colors.cyclical.

    - x axis, y axis 이름을 바꾸고 싶다면...
      - fig.update_layout
      - [layout 관련 내용을 참조](https://plotly.com/python/reference/layout/)
      - 이름 바꾸는 것 뿐만 아니라, figure 전반적인 내용을 수정할 수 있음(margin)
      - update_layout 이외에 figure를 만들 때 labels 속성을 넣어도 된다.

### plotly graph_objects

    - https://plotly.com/python/graph-objects/
    - jupyter note도 참고.
    - 공식 문서에는 좋은 예제들이 많으니 참고하자.

### Core component

- interactive하게 만들어 주는 요소.

- @callback decorator

```python
    @app.callback(
        Output(component_id="hello-output", component_property="children"),
        [
            Input("hello-input", "value"))
        ]
    )
    def update_hello(value):
        pass
```

### Jupyter-Notebook

- pipenv install jupyterlab
- Try in Your Browser. No Installation Needed.

```

```
