# class ThisIsMyFirstClass:
#     name="Sakshi"
#     age=20
#     # pass  #placeholder for storing a place--->it does nothing 

#     def getName(self):
#         print(self.name)
#         # pass

# firstObject=ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getName()
# print(firstObject.name)

# class Student:
#     def __init__(self):  #init is constructor
#         self.name=""
#         self.age=0
#         self.gender=""
#         self.grade=""

# mayur=Student()   #Object of class
# print(mayur)

# mayur.name="Sakshi"
# mayur.age=20
# mayur.gender="Male"
# mayur.grade="10th"

# print(mayur.name)
# print(mayur.age)
# print(mayur.gender)
# print(mayur.grade)

# class Student:
#     def __init__(self,name,age,gender,grade):  #init is constructor
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.grade=grade

#     def printDetails(self):
#         print("name : ",self.name)
#         print("age : ",self.age)
#         print("gender : ",self.gender)
#         print("grade : ",self.grade)

# mayur=Student("Sakshi",20,"Male","10th")   #Object of class
# print(mayur)

# mayur.printDetails()
# print(mayur.name)
# print(mayur.age)
# print(mayur.gender)
# print(mayur.grade)


#__dict__ is a special dictionary
# class ExampleClass:
#     def __init__(self,val = 1):
#         self.first=val
    
#     def set_second(self,val):
#         self.second = val

# example_object_1=ExampleClass()
# example_object_2=ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3=ExampleClass(4)
# example_object_3.third=5

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

#Self
# class Classys:
#     def method(self):
#         print("method")

# obj=Classys()
# obj.method()

# class Classy:
#     def method(self,par):
#         print("method",par)

# obj=Classy()
# obj.method(1)

#Class variable and Instance variable
# class Classy:
#     varia=2
#     def method(self):
#         print(self.varia,self.var)

# obj=Classy()
# obj.var=3
# obj.method()

class Star:
    def __init__(self,name,galaxy):
        self.name=name
        self.galaxy=galaxy

sun= Star("Sun","Milky way")
print(sun)

class Star:
    def __init__(self,name,galaxy):
        self.name=name
        self.galaxy=galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy

sun= Star("Sun","Milky way")
print(sun)

#Two-level Inheritance example
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle,LandVehicle,TrackedVehicle]:
    for cls2 in [Vehicle,LandVehicle,TrackedVehicle]:
        print(issubclass(cls1,cls2), end="\t")
    print()

print("---------inheriting parent class in child class---------------")
class Super:
    supVar=1

class Sub(Super):
    subVar = 2

obj=Sub()
print(obj.subVar)
print(obj.supVar)

#super() Keyword
class Super:
    def __init__(self):
        self.supVar=11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 21

obj=Sub()
print(obj.subVar)
print(obj.supVar)

#Multi-Level or Three-Level Inheritance
class Level1:
    variable_1=100
    def __init__(self):
        self.var_1=101
    def fun_1(self):
        return 102
    
class Level2(Level1):
    variable_2=200
    def __init__(self):
        super().__init__()
        self.var_2=201
    def fun_2(self):
        return 202
    
class Level3(Level2):
    variable_3=300
    def __init__(self):
        super().__init__()
        self.var_3=301
    def fun_3(self):
        return 302
    
obj=Level3()
print(obj.variable_1,obj.var_1,obj.fun_1())
print(obj.variable_2,obj.var_2,obj.fun_2())
print(obj.variable_3,obj.var_3,obj.fun_3())







                                                                                                                                            





