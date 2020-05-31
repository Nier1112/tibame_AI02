# 變數 variable, 開出一個區塊儲存數值用
age = 18 #電腦裏面有一個區塊，叫做age, 裡面儲存了18這個數字
age += 1 # 相當於 age = age + 1
name = "Bob" #雙引號或是單引號，是告訴電腦裏面是字，如果沒有就視為變數 上面沒有定義時 就會出錯
print(name + "" + str(age)+ "歲")

# 快捷鍵： ctrl + / 可以多列註解 再按一次回覆

fp = 1.234
print(round(fp, 1)) # round 四捨五入功能，1指小數點後一位，2指小數點後2位

#布林值, 寫作技巧，用底線來分隔字體意思，也可以用駝峰式寫法 isDoorOpen, 一般python都用 is_door_open
is_door_open = True

#關係運算子 >  <  ==
print( 6 > 10 )
print(6 > 3 )
print(6 == 6)

#邏輯運算子 可以把兩個條件合併成一個條件
print(is_door_open and 6 < 5) # 表示 is_ door_open 是 True 跟 6 > 5 都是True時 才會是 True, 兩個條件都成立時才會成立
print(is_door_open or 6 < 5) #表示其中一個成立，條件就成立

# #今天課程開始：資料邏輯處理 split 切割資料!
data = "[伙食]2019/11/18 $50-早餐"
# segment_1 = data.split("]")[0]
# segment_2 = data.split("]")[0].split("[")
# tag = segment_2[1]
# print(tag)

print(data.split("-")[0]) # 從字串裏面的 - 這個地方切衣刀，左邊的[伙食]2019/11/18 $50 是[0]的位子， 早餐 是[1]的位子
print(data.split("-")[0].split(" ")[1]) #取左邊的東西用空白鍵再切一次， 取右邊資訊就是 $50
print(data.split(" ")[0].split("]")[1]) #擷取日期
# ctrl + alt + l 可以自動排版
s = "HelloWorld!"
print(s.split("W")[0])

#step 2：讀取全部資料
#相對路徑開啟檔案 ./表示相對路徑，要在與pybasic.py同一個資料夾下
f = open("./CostData.txt", encoding = "UTF-8")
#絕對路徑開啟檔案 # \表示絕對路徑，可以開啟其他磁區的檔案 r 表示後面字元不進行轉義,r後面的 \t 就不會分行的意思
#f = open(r"C:\Users\niel\PycharmProjects\20200324Basic\CostData.txt", encoding="UTF-8")
#file_data = f.read()
file_data_list = f.readlines() #使用readlines 會把讀取後的變成list，每一行放進去list裏面
print(file_data_list)
for d in file_data_list:
    if d != "\n":  #當d 不是跑到換行時，執行下面的程式碼
        d = d.strip() #把最尾端的空白或是換行符號消除, 包含空格、換行(\n)和制表符號(\t)由於 strip()是 copy 一個新串列，需要放置到 variable裏面
        segment_1 = d.split("]")
        segment_2 = segment_1[0].split("[")
        tag = segment_2[1]
        segment_3 = segment_1[1].split(" $")
        data = segment_3[0]
        segment_4 = segment_3[0].split("-")
        cost = segment_4[0]
        print("標籤：{} 日期：{} 花費：{}".format(tag, data, cost))
        print(f"標籤：{tag} 日期：{data} 花費：{cost}")

#定義函式，可以把文字丟進去函式，拿到tag, data, cost
def get_tag_data_cost(text):
    segment_1 = d.split("]")
    segment_2 = segment_1[0].split("[")
    tag = segment_2[1] #切割成只有標籤
    segment_3 = segment_1[1].split(" $")
    data = segment_3[0] #切割成只有日期
    segment_4 = segment_3[1].split("-")
    cost = segment_4[0] #切割成只有花費
    return tag, data, cost

data = "[伙食]2019/11/18 $50-早餐"
tag, data, cost = get_tag_data_cost(data)
print(data)
print(tag)
print(cost)

f = open(r"C:\Users\niel\PycharmProjects\20200324Basic\CostData.txt", encoding="UTF-8")
file_data_list = f.readlines()

#轉化成 list理面是一本一本字典，為了讓伙食, 2019/11/18, $50 這些有個key值可以後續拿取來用
dict_list = []
for d in file_data_list:
    if d != "\n":
        tag, data, cost = get_tag_data_cost(d)
        dict_list.append({"tag": tag, "data": data, "cost": cost}) #把tag, data, cost 放入字典再放入list內
print(dict_list)
print(dict_list[2]["tag"]) # dict_list[1]["tag"] 字典拿取tag這個key值的value
#以上資料整理完成!!!可以開始使用~

#查詢資料，查總伙食花費
total_food_cost = 0
for i in dict_list: # i 這個變數會在 dict_list 裡面跑, 跑一次是一本字典，
    if i["tag"] == "伙食": # i["tag"] 是字典的用法，拿取tag這個標籤的key值， 如果標籤tag是伙食的話就跑下面程式
        total_food_cost += int(i["cost"])

print(total_food_cost)

#查詢 11/20 號及伙食的總花費
total_1120 = 0
for i in dict_list:
    if i["data"] == "2019/11/20" and i["tag"] == "伙食":
        total_1120 += int(i["cost"])

print(total_1120)

#查詢11/20號的總花費
total_1120_ = 0
for i in dict_list:
    if i["data"] =="2019/11/20":
        total_1120_ += int(i["cost"])
print(total_1120_)
