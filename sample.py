# coding:utf-8
from selenium import webdriver
import sys
from time import sleep

arg = sys.argv
word = unicode(arg[1],'utf-8')

# Chrome用のドライバを指定
driver = webdriver.Chrome()

# Googleの画像検索にアクセス
driver.get("https://www.google.co.jp/imghp")

# name属性にqが設定されている要素を取得
inputElement = driver.find_element_by_name("q")

# 取得した要素にパンケーキを設定
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
        except:
            break
    continue
print('finish')

#ブラウザをクローズ
driver.quit()
