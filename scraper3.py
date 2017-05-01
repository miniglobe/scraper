# coding:utf-8
from __future__ import print_function
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from ast import literal_eval
from time import sleep
from bs4 import BeautifulSoup
import sys
import urllib.request
from http.client import BadStatusLine
from http.client import IncompleteRead



args = sys.argv
word = args[1]
#num = args[2]

# Chrome用のドライバを指定
driver = webdriver.Chrome()

# Googleの画像検索にアクセス
driver.get("https://www.google.co.jp/imghp")

# name属性にqが設定されている要素を取得
inputElement = driver.find_element_by_name("q")

# 実行時に渡した引数を検索バーに入力する
inputElement.send_keys(word)

# name属性にbtnGが設定されている要素を取得
submitElement = driver.find_element_by_name("btnG")

# 取得した要素をクリック
submitElement.click()
judge = 10000000
while True:
    scroll_h = driver.execute_script("var h = window.pageYOffset; return h")
    if scroll_h != judge:
        judge = driver.execute_script("var m = window.pageYOffset; return m")
        #スクロール
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
    else:
        try:
            moreElement = driver.find_element_by_id("smb")
            moreElement.click()
            sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except ElementNotVisibleException:
            break
        continue
print('load complete')


#20枚分のurlを取得
cnt = 0
n = 20
while (cnt < n):
    #ページのソースを取得
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,"lxml")
    soup = soup.find_all('div', class_="rg_meta")
    #検索結果枚数 cnt
    cnt = len(soup)
else:
    driver.quit()
print(cnt)

ulist=[]
for i in soup:
    dic = i.text.replace("false", "False").replace("true", "True")
    ulist.append(literal_eval(dic)["ou"])


#画像を取得
# urls = ulist[:n]
urls = ulist[:cnt]
for cntr ,img in enumerate(urls):
  print("[%03d]Downloading.. %s" % (cntr,img))
  try:
      raw_img = urllib.request.urlopen(img).read()
      f = open('%s/%s_%03d.png' % ('output', word, cntr), 'wb')
      f.write(raw_img)
      f.close()
  except:
      pass

#ブラウザをクローズ
driver.quit()
