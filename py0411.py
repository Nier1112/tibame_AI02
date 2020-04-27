#import requests
#import codecs

# #抓網頁,
# header_data = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
#         "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#         "Cookie":"PHPSESSID=82r6aonhv5nlnn3kbadupjb675",
#         "Referer":"http://teaching.bo-yuan.net/"}
# #用post丟訊息給網頁
# u1 = requests.post(
#     "http://teaching.bo-yuan.net/",
#     headers = header_data,
#     params = {"uid":"5e9113485c1b6"},
#     data = {"ex[class]":"5e81f839475de", "ex[username]":"17楊子奇", "ex[password]":"d13dc5"})
#
# # cookie 和uid會每次登入都變更，需要再次確認. 先用post丟資訊出去，再用get拿取登入後的畫面
# #用get拿取網頁資訊出現亂碼表示需要更換編碼
# u2 = requests.get(
#     "http://teaching.bo-yuan.net/",
#     headers = header_data)
#＃會遇到亂碼的時候表示編碼需要更改，中文編碼：Big5 or utf8兩種
# u2.encoding="UTF-8"　
# if u2.text.find("ac1=member") != -1: #登入進去找到只有登入前沒有，登入後才有的頁面找到他的參數放進來確認
#     print("登入成功")
# else:
#     print("登入失敗")

#用python try 登入密碼的方式

# header_data = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
#         "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#         "Cookie":"PHPSESSID=82r6aonhv5nlnn3kbadupjb675",
#         "Referer":"http://teaching.bo-yuan.net/"}
#
# for psw in range(0, 9999,1):
#     u1 = requests.post(
#         "http://teaching.bo-yuan.net/",
#         headers = header_data,
#         params = {"uid":"5e9113485c1b6"},
#         data = {"ex[class]":"5e81f839475de", "ex[username]":"99測試", "ex[password]": psw})
#
#     u2 = requests.get(
#         "http://teaching.bo-yuan.net/",
#         headers = header_data)
#
#     u2.encoding="UTF-8"
#     if u2.text.find("ac1=member") != -1:
#         print("登入成功, 密碼是:", psw)
#         break
#     else:
#         print("登入失敗")

# #把csv的檔案讀取成list
# import csv
# r = list(csv.reader(codecs.open("自來水水質抽驗結果(106年1月).csv", "r", "utf8")))
# for i in r:
#     print(i)
# import csv, io
# u3 = requests.get("https://tppkl.blob.core.windows.net/blobfs/TaipeiTree.csv",
#                   headers = {
#                       "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#                       "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
#                   })
# print(u3.text)
# r = list(csv.reader(io.StringIO(u3.text)))
# for i in r:
#     print(r)

#json資料轉換
# import json,requests
# u4 = requests.get("https://data.taipei/api/getDatasetInfo/downloadResource",
#                   headers = {
#                       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#                       "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
#                   },
#
#                   params = {
#                       "id":"ac589468-529b-4636-a9b2-ab57ae41cbcb",
#                       "rid":"24c9f8fe-88db-4a6e-895c-498fbc94df94"
#                   })
# # json.loads是把json檔案開啟成為list檔案, list理面是字典
# d = json.loads(u4.text)
# for i in d:
#    print(i["o_tlc_agency_name"], i["o_tlc_agency_category"], i["o_tlc_agency_categorychild"])

# #把網站上的API 位址貼上，並換上參數，limit在網頁上可以直接操作，也可加入參數中調整，或調整成根據輸入顯是結果
# import json,requests
# u5 = requests.get("https://data.taipei/opendata/datalist/apiAccess",
#                   headers = {
#                       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#                       "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
#                   },
#
#                   params = {
#                       "scope":"resourceAquire",
#                       "rid":"24c9f8fe-88db-4a6e-895c-498fbc94df94",
#                       "limit": input("請輸入要查看幾筆資料:")
#                   })
# # json.loads是把json檔案開啟成為list檔案, list理面是字典
# d = json.loads(u5.text)
# print("========================")
# for i in d["result"]["results"]:
#    print(i["o_tlc_agency_categorychild"], i["o_tlc_agency_address"])

# #testbymyself csv
# import csv, requests, io
# u6 = requests.get("https://data.taipei/api/getDatasetInfo/downloadResource",
#                   params= {
#                       "id":"262e80cf-579c-4bfb-ba73-31621bc84616",
#                       "rid":"f8cd1bf4-55db-4566-a2d6-f53a8cf446bb"
#                   })
# r = list(csv.reader(io.StringIO(u6.text)))
# for i in r:
#     print(i[1], i[2], i[3])

#json
# import requests, json, prettytable
# u7 = requests.get("	https://data.taipei/api/getDatasetInfo/downloadResource",
#                   params={
#                       "id":"262e80cf-579c-4bfb-ba73-31621bc84616",
#                       "rid":"6af9f68b-b9e8-4ce4-ba29-c1038c556cd8"
#                   })
# r = json.loads(u7.text)
# t = prettytable.PrettyTable(["燈號", "地區", "燈種", "距離"]) #把資料裝入prettytable裏面
# for i in r:
#     t.add_row([i["LIGHTID"], i["Dist"], i["LightKind1"], i["LightWatt1"]])
# print(t)

