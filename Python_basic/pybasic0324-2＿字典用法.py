my_list = ["a", "b", "c"]
my_list.append("d")
my_list.remove("a")
print(my_list)
print("list裡面的個數是：", len(my_list))
print(my_list.index("c")) #找出c 這個文字的位置

a: int = 10 # int 標籤 a 是 int型態
a = "bob" # 如果a被放入字元，python會用顏色提醒 這放入的並非數字

#字典：
score_dict = {"張三":90, "李四":50, "王武": 70}
score_dict["陳二"] = 98 #增加字典內容的用法
print(score_dict)
#字典刪除資訊
#pop
score_dict.pop("陳二")
print(score_dict)

#把score_list的這本字典放入dict_list，
dict_list = [score_dict]
print(dict_list)
print(dict_list[0]["李四"])

data2 = "[生活必需品]2019/11/19 $20"
#把data2弄成字典
dict2 = {"tag":"[生活必需品]", "date":"2019/11/19", "cost": 20}
print(dict2)

#把dict2 這本字典放入dict2_list的list裏面
dict2_list = [dict2]
print(dict2_list)
