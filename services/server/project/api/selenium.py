import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
import numpy as np
import pandas as pd
import chromedriver_binary
import os

options = webdriver.ChromeOptions() 
options.add_argument('--headless')
# options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
options.add_argument("--no-sandbox")  # userをrootとして起動する時に必要なオプション
# options.add_argument("--disable-setuid-sandbox") 
# options.add_argument("--disable-dev-shm-using") 
# options.add_argument("--disable-extensions") 
# options.add_argument("--disable-gpu") 
# options.add_argument("start-maximized") 
# options.add_argument("disable-infobars") 
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" 
# chrome_driver_binary = "/usr/local/bin/chromedriver" 
driver = webdriver.Chrome(options=options) 

def get_status():
    try:
        url = os.getenv('WHITE_BOARD_URL')
        driver.get(url)
        
        # 明示的待機処理
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "username")))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "password")))
        search_box = driver.find_element_by_name('username')
        search_box.send_keys('esaka')
        search_box = driver.find_element_by_name('password')
        search_box.send_keys('keisoku123')

        # ログイン実行
        # フォーム送信は送信ボタンをクリック or フォーム内の要素にsubmitメソッドを使用
        search_box.submit()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "container")))
        
        status = {}
        elements = driver.find_elements_by_class_name('m-2')

        for e in elements[0:14]:
            # element.textで選択しているDOMに表示されているtextを全て取得出来る．
            name = e.text.split("\n")[0]
            info = e.text.split("\n")[1]
            if "出社" in info:
                status[name] = True
            else:
                status[name] = False
    finally:
        driver.quit()
        print("browser閉じる")
    return status

def decide_whom(count):
    status = get_status()
    df = pd.concat([pd.Series(count), pd.Series(status)], axis = 1)
    df.columns = ["count", "status"]
    df = df.sort_values('count')
    for index, row in df.iterrows():
        if row["status"] == True:
            break
    # kari
    index = "Esaka"
    return index