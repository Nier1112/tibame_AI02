import requests

u = requests.get("http://teaching.bo-yuan.net/test/requests/")
print(u.text) #編碼是ISO-8859-1

#改成編碼 UTF-8
u = requests.get("http://teaching.bo-yuan.net/test/requests/")
u.encoding="UTF-8" #改成編碼 UTF-8
print(u.text) #說明缺少參數 action

# 增加參數action進去
u = requests.get("http://teaching.bo-yuan.net/test/requests/",
                 params={
                     "action":"123"
                 })
u.encoding="UTF-8"
print(u.text) #說明需要DELETE的操作

#把get換成DELETE
u = requests.delete("http://teaching.bo-yuan.net/test/requests/",
                 params={
                     "action":"123"
                 })
u.encoding="UTF-8"
print(u.text) #缺少資料id

#增加資料id進去
u = requests.delete("http://teaching.bo-yuan.net/test/requests/",
                 params={
                     "action":"123",


                 },
                    data = {"id":"1234"}
                )
u.encoding="UTF-8"
print(u.text) #說明要用PUT操作

#把delete換成put
u = requests.put("http://teaching.bo-yuan.net/test/requests/",
                 params={
                     "action":"123",


                 },
                    data = {"id":"1234"}
                )
u.encoding="UTF-8"
print(u.text) #說明需要更新資料name

#更新資料name
u = requests.patch("http://teaching.bo-yuan.net/test/requests/",
                 params={
                     "action":"123",


                 },
                    data = {"id":"1234", "name":"1234"}

                )
u.encoding="UTF-8"
print(u.text) #說明需要patch的資料是 address

#把address放進去
u = requests.patch("http://teaching.bo-yuan.net/test/requests/",
                 params={
                     "action":"123",


                 },
                    data = {"id":"1234", "name":"1234", "address":"123"}

                )
u.encoding="UTF-8"
print(u.text) #說明最後post一筆資料

#把patch換成post
u = requests.post("http://teaching.bo-yuan.net/test/requests/",
                 params={
                     "action":"123",


                 },
                    data = {"id":"1234", "name":"1234", "address":"123"}

                )
u.encoding="UTF-8"
print(u.text) #Answer
