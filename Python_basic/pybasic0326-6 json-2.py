#找pm2.5濃度最高的時間.
import json

with open("./空氣品質小時值_桃園市_中壢站.json", encoding="UTF-8") as file:
    #print(file.read())
    object = json.loads(file.read())   # 開啟檔案之後，並非一個物件，json.loads() 把文字讀取成物件放入object裏面
    #print(object)

    max_con = 0                       #最大濃度直預設為 0
    max_moitorate = "" #空字串         #最大濃度直的字串先放空字串

    for i, d in enumerate(object):  #開啟成tuple
        #print(i, d)  #從 i 可以看出總共資料有幾筆 999是指 0-999 共 1,000筆
        #print(d["ItemEngName"]) #從這邊可以看出總共有幾個 ItemEngName 的種類
        if d["ItemEngName"] == "PM2.5":
            try:
                if float(d["Concentration"]) > max_con:
                    max_con = float(d["Concentration"])
                    max_moitorate = d["MonitorDate"]
            except:
                print(i, d)

    print(max_moitorate, max_con)
