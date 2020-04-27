#自動化系統操作，用python拿到資料夾內的所有內容
import os
#絕對路徑查詢內容 print(os.listdir("C:\Program Files"))
#相對路徑查詢內容 print(os.listdir("./")
# os.listdir 一定要是資料夾的路徑，檔案無效
#兩個點是查詢上一層的意思
#print(os.listdir("../"))

#如何拿到物件的資料夾路徑
#file_path = "C:\Program Files\Microsoft Security Client\Drivers"
#print(os.path.dirname(file_path))
#拿到物件路徑之後，再列出裏面所有的資訊
#print(os.listdir(os.path.dirname(file_path)))

#檢查物件或是資料夾是否存在
#print(os.path.exists("./HWQ2_05.csv")) # HWQ2_05 存在會出現True
#print(os.path.exists("./abcd.txt")) #abcd.txt不存在的例子 會出現false
#print(os.path.exists("./venv/")) #檢查venv這個資料夾存不存在 會出現True

#創建一個資料夾 資料夾名稱叫做 frompython
#os.mkdir("./frompython/")

#寫file時，檢查資料夾是否存在，若沒有就創建一個資料夾
"""
1.拿到檔案資料夾路徑  用 dirname, 會自動去除檔案名稱, 只留下資料夾路徑
2.檢查資料夾路徑是否存在 用 if os.path.exist
3.如果沒有就創一個資料夾
"""
# file_path = "./data123/file.txt"
# file_dir_path = os.path.dirname(file_path)
# if not os.path.exists(file_dir_path):
#     os.mkdir(file_dir_path)


# #檢察一個檔案的資料夾路徑，看是否存在，如果不存在 開啟一個檔名
# file_path ="./data123/file.txt"             # 因為 ""裡面是文字，所以我們現在知道有一個檔案叫做 file.txt 放入 file_path 這個 variable 裡面
# file_dir_path = os.path.dirname(file_path)  #os.path.dirname(file_path) 是把 ./data123資料夾的路徑找出來放入 file_dir_path 裡面, 會自動去掉文件名稱
# if not os.path.exists(file_dir_path):       # os.path.exists(file_dir_path) 意思是用dirname抓到的路徑下的 ./data123存在嗎? 如果不存在執行下面的程式
#     os.mkdir(file_dir_path)                 # 製作一個資料夾名稱叫做 data123
file_path = "./data123/file.txt"
file_dir_path = os.path.dirname(file_path)

index = 1
while os.path.exists(file_path):
    file_path = f"./data123/file-{index}.txt"
    index += 1

with open(file_path, "w", encoding="utf8") as file:
    pass
# #如果有相同檔名，開啟一個檔名 file-1.txt, 如果file-1.txt有了 開啟一個 file-2.txt
# index = 1
# while os.path.exists(file_path):
#     index += 1
#     file_path = f"./data123/file-{index}.txt"
#
# with open("./data123/file.txt", "w", encoding="utf8") as file:   #製作一個txt檔案的方法, 注意!!with open只能製作檔案, 不能製作資料夾!!!!
#     pass


#重新命名檔案, 資料夾名稱都一樣用法
#os.rename("./data123/file.txt", "./data123/file-1.txt")
#os.rename("./data123/", "./data1234")

#剪下貼上-->就是更改檔名到不同資料夾
#os.rename("./data1234/file-1.txt", "./file.txt")

#刪除檔案, 刪除之後不會再資源回收桶，消失在電腦硬碟裡面
#os.remove("./file.txt")

#刪除資料夾, 若資料夾裏面有東西，會警示, 資料夾清空才能刪除
#os.rmdir("./data1234")

# #讀取資料夾內檔案
# #改名字成-1, -2, -3
# os.mkdir("./data123/")
# i = 0
# for filename in os.listdir("./data123/"):
#     print(filename)
#     i += 1
#     os.rename("./data123/" + filename, f"./data123/data-{i}.txt") # rename 要加上路徑 ./data123 +filename左邊是舊的名字, 逗號右邊是新的名字

#找到特定開頭的檔案
# import glob
# print(glob.glob("Hw*")) #開頭前兩個字是HW的, *是指後面是甚麼全部撈出來
#
# #找到特定結尾, 也就是副檔名的檔案, *.csv 指前面不管甚麼字，只要是副檔名是csv都撈出來
# print(glob.glob("*.csv"))
# print(glob.glob("*.txt"))
#
# #找到特定開頭跟結尾的檔案
# print(glob.glob("hw*.py"))


