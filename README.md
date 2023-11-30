# Proyek Analisis Data: Bike Sharing Dataset 
- Nama: Yulia Harni
- Email: yuliaharni63@gmail.com

## Menentukan Pertanyaan Bisnis

- Bagaimana trends pada bike rentals by month, day, and hour?
- Apakah terdapat perbedaan yang signifikan dalam jumlah peminjaman sepeda pada musim tertentu?
- Bagaimana insight dari analisis RFM?

## Menyaipkan semua library yang dibuthkan


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
from plotly.subplots import make_subplots
```

## Data Wrangling

### Gathering Data


```python
df_day = pd.read_csv('C:/Users/User/Downloads/bike/day.csv')
df_hour = pd.read_csv('C:/Users/User/Downloads/bike/hour.csv')
```


```python
df_day .head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>instant</th>
      <th>dteday</th>
      <th>season</th>
      <th>yr</th>
      <th>mnth</th>
      <th>holiday</th>
      <th>weekday</th>
      <th>workingday</th>
      <th>weathersit</th>
      <th>temp</th>
      <th>atemp</th>
      <th>hum</th>
      <th>windspeed</th>
      <th>casual</th>
      <th>registered</th>
      <th>cnt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0.344167</td>
      <td>0.363625</td>
      <td>0.805833</td>
      <td>0.160446</td>
      <td>331</td>
      <td>654</td>
      <td>985</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2011-01-02</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0.363478</td>
      <td>0.353739</td>
      <td>0.696087</td>
      <td>0.248539</td>
      <td>131</td>
      <td>670</td>
      <td>801</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2011-01-03</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.196364</td>
      <td>0.189405</td>
      <td>0.437273</td>
      <td>0.248309</td>
      <td>120</td>
      <td>1229</td>
      <td>1349</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2011-01-04</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>0.200000</td>
      <td>0.212122</td>
      <td>0.590435</td>
      <td>0.160296</td>
      <td>108</td>
      <td>1454</td>
      <td>1562</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2011-01-05</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>0.226957</td>
      <td>0.229270</td>
      <td>0.436957</td>
      <td>0.186900</td>
      <td>82</td>
      <td>1518</td>
      <td>1600</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_hour.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>instant</th>
      <th>dteday</th>
      <th>season</th>
      <th>yr</th>
      <th>mnth</th>
      <th>hr</th>
      <th>holiday</th>
      <th>weekday</th>
      <th>workingday</th>
      <th>weathersit</th>
      <th>temp</th>
      <th>atemp</th>
      <th>hum</th>
      <th>windspeed</th>
      <th>casual</th>
      <th>registered</th>
      <th>cnt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.24</td>
      <td>0.2879</td>
      <td>0.81</td>
      <td>0.0</td>
      <td>3</td>
      <td>13</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.22</td>
      <td>0.2727</td>
      <td>0.80</td>
      <td>0.0</td>
      <td>8</td>
      <td>32</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.22</td>
      <td>0.2727</td>
      <td>0.80</td>
      <td>0.0</td>
      <td>5</td>
      <td>27</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.24</td>
      <td>0.2879</td>
      <td>0.75</td>
      <td>0.0</td>
      <td>3</td>
      <td>10</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.24</td>
      <td>0.2879</td>
      <td>0.75</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Assessing Data


