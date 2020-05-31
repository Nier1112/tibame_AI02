# input 方法
name = input("請輸入名字")
print(f"你好{name}")

# Error Handling:
try: #讓python試試看能不能執行

    num1 = input("請輸入數值1:  ")
    num2 = input("請輸入數值2:  ")
    print("兩個數字的總合為:  ", int(num1) + int(num2))
except: #如果上面的程式不能執行，就跑下面的程式
    print("請輸入數值!")

# 輸入 tag 之後 印出所有的tag 平均消費金額


class Receipt:
    def __init__(self, tag, date, cost, event):
        self.tag = tag
        self.date = date
        self.cost =cost
        self.event = event
    def print_info(self):
        print(f"[{self.tag}]{self.date} ${self.cost}-{self.event}")

def get_tag_date_cost_event(text: str):
    segment_1 = text.split("]")
    segment_2 = segment_1[0].split("[")
    tag = segment_2[1]
    segment_3 = segment_1[1].split(" $")
    date = segment_3[0]
    segment_4 = segment_3[1].split("-")
    cost = segment_4[0]
    event = "" # 沒有 event 的時候就是空
    # 有 event 資料
    if len(segment_4) > 1: #如果segment_4的資料有兩筆
        event = segment_4[1] #event的資料取右邊
    return tag, date, cost, event


f = open("./CostData.txt", encoding="utf8")
file_data_list = f.readlines()

tagin_ = input("請輸入標籤: ")