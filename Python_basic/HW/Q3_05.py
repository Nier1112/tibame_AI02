import csv

#106年1月資料:
with open("./自來水水質抽驗結果(106年1月).csv", "r", encoding="UTF-8") as file1:
    reader = csv.reader(file1)
    reader1_result = []
    count1 = 0
    for i, d in enumerate(reader):
        if i == 0:
         reader1_result.append(d)
        if i != 0 and d[4] == "平鎮區":
            reader1_result.append(d)
            count1 +=1
    print("106年1月總共有:", count1, "筆平鎮區資訊")

#106年2月資料
with open("./自來水水質抽驗結果(106年2月).csv", "r", encoding="UTF-8") as file2:
    reader = csv.reader(file2)
    count2 = 0
    for i, d in enumerate(reader):
        if i != 0 and d[4] == "平鎮區":
            reader1_result.append(d)
            count2 +=1
    print("106年2月總共有:", count2, "筆平鎮區資訊")

#106年3月資料
with open("./自來水水質抽驗結果(106年3月).csv", "r", encoding="UTF-8") as file3:
    reader = csv.reader(file3)
    count3 = 0
    for i, d in enumerate(reader):
        if i != 0 and d[4] == "平鎮區":
            reader1_result.append(d)
            count3 +=1
    print("106年３月總共有:", count3, "筆平鎮區資訊")
#將所有平鎮區域的資訊寫入 HW03_05.csv內
with open("./HW03_05.csv", "w", encoding="UTF-8", newline="") as file4:
    writer = csv.writer(file4)
    writer.writerows(reader1_result)

#用 function 處理, 重複的部分寫一次就好
result_list = []
def get_locationdata(file_path, location):
    with open(file_path, "r", encoding="UTF-8") as file:
        reader = csv.reader(file)
        reader_result = []
        for row in reader:
            if row[4] == location:
                reader_result.append(row)
    return reader1_result

result_list += get_locationdata("./自來水水質抽驗結果(106年1月).csv", "平鎮區")
result_list += get_locationdata("./自來水水質抽驗結果(106年2月).csv", "平鎮區")
result_list += get_locationdata("./自來水水質抽驗結果(106年3月).csv", "平鎮區")

with open(f"./平鎮區水質.csv", "w", encoding="utf8") as file:
    writer = csv.writer(file)
    for r in result_list:
        writer.writerow(r)