```python
df_day.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 731 entries, 0 to 730
    Data columns (total 16 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   instant     731 non-null    int64  
     1   dteday      731 non-null    object 
     2   season      731 non-null    int64  
     3   yr          731 non-null    int64  
     4   mnth        731 non-null    int64  
     5   holiday     731 non-null    int64  
     6   weekday     731 non-null    int64  
     7   workingday  731 non-null    int64  
     8   weathersit  731 non-null    int64  
     9   temp        731 non-null    float64
     10  atemp       731 non-null    float64
     11  hum         731 non-null    float64
     12  windspeed   731 non-null    float64
     13  casual      731 non-null    int64  
     14  registered  731 non-null    int64  
     15  cnt         731 non-null    int64  
    dtypes: float64(4), int64(11), object(1)
    memory usage: 91.5+ KB
    


```python
# Display summary statistics
print(df_day.describe())
```

              instant      season          yr        mnth     holiday     weekday  \
    count  731.000000  731.000000  731.000000  731.000000  731.000000  731.000000   
    mean   366.000000    2.496580    0.500684    6.519836    0.028728    2.997264   
    std    211.165812    1.110807    0.500342    3.451913    0.167155    2.004787   
    min      1.000000    1.000000    0.000000    1.000000    0.000000    0.000000   
    25%    183.500000    2.000000    0.000000    4.000000    0.000000    1.000000   
    50%    366.000000    3.000000    1.000000    7.000000    0.000000    3.000000   
    75%    548.500000    3.000000    1.000000   10.000000    0.000000    5.000000   
    max    731.000000    4.000000    1.000000   12.000000    1.000000    6.000000   
    
           workingday  weathersit        temp       atemp         hum   windspeed  \
    count  731.000000  731.000000  731.000000  731.000000  731.000000  731.000000   
    mean     0.683995    1.395349    0.495385    0.474354    0.627894    0.190486   
    std      0.465233    0.544894    0.183051    0.162961    0.142429    0.077498   
    min      0.000000    1.000000    0.059130    0.079070    0.000000    0.022392   
    25%      0.000000    1.000000    0.337083    0.337842    0.520000    0.134950   
    50%      1.000000    1.000000    0.498333    0.486733    0.626667    0.180975   
    75%      1.000000    2.000000    0.655417    0.608602    0.730209    0.233214   
    max      1.000000    3.000000    0.861667    0.840896    0.972500    0.507463   
    
                casual   registered          cnt  
    count   731.000000   731.000000   731.000000  
    mean    848.176471  3656.172367  4504.348837  
    std     686.622488  1560.256377  1937.211452  
    min       2.000000    20.000000    22.000000  
    25%     315.500000  2497.000000  3152.000000  
    50%     713.000000  3662.000000  4548.000000  
    75%    1096.000000  4776.500000  5956.000000  
    max    3410.000000  6946.000000  8714.000000  
    


```python
# identifikasi missing value
df_day.isna().sum()
```




    instant       0
    dteday        0
    season        0
    yr            0
    mnth          0
    holiday       0
    weekday       0
    workingday    0
    weathersit    0
    temp          0
    atemp         0
    hum           0
    windspeed     0
    casual        0
    registered    0
    cnt           0
    dtype: int64




```python
# Check for duplicates
print(df_day.duplicated().sum())

# Remove duplicates
df_day = df_day.drop_duplicates()
```

    0
    


```python
# Display data types of each column
print(df_day.dtypes)
```

    instant         int64
    dteday         object
    season          int64
    yr              int64
    mnth            int64
    holiday         int64
    weekday         int64
    workingday      int64
    weathersit      int64
    temp          float64
    atemp         float64
    hum           float64
    windspeed     float64
    casual          int64
    registered      int64
    cnt             int64
    dtype: object
    


```python
df_hour.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 17379 entries, 0 to 17378
    Data columns (total 17 columns):
     #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
     0   instant     17379 non-null  int64  
     1   dteday      17379 non-null  object 
     2   season      17379 non-null  int64  
     3   yr          17379 non-null  int64  
     4   mnth        17379 non-null  int64  
     5   hr          17379 non-null  int64  
     6   holiday     17379 non-null  int64  
     7   weekday     17379 non-null  int64  
     8   workingday  17379 non-null  int64  
     9   weathersit  17379 non-null  int64  
     10  temp        17379 non-null  float64
     11  atemp       17379 non-null  float64
     12  hum         17379 non-null  float64
     13  windspeed   17379 non-null  float64
     14  casual      17379 non-null  int64  
     15  registered  17379 non-null  int64  
     16  cnt         17379 non-null  int64  
    dtypes: float64(4), int64(12), object(1)
    memory usage: 2.3+ MB
    


