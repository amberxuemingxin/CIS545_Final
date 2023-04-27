import pandas as pd
# data_split function
def data_split_generator(data):
    train_start_date = pd.to_datetime('1910-01-31')
    train_end_date = pd.to_datetime('1990-12-31')
    vali_end_date = pd.to_datetime('2000-12-31')
    # test_end_date = pd.to_datetime('2010-12-31')
    for i in range(5):
        # print(train_start_date, train_end_date, vali_end_date, test_end_date)
        train_start_date = train_end_date + pd.DateOffset(years=-30) + pd.offsets.MonthEnd(0)
        train_data = data[(data.target_dates >= train_start_date) & (data.target_dates <= train_end_date)]
        vali_data = data[(data.target_dates > train_end_date) & (data.target_dates <= vali_end_date)]
        yield train_data, vali_data
        train_end_date = train_end_date + pd.DateOffset(years=-10) + pd.offsets.MonthEnd(0)
        vali_end_date = vali_end_date + pd.DateOffset(years=-10) + pd.offsets.MonthEnd(0)

