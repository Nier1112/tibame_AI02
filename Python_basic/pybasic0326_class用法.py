# class 類別
class Person:
    def __init__(self, name, age): #python裏面，只有要有底線的都是系統自訂函式，想像成是拿出一張空白設計圖
        self.name = name #設計圖上面的name這個屬性
        self.age = age   #設計圖上面的age這個屬性
    def greet(self): #做一些動作,這個動作會列印出下面東西"I am XX OO old"
        print(f"I am {self.name} {self.age} old")

    def change_name(self, new_name): #這個動作會更改名字
        self.name = new_name

#繼承上面的類別
class ChinesePerson(Person): #chineseperson 繼承 Person的類別，Person上的資訊都可以用
    def __init__(self, name, age, zodiac_sign): #ChinesePerson這張設計圖
        super().__init__(name, age) #super() 是繼承上面Person class裡面的初始化屬性，也就是某些屬性跟Person相同的部分直接拿來用就不用在血一次
        self.zodiac_sign = zodiac_sign #ChinesePerson這張設計圖自己的屬性
    # def __init__(self,name, age, zodiac_sign):
    #     self.name = name
    #     self.age = age
    #     self.zodiac_sign = zodiac_sign
#    pass # 甚麼事情都不要做 就寫 PASS
    def greet(self):
        print(f"我是 {self.name} {self.age} 歲, 生肖是{self.zodiac_sign}")


p1 = Person("Bob", 18) #把p1這些東西 bob, 18的屬性放入 Person這個設計圖內
p2 = Person("nier", 20)
print(p1)
print(p1.name, p1.age)
print(p2.name, p2.age)
p1.greet()
p2.greet()
p2.change_name("kevin")
print(p2.name, p2.age)

p3 = ChinesePerson("張三", 40, "鼠")
print(p3.greet())