```python
# Display summary statistics
print(df_hour.describe())
```

              instant        season            yr          mnth            hr  \
    count  17379.0000  17379.000000  17379.000000  17379.000000  17379.000000   
    mean    8690.0000      2.501640      0.502561      6.537775     11.546752   
    std     5017.0295      1.106918      0.500008      3.438776      6.914405   
    min        1.0000      1.000000      0.000000      1.000000      0.000000   
    25%     4345.5000      2.000000      0.000000      4.000000      6.000000   
    50%     8690.0000      3.000000      1.000000      7.000000     12.000000   
    75%    13034.5000      3.000000      1.000000     10.000000     18.000000   
    max    17379.0000      4.000000      1.000000     12.000000     23.000000   
    
                holiday       weekday    workingday    weathersit          temp  \
    count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   
    mean       0.028770      3.003683      0.682721      1.425283      0.496987   
    std        0.167165      2.005771      0.465431      0.639357      0.192556   
    min        0.000000      0.000000      0.000000      1.000000      0.020000   
    25%        0.000000      1.000000      0.000000      1.000000      0.340000   
    50%        0.000000      3.000000      1.000000      1.000000      0.500000   
    75%        0.000000      5.000000      1.000000      2.000000      0.660000   
    max        1.000000      6.000000      1.000000      4.000000      1.000000   
    
                  atemp           hum     windspeed        casual    registered  \
    count  17379.000000  17379.000000  17379.000000  17379.000000  17379.000000   
    mean       0.475775      0.627229      0.190098     35.676218    153.786869   
    std        0.171850      0.192930      0.122340     49.305030    151.357286   
    min        0.000000      0.000000      0.000000      0.000000      0.000000   
    25%        0.333300      0.480000      0.104500      4.000000     34.000000   
    50%        0.484800      0.630000      0.194000     17.000000    115.000000   
    75%        0.621200      0.780000      0.253700     48.000000    220.000000   
    max        1.000000      1.000000      0.850700    367.000000    886.000000   
    
                    cnt  
    count  17379.000000  
    mean     189.463088  
    std      181.387599  
    min        1.000000  
    25%       40.000000  
    50%      142.000000  
    75%      281.000000  
    max      977.000000  
    


```python
# identifikasi missing value
df_hour.isna().sum()
```




    instant       0
    dteday        0
    season        0
    yr            0
    mnth          0
    hr            0
    holiday       0
    weekday       0
    workingday    0
    weathersit    0
    temp          0
    atemp         0
    hum           0
    windspeed     0
    casual        0
    registered    0
    cnt           0
    dtype: int64




```python
# Check for duplicates
print(df_day.duplicated().sum())

# Remove duplicates
df_day = df_day.drop_duplicates()
```

    0
    


```python
# Display data types of each column
print(df_hour.dtypes)
```

    instant         int64
    dteday         object
    season          int64
    yr              int64
    mnth            int64
    hr              int64
    holiday         int64
    weekday         int64
    workingday      int64
    weathersit      int64
    temp          float64
    atemp         float64
    hum           float64
    windspeed     float64
    casual          int64
    registered      int64
    cnt             int64
    dtype: object
    

### Menggabungakan kedua dataset


```python
all_data = df_day.merge(df_hour, on='dteday', how='inner', suffixes=('_day', '_hour'))
print(all_data.shape)
```

    (17379, 32)
    


