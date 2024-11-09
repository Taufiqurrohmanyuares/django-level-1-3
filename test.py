# print ("Hello World !")

# x = 5
# y = "john"
# print (type(x))
# print (type(y))

# import re
# string = "Hi this Python for you"
# pattern = "[a-m]"
# result = re.findall(pattern, string)
# print(result)

# var1= 1
# var1 -= 1
# var1 = int(var1)
# print()

# print(bool(var1))

# scope local
# x = 25

# def my_func():
#     global x
#     x = 50
#     print("inside function x is ", x)

# my_func()
# print("outside function x is ", x)

# scope  enclosing function locals

# name = "global name"

# def my_func():
#     name = "Taufiq"

#     def hello_func():
#         print("hello", name)

#     hello_func()

# my_func()
# print(name)

# scope built in
# mylist = [1, 2, 3]
# print( "before", len(mylist))

# def len(x):
#     return "hahaha"

# print("after", len(mylist))

# OOP
# mylist = [1, 2, 3]
# mylist
# print(type(1))

# membuat class
# class myclass:
#   x = 100
#   def hello(self): 
#     print("hello")

# print(myclass)
# <class '__main__.myclass'> : modulnya ini

# myobject = myclass()
# print(myobject.x)

# myobject.x = 50
# print(myobject.x)

# myclass.hello()
# myobject.hello()

# contoh 2

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # print("parent init")

#     def __str__(self):
#         return "name:" + self.name + "and age:" + str(self.name)

#     def selfintro(self):
#         print("hello my name is", self.name)
# pewarisan inheritance
# class anak
# class student(person):
#     def __init__(self, name, age, currclass):
#         super().__init__( name, age)
#         # print("child init")
#         self.currclass = currclass

#     def selfintro(self):
#         print ("Hello! my name is", self.name, " and I am in", self.currclass, "grade")


#     def showjob(self):
#         print("I am sdtudent")
# sx = student("fina ", 6, 1)
# sx.showjob()
# print(sx.name)
# print(sx.age)
# print(sx)
# sx.selfintro()


# x = person ("dewi", 17)

# del x.age
# print(x)
# print(x.name)
# print(x.age)
# x.selfintro()

# Polimorfisme
class car :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive !")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

# craate a car class
#objecnya
car1 = car("Toyota", "avanza")  
#Create a Boat Class
boat1 = Boat("viking", "Billfish 380")
#create a Plane class
Plane1 = Plane("boeing", "777x")

for x in (car1, boat1, Plane1):
    x.move()