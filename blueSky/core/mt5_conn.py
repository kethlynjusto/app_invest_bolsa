from datetime import datetime, timedelta
import pandas as pd
import MetaTrader5 as mt5

NoneType = type(None)

# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()


def is_invalid_data(rates):
    return type(rates) is NoneType

def get_data_by_bar(stocks: list, bars: int, timeframe: int) -> pd.DataFrame:
    data = None
    for i, stock in enumerate(stocks):
        rates = mt5.copy_rates_from_pos(stock, timeframe, 0, bars)

        if is_invalid_data(rates): 
            continue

        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame['stock'] = stock

        if i == 0:
            data = rates_frame
        else:
            data = data.append(rates_frame)
            
    return data      


def get_data_start_from(stocks: list, start_date: datetime, bars: int, timeframe: int) -> pd.DataFrame:
    data = None
    for i, stock in enumerate(stocks):
        #stz = start_date - timedelta(hours=3)

        rates = mt5.copy_rates_from(stock, timeframe, start_date, bars)

        if is_invalid_data(rates):  
            continue

        rates_frame = pd.DataFrame(rates)
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame['stock'] = stock

        if i == 0:
            data = rates_frame
        else:
            data = data.append(rates_frame)
            
    return data          


def get_data_by_date(stocks: list, start_date: datetime, end_date:datetime, timeframe: int) -> pd.DataFrame:
    data = None
    for i, stock in enumerate(stocks):
        rates = mt5.copy_rates_range(stock, timeframe, start_date, end_date)
        
        if is_invalid_data(rates):  
            continue
        
        rates_frame = pd.DataFrame(rates)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame['stock'] = stock

        if i == 0:
            data = rates_frame
        else:
            data = data.append(rates_frame)

    return data