```python
all_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>instant_day</th>
      <th>dteday</th>
      <th>season_day</th>
      <th>yr_day</th>
      <th>mnth_day</th>
      <th>holiday_day</th>
      <th>weekday_day</th>
      <th>workingday_day</th>
      <th>weathersit_day</th>
      <th>temp_day</th>
      <th>...</th>
      <th>weekday_hour</th>
      <th>workingday_hour</th>
      <th>weathersit_hour</th>
      <th>temp_hour</th>
      <th>atemp_hour</th>
      <th>hum_hour</th>
      <th>windspeed_hour</th>
      <th>casual_hour</th>
      <th>registered_hour</th>
      <th>cnt_hour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0.344167</td>
      <td>...</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.24</td>
      <td>0.2879</td>
      <td>0.81</td>
      <td>0.0</td>
      <td>3</td>
      <td>13</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0.344167</td>
      <td>...</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.22</td>
      <td>0.2727</td>
      <td>0.80</td>
      <td>0.0</td>
      <td>8</td>
      <td>32</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0.344167</td>
      <td>...</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.22</td>
      <td>0.2727</td>
      <td>0.80</td>
      <td>0.0</td>
      <td>5</td>
      <td>27</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0.344167</td>
      <td>...</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.24</td>
      <td>0.2879</td>
      <td>0.75</td>
      <td>0.0</td>
      <td>3</td>
      <td>10</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2011-01-01</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>2</td>
      <td>0.344167</td>
      <td>...</td>
      <td>6</td>
      <td>0</td>
      <td>1</td>
      <td>0.24</td>
      <td>0.2879</td>
      <td>0.75</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 32 columns</p>
</div>



### Cleaning Data


```python
#correct datatype
all_data['dteday'] = pd.to_datetime(all_data['dteday'])

# Verify the changes
print(all_data.dtypes)
```

    instant_day                 int64
    dteday             datetime64[ns]
    season_day                  int64
    yr_day                      int64
    mnth_day                    int64
    holiday_day                 int64
    weekday_day                 int64
    workingday_day              int64
    weathersit_day              int64
    temp_day                  float64
    atemp_day                 float64
    hum_day                   float64
    windspeed_day             float64
    casual_day                  int64
    registered_day              int64
    cnt_day                     int64
    instant_hour                int64
    season_hour                 int64
    yr_hour                     int64
    mnth_hour                   int64
    hr                          int64
    holiday_hour                int64
    weekday_hour                int64
    workingday_hour             int64
    weathersit_hour             int64
    temp_hour                 float64
    atemp_hour                float64
    hum_hour                  float64
    windspeed_hour            float64
    casual_hour                 int64
    registered_hour             int64
    cnt_hour                    int64
    dtype: object
    

## Exploratory Data Analysis (EDA) 


```python
# Display basic statistics of the 'cnt_hour' column (total rental bikes) over time
hourly_stats = all_data.groupby('hr')['cnt_hour'].describe()

# Display basic statistics of the 'cnt_day' column (total rental bikes) over days
daily_stats = all_data.groupby('dteday')['cnt_day'].describe()

# Display basic statistics of the 'cnt_day' column (total rental bikes) over months
monthly_stats = all_data.groupby('mnth_hour')['cnt_day'].describe()

# Print the results
print("Hourly Statistics:")
print(hourly_stats)

print("\nDaily Statistics:")
print(daily_stats)

print("\nMonthly Statistics:")
print(monthly_stats)

