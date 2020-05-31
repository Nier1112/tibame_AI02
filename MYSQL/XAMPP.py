import pymysql

#連結php系統資料庫
link = pymysql.connect(
    host = "localhost", #同一台電腦就是 localhost
    user = "root",      #預設值都是root
    passwd ="",         #預設值是空值 也就是沒有密碼
    db = "member",      #連結到　member這個資料庫
    charset = "utf8"    #編碼
)

#取得指令操作變數: link 是跟sql系統連接的部分， link.cursor()是表示連結之後顯示游標點並放入 con 這個 variable 裡面
con = link.cursor()

#新增資訊
infor = {
    "nam": input("請輸入新增名字:"),
    "bir": input("請輸入新增生日:"),
    "add": input("請輸入新增地址:"),
    "hobby": input("請輸入新增嗜好:")
}
#將上述輸入文字整理成sql可以讀懂的指令, %s是指sql之外來的指令，
con.execute(
    "INSERT INTO `member` (`name`, `birthday`, `address`, `hobby`) " +
    "VALUES(%(nam)s,%(bir)s,%(add)s,%(hobby)s);",infor)

# #修改資訊
# modify = {
#     "id":  input("請輸入要修改資料的id:"),
#     "nam": input("請輸入名字:"),
#     "bir": input("請輸入生日:"),
#     "add": input("請輸入地址:"),
#     "hob": input("請輸入嗜好:")
# }
#
# con.execute(
#     "UPDATE `member` SET "+
#     "`name`=%(nam)s, `birthday`=%(bir)s, `address`=%(add)s, `hobby`=%(hob)s "+
#     "WHERE `id`=%(id)s;",modify)

# delmem = {
#     "id": input("請輸入要刪除資料的id:")
# }
# con.execute(
#     "DELETE FROM `member` WHERE `id`=%(id)s;",delmen)

# #將上述的資訊傳輸到aql系統
link.commit()
# #關閉連線
link.close()

#搜尋指令, fetchall() 在python裡面找到資訊後會tuple格式表示，一個tuple代表一筆資料
# con.execute("SELECT * FROM member")
# rows = con.fetchall()
# for d in rows:
#     print(d)
#
# #搜尋指令, fetchone()
# con.execute("SELECT * FROM member WHERE `id`=4")
# rows= con.fetchone()
# print(rows)
# print(rows[1])