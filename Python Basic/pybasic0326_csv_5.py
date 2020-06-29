import csv

max_load_count = 0
max_load_name = 0

with open("opendata_requests.csv", encoding="UTF-8") as file:
    reader = csv.reader(file) # 用 csv.reader讀取出來的會是一個二維的 list 也就是[[xxx][ooo]....]
    #for i in reader:
    #    print(i)       #這邊可以打印出每一個i跑過去的 list內容
    for i, row in enumerate(reader):
        if i != 0: #第一筆不跑，因此當 i 是第一筆的時候不執行，i 是第二筆以後跑回圈, 如果要看前10筆數據， if i< 10:
            #print(i, row) #可以看出有 0-42867筆資料，共 42868筆資料
            count = int(row[3].replace(",", "")) #count下載次數的部分，也就是row的第3個index 把, 用空資料取代
            #print(i, row[3].replace(",", ""))    #記得! .replace這個方法不會改變原本資料，需要給他一個variable裝新資料
            if count > max_load_count:
                max_load_count = count
                max_load_name = row[1]
    print(max_load_count)
    print(f"最高下載次數為{max_load_count} 資料是 {max_load_name}")

with open("opendata_requests.csv", encoding="UTF-8") as file:
    d =  csv.DictReader(file)  #把 csv 讀取成字典
    for row in d:
        print(row["資料集名稱"])
        #print(row["資料集名稱"])


