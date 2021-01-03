"""
Goal:
1. get & save stock data
2. reformat stock data
3. plot stock data
"""

import pandas_datareader
from pandas_datareader import data as pdr
import yfinance as yf


def collect_single_stock_data(code, start, end, file_format='csv'):
    # maintain valid api get_data_yahoo
    yf.pdr_override()
    # collect data
    count = 10
    while count >= 0:
        try:
            stock = pdr.get_data_yahoo(code,'2000-01-01','2020-12-31', retry_count=10)
            break
        except RuntimeError as e:
            print("data acquire attempt {} fail: {}".format(10 - count, e))
            count -= 1
        else:
            print("success!")
            # save data
            if file_format == 'csv':
                stock.to_csv('./data/'+code+'.csv')
            else:
                stock.to_excel('./data/'+code+'.csv')
            return stock
    print("data acquirement fail!")

# yf.pdr_override()
# stockCodeList = []
# stockCodeList.append('000001.sz')     # 深股“平安银行”
# for code in stockCodeList:
#     stock = pandas_datareader.get_data_yahoo(code,'2019-01-02','2019-01-03')
#     print(stock)


if __name__ == "__main__":
    collect_single_stock_data("000001.sz", '2000-01-01', '2021-1-1')    # 深股“平安银行”
