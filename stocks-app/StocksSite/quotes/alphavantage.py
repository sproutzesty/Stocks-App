import pandas as pandas
import SECRET_KEY
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries

stock = input('What stock do you want to view?: ')
print('fb')

def rsi_dataframe(stock=stock):
        api_key = SECRET_KEY 
        period=60
        ts = TimeSeries(key=api_key, output_format='pandas')
        data_ts = ts.get_intraday(stock.upper(), interval='1min', outputsize='full')

    #indicator
        ti = TechIndicators(key=api_key, output_format='pandas')
        data_ti, mata_data_ti = ti.get_rsi(symbol=stock.upper(), interval='1min', time_period=period, series_type='close')

        df = data_ts[0][period::]

        return print(df)

rsi_dataframe()