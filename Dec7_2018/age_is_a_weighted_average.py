from pandas import read_csv
from pandas import datetime
from pandas import DataFrame
from pandas import concat

# ToDo: Slide 22

# frame a sequence as a supervised learning problem
def timeseries_to_supervised(data, lag=1):
    df = DataFrame(data)
    columns = [df.shift(i) for i in range(1, lag+1)]
    columns.append(df)
    df = concat(columns, axis=1)
    df.fillna(0, inplace=True)
    return df

# load dataset
def parser(x):
    return x


series = read_csv(#'ford_explorer_Price-Year-Miles',
                  '../sales-of-shampoo-over-a-three-ye.csv',
                  header=0,
                  # ToDo: this is in slide 22 but doesn't work
                  #parse_dates[0]
                  index_col=0,
                  squeeze=True,
                  #date_parser=parser()
                  )

# Their data result:

# Month
# 1901-01-01    266.0
# 1901-02-01    145.9
# 1901-03-01    183.1
# 1901-04-01    119.3
# 1901-05-01    180.3
# Name: Sales, dtype: float64

# Mine:



# transform to supervised learning
X = series.values
#ToDo: AttributeError: 'numpy.ndarray' object has no attribute 'head'
print(X.head)
supervised = timeseries_to_supervised(X, 1)
print(supervised.head)

# ToDo: tests

# Open some files

