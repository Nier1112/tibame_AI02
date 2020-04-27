#製作5->新增會員電話, 6->刪除會員電話
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

while True:
    if cmd == "0":
        break
    elif cmd =="1":
        t = prettytable.PrettyTable(["id", "name", "birthday", "address", "tel"], encoding="utf8")
        # LEFT JOIN是以member資料庫為主要顯示, 並且member資料庫的id連結tel資料庫的member_id
        c.execute("SELECT * FROM `member` LEFT JOIN `tel` ON `member`.`id`= `tel`.`member_id`")
        n = c.rowcount #算出總共有幾筆資訊
        for i in range(0,n):
            r = c.fetchone()
            t.add_row([str(r[0]), r[1], r[2], r[3],r[6]])
            t.align["name"]="l"
            t.align["birthday"]="l"
            t.align["address"]="l"
            t.align["tel"]="l"
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
        par = {"id":input("輸入要刪除的id:")}
        c.execute("DELETE FROM `member` WHERE `id`=%(id)s", par)
        link.commit()
    elif cmd =="5":
        t = prettytable.PrettyTable(["id", "name", "birthday", "address", "tel"], encoding="utf8")
        c.execute("SELECT * FROM `member` LEFT JOIN `tel` ON `member`.`id`= `tel`.`tel`")
        n =c.rowcount
        for i in range(0,n):
            r = c.fetchone()
            t.add_row([str(r[0]), r[1], r[2], r[3],r[4]])
            t.align["name"]="l"
            t.align["birthday"]="l"
            t.align["address"]="l"
            t.align["tel"]="l"
        print(t)
        num = input("選擇要添加的會員編號:")
        ph = input("請輸入電話號碼:")
        c.execute(
            "INSERT INTO `tel`(`member_id`, `tel`) " +
            "VALUES(%s,%s)", (num, ph))  # 讀取外面資訊到%s裏面時的格式
        link.commit()
    elif cmd =="6":
        t = prettytable.PrettyTable(["id", "name", "birthday", "address", "tel"], encoding="utf8")
        c.execute("SELECT * FROM `member` LEFT JOIN `tel` ON `member`.`id`= `tel`.`member_id`")
        n = c.rowcount
        for i in range(0, n):
            r = c.fetchone()
            t.add_row([str(r[0]), r[1], r[2], r[3], r[6]])
            t.align["name"] = "l"
            t.align["birthday"] = "l"
            t.align["address"] = "l"
            t.align["tel"] = "l"
        print(t)
        num = input("選擇要刪除的會員編號:")
        t2 = prettytable.PrettyTable(["id", "tel"])
        c.execute("SELECT * FROM `tel` WHERE `member_id`=%s", (num)) #由於member_id =id 所以當輸入id時可由member_id把所有資訊撈出來
        n = c.rowcount
        for i in range(0, n):
            r = c.fetchone()
            t2.add_row([r[0], r[2]])
        print(t2)
        #刪除動作
        ph = input("選擇要刪除的電話號碼編號:")
        c.execute("DELETE `tel` FROM `tel` WHERE `id`=%s", (ph))
        link.commit()

    print("(0) 離開程式:")
    print("(1) 顯示會員列表:")
    print("(2) 新增會員資料:")
    print("(3) 更新會員資料:")
    print("(4) 刪除會員資料:")
    print("(5) 新增會員電話:")
    print("(6) 刪除會員電話:")

    cmd =input("指令")
    os.system("cls")

link.close()