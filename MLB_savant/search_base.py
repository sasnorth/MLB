#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


get_ipython().system('pip install beautifulsoup4')


# In[3]:


from selenium import webdriver
import time
import pandas as pd

from selenium.webdriver.common.keys import Keys

# In[4]:
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\\Users\\sasno\\Desktop\\Mypandas\\MLB_savant"}
chromeOptions.add_experimental_option("prefs", prefs)
# chromeOptions.add_argument('--ignore-certificate-errors')


# GoogleChromeを起動
browser = webdriver.Chrome(executable_path='C:\\Users\\sasno\\Desktop\\Mypandas\\chromedriver.exe', chrome_options=chromeOptions)
browser.implicitly_wait(3)


# In[6]:

# ウェブサイトへアクセス
url = "https://baseballsavant.mlb.com/statcast_search"
time.sleep(1)
browser.get(url)
print(url, ":アクセス完了")


# In[ ]:



# In[9]:
# テキストボックス入力
NAME = "darvish"
element = browser.find_element_by_xpath('//*[@id="pitchers_lookup_chosen"]/ul/li/input')
element.clear()
element.send_keys(NAME)
element.send_keys(Keys.ENTER)
print("フォームを送信")

# チェックボックス入力
select = browser.find_element_by_xpath('//*[@id="ddlPitchTypes"]/div[1]')
select.click()
time.sleep(1)
check = browser.find_element_by_xpath('//*[@id="lbl_PT_FF"]')
check.click()
print("チェックボックスを選択")

# 入力したデータをクリック
browser_from = browser.find_element_by_xpath('//*[@id="pfx_form"]/div[3]/div/input[1]')
time.sleep(1)
browser_from.click()
print("情報を入力してSearchを押しました")
time.sleep(1)


# In[10]:


# ダウンロードボタンをクリック
frm = browser.find_element_by_xpath('//*[@id="table_all_pid_"]/img')
time.sleep(1)
frm.click()
time.sleep(1)
print('ダウンロードボタンをクリック')


# In[ ]:




