# -*- coding: utf-8 -*-
"""
Created on 2023.06.12
@author: Zisheng Ji
"""

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Open Chrome and Access the Website
option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
option.add_argument(
    '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
)
option.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=option)

driver.get('https://www.binance.com/en/markets/coinInfo-Launchpad?p=1')

LaunchpadName = []
page = True
while (page):
    try:
        for i in range(1, 16):
            TokenName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div[{}]/div/div[1]/div/div/div[3]/div".format(i)).text
            LaunchpadName.append(TokenName)
            print(i)
    except NoSuchElementException:
        page = False
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/div[4]/div/button[5]').click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/div[3]/div")))


def save_file(Data, col_name, save_address):
    Name = col_name
    TokenData = pd.DataFrame(data=Data, columns=Name)
    TokenData.to_excel(save_address, index=False)


save_file(LaunchpadName, ['Token'], 'TokenList.xlsx')