# #中國信託網頁，資料並非在網址裏面, 會由動態載入方式處理
# import requests
#
# u8 = requests.post(
#     "https://www.ctbcbank.com/IB/api/adapters/IB_Adapter/resource/preLogin",
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#         "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#         "Connection": "keep-alive",
#         "Content-Length": "495",
#         "Content-Type": "application/json",
#         "Cookie": "CTBC_ctbcbank_dap=!/Ek7q9Bq+97IUF9b2FCKhpyPkKrRw+WKiNysKyyh9KQIIidQzzdNUE79LTwi1H1eb9V6PyT7AQu97Q==; pzqXflQLz5wTSg5443S=PWZicSlpBae6xVzN30P9tR9Rf07A_jz0ZyuCYAwGHCtJgEpR4fPpmpmhgs_udtbq; BIGipServer~EBMW~POOL_EBMW_WEB=!4tEBp+EzpIXGd7db2FCKhpyPkKrRw0emjjaKd/vntI5G0+gr3z/mRSqIlx37vFvksgPEu6YIhh9v/w==; TS01a2d410=01c2a9c2b982fd4bff8a68c708615a34323fd4df21b7a813340b659a3065265e03c45c29c5ac7fda2708e99f687fb89028e17a46bc; ngsessionid=1586583582641; v1st=E6F52D56D95FF2C2; BIGipServer~EBMW~POOL_EBMW_TAG=!ZJJMQAxsfMnor+hb2FCKhpyPkKrRw6ReBuwhmrqmHQdI/tmRW700k4+/4dCFk5LHpuzCnjwMdNW0AQ==; TS0152eaef=01c2a9c2b982fd4bff8a68c708615a34323fd4df21b7a813340b659a3065265e03c45c29c5ac7fda2708e99f687fb89028e17a46bc; s_fid=74BA97DEFE52C0AA-20D658B380139084; s_cc=true; JSESSIONID=0000pVGyIuMGsbJ5c1KX0vq2F8d:-1; EBMWSID=FBdnwDClYYTT5zhRWusNMHwhdYHaqT4HK1J7XBU92xmynLt47OCE!-864382513; BIGipServer~EBMW~POOL_EBMWIB_AP=!aTFrjez9QJJE5rNb2FCKhpyPkKrRw2IfAnvwXVUHoXir90Wym87LasTUWDZsqoMkCi9pv7PeDnwrnLo=; _ga=GA1.2.478375549.1586583592; _gid=GA1.2.527796260.1586583592; _gat_UA-136408356-1=1; _gat_UA-136403503-1=1; _gat_UA-148818971-1=1; _gat_UA-135916138-1=1; _gat_UA-135916138-2=1; pzqXflQLz5wTSg5443T=1NuKrkgrrMeBpUE2EOo7e84FAr_28dQ41LDN2hbM2Nc.JHimgbO1IH0uNWq9Agg0slWStN8p6HRMCNTWAxU6FlRsdNuYTPYWmZxZ0xnJcCvTjHxnddFbZrGlC8SeRK8DwgSGLNJbWCuexmSM6lY.ouh1yJnYMyyb3L5HMMk31ptj9jdgJ1PsPDbiJU5NuphOkWDBR8ppFNHUiBTRPOggF03.QVUE91i2e0BIULQxz0vhxJd_JAscu3QUoa8Rfmh2_FbcNX.GdI1m34wKzHEKsQjIRTRQkexVrw9EseyCvhJW6CA; BIGipServer~RTDS~POOL_RTDS_9080=!dyvkNbgNymWm0tWnphmIOaVF7qu+1OLDrGM2G0HEL8jogNWdapthYTzcWDOCOibvz7CjeqIHZvbdxA==",
#         "Host": "www.ctbcbank.com",
#         "Origin": "https://www.ctbcbank.com",
#         "Referer": "https://www.ctbcbank.com/twrbo/zh_tw/index/h_locate_index/h_locate_inquiry.html",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-origin",
#         "x-auth-token": "2f6dafdc-154a-4108-b23a-9c3b6374514a",
#         "X-Channel-Id": "EBMW_WEB_O",
#         "X-Requested-With": "MFPAsync"
#     },#params放的是網址上面問號以後的參數，美個參數用&分隔
#     params = {
#         "IIhfvu":"1qxEbjcIbnoSC5n4BtenF6rl6Lq4yKb2TrZ6cPQmcqgTjb0MIHRWgbizi2__6pcj0zCBzq9HAbOmpqH16GzNezOJ3zskQVFNRx0Zq3wro3gsMl9mIpBJsuzhb0EKr_rKM.8CEVOvy3E1IYViF8Aix5RzouYHAkKTI6HPqDp60U5aBxiNWN8wMS8.tdyiG4sbSvC7YFh5cTwGQXGXRW7n_XXaIdCwGA7HQgK0qRkk3uJJItmC1H5h_smEpGlKF9JJuNjAZg7xddyzQOqhbTV4W0bs92Pu6mDtIIxjrzt7STbimpxc6v2cDW3dzWQaeYobYsp5w1FwJYw5Jwx.DJX2brCfmnH_J3w6bCzWqKExzfeNj9V5NSVxoUUAk57cSEbwTPCFSLEHib5u_GzfFFSWNng7nbwko27JGSiW"
#     },#從chrome裡面的Response headers找
#     data = {
#         "deviceIxd": "none",
#         "trackingIxd": "d6b0f2c2-4afc-4d1a-8d18-b172728637bf",
#         "txnIxd": "76f6126a-76c4-4a1a-9f74-ed0128fe95bd",
#         "model": "chrome",
#         "platform": "windows7",
#         "ersion": "6.1",
#         "runtime": "chrome",
#         "runtimeVer": 80,
#         "network": "unknown",
#         "appVer": "5.01.18",
#         "clientNo": "1586583845836",
#         "clientTime": 1586583850081,
#         "token": "7a85de18-bae5-4bf5-bc60-03eb8eb16d6b",
#         "locale": "zh_TW",
#         "fromSys": "1",
#         "seed": "20200411133940891000389520621406",
#         "deviceToken": "none",
#         "resource": "/twrbo-general/qu002/010",
#         "rqData": {}
#     }
# )
# print(u8.status_code) #顯示 400 表示伺服器不理會我的問題

