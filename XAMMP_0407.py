#製作一個界面可以有顯示, 新增, 更新 和刪除會員資料
import pymysql, os, prettytable

os.system("cls")
setting_pass = input("請輸入資料庫的密碼:")
setting_port = input("請輸入資料庫的port:")

if setting_port =="":
    setting_port = 3306
else:
    setting_port = int(setting_port)

link = pymysql.connect(
    host ="localhost",
    user = "root",
    passwd = setting_pass,
    db="python_ai",
    charset ="utf8",
    port = setting_port
)

cmd = -1
os.system("cls") #cmd下清空畫面
c =link.cursor()

while True: #while True是為了讓輸入錯誤的時候，不會就此停下程式而會持續循環到表單繼續可以操作
    if cmd == "0":
        break
    elif cmd =="1":
        t = prettytable.PrettyTable(["id", "name", "birthday", "address"], encoding="utf8")
        c.execute("SELECT * FROM `member`")
        n = c.rowcount
        for i in range(0,n):
            r = c.fetchone()
            t.add_row([str(r[0]), r[1], r[2], r[3]])
            t.align["name"]="l"
            t.align["birthday"]="l"
            t.align["address"]="l"
        print(t)

    elif cmd == "2":
        name_ = input("請輸入name:")
        bir_ = input("請輸入birthday:")
        address_ = input("請輸入address:")

        c.execute(
            "INSERT INTO `member`(`name`, `birthday`, `address`) "+
            "VALUES(%s,%s,%s)",(name_, bir_, address_)  #讀取外面資訊到%s裏面時的格式
        )
        link.commit()
    elif cmd =="3":
        par = {
            "id":input("輸入你要修改資料的id:"),
            "nam":input("輸入名字:"),
            "bir":input("輸入生日:"),
            "add":input("輸入地址:")}
        c.execute(
            "UPDATE `member` SET "+
            "`id`=%(id)s, `name`=%(nam)s, `birthday`=%(bir)s, `address`=%(add)s WHERE `id`=%(id)s;"
            , par)
        link.commit()
    elif cmd =="4":
        par = {
            "id":input("輸入要刪除的id:")
        }
        c.execute(
            "DELETE FROM `member` WHERE `id`=%(id)s", par)
        link.commit()

    print("(0) 離開程式:")
    print("(1) 顯示會員列表:")
    print("(2) 新增會員資料:")
    print("(3) 更新會員資料:")
    print("(4) 刪除會員資料:")
    cmd =input("指令")
    os.system("cls")

link.close()