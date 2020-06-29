import csv

#輸入單位名稱
search_in = input("請輸入單位名稱：")
search_result = []
count = 0

#開啟檔案並將搜尋名稱資料放入 serarch_result 的list裏面
with open("./opendata_requests.csv", encoding="UTF-8") as file:
    reader = csv.reader(file)

    try:
        for i, d in enumerate(reader):
            if i != 0 and d[0] == search_in:
                search_result.append(d)
                count += 1
                #print(i, d)
        print("總共", count, "筆資料")

    except:
        print(i, d)

#寫入所搜尋的名稱資訊至新檔案 HWQ2_05.csv 裏面
with open("HWQ2_05.csv", "w", encoding="UTF-8", newline="") as hwfile:
    writer = csv.writer(hwfile)
    writer.writerows(search_result)