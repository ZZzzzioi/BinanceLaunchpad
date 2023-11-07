import requests
import json
from prettytable import PrettyTable
import pandas as pd
from random import randint
import time
import os
import glob


def compose_params(token_id, vs_currency, days, interval):
    result = ''
    prms = {
        'token_id': token_id,
        'vs_currency': vs_currency,
        'days': days,
        'interval': interval
    }
    result = 'https://api.coingecko.com/api/v3/coins/' +\
    '{}/market_chart?vs_currency={}&days={}&interval={}'.format(
        prms['token_id'], prms['vs_currency'], prms['days'], prms['interval'])
    return result

'''
1. 按照时间序列进行合并， 制作数据表格
2. 通过数据绘制折线图, 上传GoogleSheet
'''
def price(parms)
    resp = requests.get(parms).text
    json_body = json.loads(resp)
    json_data = json_body['prices']
    data_res = PrettyTable()
    title_list = ['Time', 'Open', 'High', 'Low', 'Close', 'Value']
    data_res.field_names = title_list
    data_list = []
    for node in json_data:
        arr = [dict_value for key, dict_value in node.items()]
        data_list.append(arr)
        data_res.add_row(arr)
    print(data_res[:10])
    return data_list

TokenData = pd.read_excel('TokenList.xlsx')
TokenSymbol = list(TokenData['Symbol'])
vs_currency = 'usd'
days = 'max'
interval = 'daily'
token_id = TokenSymbol[0]
parms = compose_params(token_id, vs_currency, days, interval)

