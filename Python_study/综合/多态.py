class Animal:
    def speak(self):
        pass  # 父类确定方法  子类觉得方法实现


# 顶层设计


#  方法体空实现  就是抽象类
class Dog:
    def speak(Animal):  # 方法
        print("wwwwww")


class Cat:
    def speak(Animal):  # 方法
        print("mmmmmmmmmmmm")


def make_noise(animal: Animal):  # 这个是函数
    animal.speak()


dog = Dog()  # 实例化  Dog() 就是对象  把值赋给dog
# Dog类的类对象
cat = Cat()  # 实例化
# Cat类的类对象
make_noise(dog)
make_noise(cat)
# 给函数传不同的对象