```

    Hourly Statistics:
        count        mean         std   min     25%    50%     75%    max
    hr                                                                   
    0   726.0   53.898072   42.307910   2.0   25.00   40.0   69.00  283.0
    1   724.0   33.375691   33.538727   1.0   11.00   20.0   42.25  168.0
    2   715.0   22.869930   26.578642   1.0    5.00   11.0   28.50  132.0
    3   697.0   11.727403   13.239190   1.0    3.00    6.0   15.00   79.0
    4   697.0    6.352941    4.143818   1.0    3.00    6.0    8.00   28.0
    5   717.0   19.889819   13.200765   1.0    8.00   19.0   29.00   66.0
    6   725.0   76.044138   55.084348   1.0   23.00   76.0  117.00  213.0
    7   727.0  212.064649  161.441936   1.0   55.50  208.0  332.00  596.0
    8   727.0  359.011004  235.189285   5.0  131.50  385.0  559.50  839.0
    9   727.0  219.309491   93.703458  14.0  155.00  216.0  293.00  426.0
    10  727.0  173.668501  102.205413   8.0  106.00  147.0  218.00  539.0
    11  727.0  208.143054  127.495536  10.0  123.00  180.0  256.00  663.0
    12  728.0  253.315934  145.081134   3.0  158.00  229.0  322.25  776.0
    13  729.0  253.661180  148.107657  11.0  154.00  224.0  322.00  760.0
    14  729.0  240.949246  147.271574  12.0  142.00  212.0  303.00  750.0
    15  729.0  251.233196  144.632541   7.0  151.00  227.0  324.00  750.0
    16  730.0  311.983562  148.682618  11.0  207.25  304.5  419.00  783.0
    17  730.0  461.452055  232.656611  15.0  262.25  475.0  604.75  976.0
    18  728.0  425.510989  224.639304  23.0  235.00  418.5  562.25  977.0
    19  728.0  311.523352  161.050359  11.0  174.75  309.5  414.50  743.0
    20  728.0  226.030220  119.670164  11.0  124.00  223.5  303.25  567.0
    21  728.0  172.314560   89.788893   6.0   95.00  173.5  233.00  584.0
    22  728.0  131.335165   69.937782   9.0   76.00  129.0  174.00  502.0
    23  728.0   87.831044   50.846889   2.0   50.00   80.0  121.00  256.0
    
    Daily Statistics:
                count    mean  std     min     25%     50%     75%     max
    dteday                                                                
    2011-01-01   24.0   985.0  0.0   985.0   985.0   985.0   985.0   985.0
    2011-01-02   23.0   801.0  0.0   801.0   801.0   801.0   801.0   801.0
    2011-01-03   22.0  1349.0  0.0  1349.0  1349.0  1349.0  1349.0  1349.0
    2011-01-04   23.0  1562.0  0.0  1562.0  1562.0  1562.0  1562.0  1562.0
    2011-01-05   23.0  1600.0  0.0  1600.0  1600.0  1600.0  1600.0  1600.0
    ...           ...     ...  ...     ...     ...     ...     ...     ...
    2012-12-27   24.0  2114.0  0.0  2114.0  2114.0  2114.0  2114.0  2114.0
    2012-12-28   24.0  3095.0  0.0  3095.0  3095.0  3095.0  3095.0  3095.0
    2012-12-29   24.0  1341.0  0.0  1341.0  1341.0  1341.0  1341.0  1341.0
    2012-12-30   24.0  1796.0  0.0  1796.0  1796.0  1796.0  1796.0  1796.0
    2012-12-31   24.0  2729.0  0.0  2729.0  2729.0  2729.0  2729.0  2729.0
    
    [731 rows x 8 columns]
    
    Monthly Statistics:
                count         mean          std     min     25%     50%     75%  \
    mnth_hour                                                                     
    1          1429.0  2228.370189  1139.804003   431.0  1263.0  1977.0  3272.0   
    2          1341.0  2671.260999  1137.608314  1005.0  1623.0  2402.0  3777.0   
    3          1473.0  3709.164969  1883.731151   605.0  2077.0  3239.0  5382.0   
    4          1437.0  4484.418928  1763.049463   795.0  3141.0  4220.0  6233.0   
    5          1488.0  5349.774194  1288.628585  2633.0  4401.0  4890.5  6421.0   
    6          1440.0  5772.366667  1230.447244  3767.0  4834.5  5308.5  6983.0   
    7          1488.0  5563.677419  1263.862677  3285.0  4475.0  5446.5  6685.0   
    8          1475.0  5689.239322  1457.790768  1115.0  4576.0  5255.0  7148.0   
    9          1437.0  5772.107864  1792.457187  1842.0  4539.0  5423.0  7525.0   
    10         1451.0  5319.965541  1842.788517    22.0  4187.0  5041.0  7282.0   
    11         1437.0  4245.956159  1276.061095  1495.0  3368.0  4068.0  5315.0   
    12         1483.0  3411.030344  1534.812094   441.0  2423.0  3485.0  4649.0   
    
                  max  
    mnth_hour          
    1          4521.0  
    2          5062.0  
    3          8362.0  
    4          7460.0  
    5          8294.0  
    6          8120.0  
    7          8173.0  
    8          7865.0  
    9          8714.0  
    10         8156.0  
    11         6852.0  
    12         6606.0  
    


```python
# Filter the dataset for each season and calculate aggregate statistics
seasonal_analysis = all_data.groupby('season_day').agg({
    'cnt_day': ['count', 'mean', 'std', 'min', 'max']
}).reset_index()

