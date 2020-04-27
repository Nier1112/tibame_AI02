#從中央氣象局做出可以查詢縣市和天氣的查詢
import requests, prettytable
from bs4 import BeautifulSoup
url = requests.get(
    "https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"},
    params= {
            "ID": "Sat%20Apr%2011%202020%2019:58:30%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)"}
                 )

url.encoding = "UTF-8"
w = BeautifulSoup(url.text, "html.parser")
t = prettytable.PrettyTable(["縣市", "溫度"])
#地點整理
loc_list = []
loc = w.find_all("th")
for i in loc:
   loc_list.append(i.text)
#溫度整理
tem_list = []
temp = w.find_all("span", {"class":"tem-C is-active"})
for i in temp:
    tem_list.append(i.text)
while True:
    search = input("請輸入要查詢的縣市:")
    if search in loc_list:
        a = loc_list.index(search)
        t.add_row([search, tem_list[a]])
        print(t)
    else:
        print("查無資料")