# #華南銀行
# import requests, codecs
#
# u9 = requests.get(
#     "https://www.hncb.com.tw/hncb/XML/Taiwan.xml",
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36}",
#         "Sec-Fetch-Dest": "empty",
#         "Referer": "https://www.hncb.com.tw/wps/portal/HNCB/branches"}
#
# )
# print(u9.status_code) #確定可以存取
# with codecs.open("2020.04.11.xml", "w", "UTF-8") as f:
#     f.write(u9.text)

# #beautifulsoup函式解析讀取出來是網頁資訊
# from bs4 import BeautifulSoup
# import requests, codecs
# u10 = requests.get(
#     "https://www.taiwan.net.tw/m1.aspx",
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#         "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#         "Cookie": "ASP.NET_SessionId=pxqsxdgpvft3zelzrdxxxcsa; TwSessID=; _ga=GA1.3.1470569981.1586590876; _gid=GA1.3.1340334767.1586590876; _gat_gtag_UA_5278761_9=1",
#     },
#     params= {
#         "sNo":"0001001"
#     })
# b1 = BeautifulSoup(u10.text, "html.parser")
# # a1 = b1.find_all("a", {"class":"columnBlock-title"}) #抓標題
# # for i in a1:
# #     print(i.text)
# # a2 = b1.find_all("span", {"class":"date"})
# # for i in a2:
# #     print(i.text)
#
# #把每一頁都存檔
# fn =1
# a3 = b1.find_all("div", {"class":"columnBlock-info"})
# for i in a3:
#     title = i.find("a", {"class":"columnBlock-title"})
#     date = i.find("span", {"class":"date"})
#     if title.attrs["href"].find("m1.aspx") != -1:
#         r2 = requests.get(
#             "https://www.taiwan.net.tw/" + title.attrs["href"],
#             headers={
#                 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#                 "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#                 "Cookie": "ASP.NET_SessionId=pxqsxdgpvft3zelzrdxxxcsa; TwSessID=; _ga=GA1.3.1470569981.1586590876; _gid=GA1.3.1340334767.1586590876",
#             }
#         )
#         b2 = BeautifulSoup(r2.text, "html.parser")
#         with codecs.open("html/"+ str(f(n))+ ".txt", "w", "UTF-8") as f:
#             f.write(title.text +"\r\n")
#             f.write(date.text + "\r\n\r\n")
#             f.write(b2.find("div", {"class":"content"}).find("p").text)
#             fn += 1

#104網頁查詢
import requests, prettytable
from bs4 import BeautifulSoup
keyword = input("請輸入要搜尋的關鍵字:")
t = prettytable.PrettyTable(["公司名稱", "職缺名稱"], encoding="UTF-8")
for page in range(1, 3, 1):
    u11 = requests.get(
        "https://www.104.com.tw/jobs/search/",
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        },
        params= {
            "keyword":keyword,
            "order":1,
            "jobsource":"2018indexpoc",
            "ro": 0,
            "asc":0,
            "page":page,
            "mode":"s"
                 })
    b1 = BeautifulSoup(u11.text, "html.parser")
    a1 = b1.find_all("article", {"class":"job-list-item"})
    for i in a1:
        t.add_row([i.attrs["data-cust-name"], i.attrs["data-job-name"]])
print(t)