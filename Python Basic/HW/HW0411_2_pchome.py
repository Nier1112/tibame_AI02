import requests, json, prettytable
#為 pchome 線上購物建立一個離線版本的商品搜尋程式
q = input("請輸入查詢關鍵字:")
u = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/all/results",
                 headers = {
                     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                     "Accept": "application/json, text/javascript, */*; q=0.01",
                     "Sec-Fetch-Dest": "empty",
                     "X-Requested-With": "XMLHttpRequest"
                 },
                 params= {
                     "q":q, #要讀取外面
                     "page":"1"
                 })
print(u.status_code) #code為200 正常存取, 自己看就好
r = json.loads(u.text) #[]和{}為json格式用json將格式轉換成python格式

t = prettytable.PrettyTable(["商品名稱", "價格"])
for i in r["prods"]:
    t.add_row([i["name"], i["price"]])
    t.align["商品名稱"] = "l"
    t.align["價格"] = "r"
print(t)
while True:
    page = 1
    pagein = input("輸入頁碼:")
    if page == "":
        page = 1
    else:
        page = pagein
    u = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/all/results",
                     headers = {
                         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                         "Accept": "application/json, text/javascript, */*; q=0.01",
                         "Sec-Fetch-Dest": "empty",
                         "X-Requested-With": "XMLHttpRequest"
                     },
                     params= {
                         "q":q,
                         "page":page
                     })
    r = json.loads(u.text)
    t = prettytable.PrettyTable(["商品名稱", "價格"])
    for i in r["prods"]:
        t.add_row([i["name"], i["price"]])
        t.align["商品名稱"] = "l"
        t.align["價格"] = "r"
    print(t)
