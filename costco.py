print ("Scraping COSTCO")
# 如果先前沒安裝過requests 則這邊會失敗, 因此需要先安裝, 可用這個指令: pip install requests
import requests 
 
# 指定要抓取的網頁URL
url = "https://www.costco.com.tw/Appliances/Cooling-Heating-Dehumidifiers/c/306"
url = "https://www.costco.com.tw/Electronics/Apple-Devices/iPhone/c/10704"
 
# 使用requests.get() 來得到網頁回傳內容
r = requests.get(url)
 
# request.get()回傳的是一個物件 
# 若抓成功, 則網頁原始碼會放在物件的text屬性, 我們把它存在一個變數 'web_content'
web_content = r.text
 
#print(web_content) 可以印出來看看, 會跟從網頁右鍵查看原始碼看到的一樣
# 載入BeautifulSoup套件, 若沒有的話可以先: pip install beautifulsoup4
from bs4 import BeautifulSoup

# 以 Beautiful Soup 解析 HTML 程式碼 : 
soup = BeautifulSoup(web_content, 'lxml')

# 找出所有class為"board-name"的div elements
listerNameElements = soup.find_all('div', class_="product-name-container")
listerNameElements

listerNames = [e.text for e in listerNameElements]
listerNames
# 觀察網頁原始碼後看到
# 雖然<div class="board-nuser">裡面還有用<span>夾住我們想要的資料(人氣值)
# 不過我們會用.text 直接取出所包含的文字部分即可 
priceElements = soup.find_all('div', class_="product-price")
# 取出的文字的類型是字串, 我們可用int()轉成數字類型
price = [ e.text for e in priceElements]
price
print(len(listerNames), len(price))
# 128 128
 
for bn, popu in zip(listerNames, price):
    print(popu, bn)
