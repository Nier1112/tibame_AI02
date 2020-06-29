# enumerate 可以將開啟的 list 用 tuple的方式表現
mylist = [{"a":1}, {"b":2}, {"c":3}, {"d":4}]

print(mylist)

for d in mylist: #直接列印出個別的文字
    print(d)

for i in enumerate(mylist): #將mylist變成有索引的數值
    print(i)
a = list(enumerate(mylist))
print(a)

for i, d in enumerate(mylist):
    print(f"第{i}個標籤是{d}")


# with open("./data.txt", "a", encoding="UTF-8") as file:
#     userinput = input("請輸入文字: ")
#     file.write(userinput+"\n")
#     print(file)

