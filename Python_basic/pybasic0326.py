# class 類別
class Person:
    def __init__(self, name, age): #python裏面，只有要有底線的都是系統自訂函式
        self.name = name #Person這個class的屬性，就是設計圖
        self.age = age
    def greet(self): #做一些動作
        print(f"I am {self.name} {self.age} old")

    def change_name(self, new_name):
        self.name = new_name

#繼承上面的類別
class ChinesePerson(Person): #chineseperson 繼承 Person的類別，Person上的資訊都可以用
    def __init__(self, name, age, zodiac_sign):
        super().__init__(name, age) #super() 是繼承上面Person class裡面的初始化屬性
        self.zodiac_sign = zodiac_sign
    # def __init__(self,name, age, zodiac_sign):
    #     self.name = name
    #     self.age = age
    #     self.zodiac_sign = zodiac_sign
#    pass # 甚麼事情都不要做 就寫 PASS
    def greet(self):
        print(f"我是 {self.name} {self.age} 歲, 生肖是{self.zodiac_sign}")


p1 = Person("Bob", 18)
p2 = Person("nier", 20)
print(p1.name, p1.age)
print(p2.name, p2.age)
p1.greet()
p2.greet()
p2.change_name("kevin")
print(p2.name, p2.age)

p3 = ChinesePerson("張三", 40, "鼠")
print(p3.greet())