# Rename the columns for better readability
seasonal_analysis.columns = ['Season', 'Count', 'Mean', 'Std', 'Min', 'Max']

# Display the seasonal analysis
print(seasonal_analysis)

```

       Season  Count         Mean          Std   Min   Max
    0       1   4242  2635.348185  1391.789800   431  7836
    1       2   4409  4995.253119  1690.209773   795  8362
    2       3   4496  5654.093194  1446.451168  1115  8714
    3       4   4232  4765.366021  1654.202601    22  8555
    

### Visualization 

bagaimana trends in bike rentals by month, day, and hour.


```python
# Hourly trend
hourly_trend = all_data.groupby('hr')['cnt_hour'].mean()
plt.figure(figsize=(10, 6))
plt.plot(hourly_trend.index, hourly_trend.values, marker='o')
plt.title('Hourly Bike Rental Trend')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Bike Rentals')
plt.grid(True)
plt.show()

# Daily trend
daily_trend = all_data.groupby('dteday')['cnt_day'].mean()
plt.figure(figsize=(14, 6))
plt.plot(daily_trend.index, daily_trend.values, marker='o')
plt.title('Daily Bike Rental Trend')
plt.xlabel('Date')
plt.ylabel('Average Bike Rentals')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Monthly trend
monthly_trend = all_data.groupby('mnth_hour')['cnt_day'].mean()
plt.figure(figsize=(10, 6))
plt.plot(monthly_trend.index, monthly_trend.values, marker='o')
plt.title('Monthly Bike Rental Trend')
plt.xlabel('Month')
plt.ylabel('Average Bike Rentals')
plt.grid(True)
plt.show()

```


    
![png](Notebook_Submission_files/Notebook_Submission_31_0.png)
    



    
![png](Notebook_Submission_files/Notebook_Submission_31_1.png)
    



    
![png](Notebook_Submission_files/Notebook_Submission_31_2.png)
    


Analyze how bike rentals vary across different seasons.


```python
# Set the style of seaborn
sns.set(style="whitegrid")

# Create a bar plot for the seasonal analysis
plt.figure(figsize=(10, 6))
sns.barplot(x='Season', y='Mean', data=seasonal_analysis, palette="viridis")
plt.title('Average Bike Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Average Bike Rentals')
plt.show()

```

    C:\Users\User\AppData\Local\Temp\ipykernel_10768\2481080152.py:6: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.barplot(x='Season', y='Mean', data=seasonal_analysis, palette="viridis")
    


    
![png](Notebook_Submission_files/Notebook_Submission_33_1.png)
    


RFM Anlysis


```python
# Calculate Recency, Frequency, and Monetary Value
current_date = all_data['dteday'].max()

# Recency
recency = all_data.groupby('registered_hour')['dteday'].max().reset_index()
recency['recency'] = (current_date - recency['dteday']).dt.days
recency = recency[['registered_hour', 'recency']]

