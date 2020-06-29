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

# step2：讀取全部資料
f = open("./CostData.txt", encoding="utf8")
file_data_list = f.readlines()

receipt_list = []
for d in file_data_list:
    if d != "\n":
        d = d.strip()
        tag, date, cost, event = get_tag_date_cost_event(d)
        r = Receipt(tag, date, cost, event)
        receipt_list.append(r)

max_receipt:Receipt = receipt_list[0]

for r in receipt_list:
    if r.event == "早餐":
       if int(r.cost) > int(max_receipt.cost):
           max_receipt = r

max_receipt.print_info()
