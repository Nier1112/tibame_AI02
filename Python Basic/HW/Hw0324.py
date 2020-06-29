#找出早餐當中花費最多的帳目
"""
1.整理 data
2.列出伙食中，早餐項目的花費
3.找出花費最大的
"""
#開啟 CostData 檔案，並用 list 型式表示
f= open("./CostData.txt", encoding="UTF-8")
file_data_list = f.readlines()
print(file_data_list)

#切割文字，整理檔案成只有伙食費及早餐項目
for i in file_data_list:
    if i != "\n":
        i = i.strip()
        segment_1 = i.split("]")
        segment_2 = segment_1[0].split("[")
        tag = segment_2[1]
        if tag == "伙食":
            segment_3 = segment_1[1].split(" $")
            segment_4 = segment_3[1].split("-")
            date = segment_3[0]
            cost = segment_4[0]
            time_1 = segment_4[1]
            if time_1 == "早餐":
                print("項目:{} 日期:{} 花費:{} 時間:{}".format(tag, date, cost, time_1))

#把整理過後的資訊以字典方式放入下面dict_list
dict_list = []
for i in file_data_list:
    if i != "\n":
        i = i.strip()
        segment_1 = i.split("]")
        segment_2 = segment_1[0].split("[")
        tag = segment_2[1]
        if tag == "伙食":
            segment_3 = segment_1[1].split(" $")
            segment_4 = segment_3[1].split("-")
            date = segment_3[0]
            cost = segment_4[0]
            time_1 = segment_4[1]
            if time_1 == "早餐":
                dict_list.append({"tag":tag, "date":date, "cost":cost, "time":time_1})
print(dict_list)

#把字典內 cost 的　value 放入 max_list內，以max函式得知最大值為 100
maxcost_list = []
for i in dict_list:
    maxcost_list.append(int(i["cost"]))
print(max(maxcost_list))

#列印出當 cost 最大值為 100 時候的整本字典內容
for d in dict_list:
    if d["cost"] == "100":
        print(d)