# Frequency
frequency = all_data.groupby('registered_hour').size().reset_index(name='frequency')

# Monetary Value
monetary_value = all_data.groupby('registered_hour')['cnt_hour'].sum().reset_index(name='monetary_value')

# Merge the three metrics
rfm_data = pd.merge(recency, frequency, on='registered_hour')
rfm_data = pd.merge(rfm_data, monetary_value, on='registered_hour')

# Display the RFM data
print(rfm_data.head())

```

       registered_hour  recency  frequency  monetary_value
    0                0       38         24              35
    1                1        0        201             294
    2                2        1        245             648
    3                3        0        294            1154
    4                4        3        307            1602
    


```python
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))
 
colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]
 
sns.barplot(y="recency", x="registered_hour", data=rfm_data.sort_values(by="recency", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("user_registered_hour",fontsize=18)
ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
ax[0].tick_params(axis ='x', labelsize=15)
 
sns.barplot(y="frequency", x="registered_hour", data=rfm_data.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("user_registered_hour",fontsize=18)
ax[1].set_title("By Frequency", loc="center", fontsize=18)
ax[1].tick_params(axis='x', labelsize=15)
 
sns.barplot(y="monetary_value", x="registered_hour", data=rfm_data.sort_values(by="monetary_value", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel("user_registered_hour",fontsize=18)
ax[2].set_title("By Monetary", loc="center", fontsize=18)
ax[2].tick_params(axis='x', labelsize=15)
 
plt.suptitle("Best Customer Based on RFM Parameters (registered_hour)", fontsize=20)
plt.show()
```

    C:\Users\User\AppData\Local\Temp\ipykernel_10768\3521458839.py:5: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.barplot(y="recency", x="registered_hour", data=rfm_data.sort_values(by="recency", ascending=False).head(5), palette=colors, ax=ax[0])
    C:\Users\User\AppData\Local\Temp\ipykernel_10768\3521458839.py:11: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.barplot(y="frequency", x="registered_hour", data=rfm_data.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
    C:\Users\User\AppData\Local\Temp\ipykernel_10768\3521458839.py:17: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.barplot(y="monetary_value", x="registered_hour", data=rfm_data.sort_values(by="monetary_value", ascending=False).head(5), palette=colors, ax=ax[2])
    


    
![png](Notebook_Submission_files/Notebook_Submission_36_1.png)
    


## Conclusion

- Bagaimana trends pada bike rentals by month, day, and hour?

--  Trend Bulanan: Peminjaman sepeda menunjukkan pola yang signifikan berdasarkan bulan .
                 Puncak peminjaman terjadi pada bulan-bulan musim panas, seperti musim panas dan musim gugur.

-- Trend Harian: Pada tingkat harian, terlihat pola yang jelas dengan peningkatan peminjaman selama jam-jam puncak.
Peminjaman mencapai puncaknya pada pagi dan sore hari, mencerminkan mobilitas tinggi seiring dengan perjalanan ke dan dari tempat kerja.


-- Trend Jam: Pada tingkat jam, pola harian menunjukkan bahwa sepeda lebih sering dipinjam pada jam-jam puncak perjalanan.
Jam-jam tertentu, seperti pagi hari dan sore hari, menjadi waktu yang paling diminati untuk peminjaman.

- Apakah terdapat perbedaan yang signifikan dalam jumlah peminjaman sepeda pada musim tertentu?

-- Berdasarkan tren ini, strategi penempatan sepeda lebih efektif jika ditingkatkan selama musim panas dan musim gugur

- Bagaimana insight dari analisis RFM?

-- Analisis RFM pada pengguna terdaftar per jam memberikan wawasan yang mendalam tentang preferensi dan kebiasaan pengguna, membantu penyedia layanan untuk mengambil tindakan yang lebih tepat guna dan meningkatkan kualitas layanan secara keseluruhan


```python

```
