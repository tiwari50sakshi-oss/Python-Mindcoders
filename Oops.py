# class ThisIsMyFirstClass:
#     name="Sakshi"
#     age=20
#     # pass  #placeholder for storing a place--->it does nothing 

#     def getName(self):
#         print(self.name)
#         print(self.age)
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

# class Star:
#     def __init__(self,name,galaxy):
#         self.name=name
#         self.galaxy=galaxy

# sun= Star("Sun","Milky way")
# print(sun)

# class Star:
#     def __init__(self,name,galaxy):
#         self.name=name
#         self.galaxy=galaxy

#     def __str__(self):
#         return self.name + ' in ' + self.galaxy

# sun= Star("Sun","Milky way")
# print(sun)

#Two-level Inheritance example
# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# for cls1 in [Vehicle,LandVehicle,TrackedVehicle]:
#     for cls2 in [Vehicle,LandVehicle,TrackedVehicle]:
#         print(issubclass(cls1,cls2), end="\t")
#     print()

# print("---------inheriting parent class in child class---------------")
# class Super:
#     supVar=1

# class Sub(Super):
#     subVar = 2

# obj=Sub()
# print(obj.subVar)
# print(obj.supVar)

# #super() Keyword
# class Super:
#     def __init__(self):
#         self.supVar=11

# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 21

# obj=Sub()
# print(obj.subVar)
# print(obj.supVar)

# #Multi-Level or Three-Level Inheritance
# class Level1:
#     variable_1=100
#     def __init__(self):
#         self.var_1=101
#     def fun_1(self):
#         return 102
    
# class Level2(Level1):
#     variable_2=200
#     def __init__(self):
#         super().__init__()
#         self.var_2=201
#     def fun_2(self):
#         return 202
    
# class Level3(Level2):
#     variable_3=300
#     def __init__(self):
#         super().__init__()
#         self.var_3=301
#     def fun_3(self):
#         return 302
    
# obj=Level3()
# print(obj.variable_1,obj.var_1,obj.fun_1())
# print(obj.variable_2,obj.var_2,obj.fun_2())
# print(obj.variable_3,obj.var_3,obj.fun_3())


#Class Variable
# class ExampleClass:
#     counter=0
#     def __init__(self,val=1):
#         self.__first=val
#         ExampleClass.counter+=1   

# example_object_1=ExampleClass()
# example_object_2=ExampleClass(2)
# example_object_3=ExampleClass(4)

# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)


#AttributeError which is predefined class in python 
# class ExampleClass:
    
#     def __init__(self,val):
#         if val%2!=0:
#             self.a=1
#         else:
#             self.b=1

# example_object=ExampleClass(12)
# print(example_object.a)
# print(example_object.b) #One out of two will give AttributeError if odd a=1,otherwise b=1


#Exception Handling---> Try-Except Example
# class ExampleClass:
#     def __init__(self,val):
#         if val%2!=0:
#             self.a=1
#         else:
#             self.b=1

# example_object=ExampleClass(1)
# try:
#     print("a = ",example_object.a)
# except AttributeError:
#     try:
#         print("b = ",example_object.b) 
#     except AttributeError:
#         print("The error has occurred! Silently passing")


#Has Attribute returns true or false---->hasattr
# class ExampleClass:
#     a=1
#     def __init__(self,val):
#         if val%2!=0:
#             self.a=1
#         else:
#             self.b=1

# example_object=ExampleClass(12)
# if hasattr(example_object,'a'):     
#     print("a = ",example_object.a)        # print(example_object.a)
#                                           # print(example_object.b)
# if hasattr(example_object,'b'):
#     print("b = ",example_object.b) 

# print(hasattr(ExampleClass,'b'))    #Checking the existence of property inside class thats why b returns false
# print(hasattr(ExampleClass,'a'))  

# class Python:
#     population=0   #Both are class variables
#     victims=1
#     def __init__(self):
#         self.venom=3           #Instance variable
#         self.__length=False    #Private variable--->throw error (Cause "__" is added to the variable name)--->Cannot be accessed outside this class but there's a twist but not suugested

# myObj=Python()
# print(myObj.population)
# print(myObj.victims)   
# print(myObj.venom)   
# # print(myObj.__length)    #AttributeError for both
# # print(myObj.length)
# print(myObj._Python__length)

# class Python:
#     def __init__(self):
#         self.constrictor=1

# version_2=Python()
# if hasattr(version_2,'constrictor'):
#     print("constrictor exists")


#Name Mangling in methods
# class Classy:
#     def visible(self):
#         print("visible")
    
#     def __hidden(self):    #Hidden method
#         print("hidden")

# obj=Classy()
# obj.visible()
# try: 
#     obj.__hidden            #this fails
# except:
#     print("failed")         #Output:failed
# obj._Classy__hidden()      #output:hidden----->access hidden method
 
# print(type(obj))           
# print(type(obj).__name__)   #__name__ returns the name of the class


#isinstance function
# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# my_vehicle=Vehicle()
# my_land_vehicle=LandVehicle()
# my_tracked_vehicle=TrackedVehicle()

# for cls1 in [my_vehicle,my_land_vehicle,my_tracked_vehicle]:
#     for cls2 in [Vehicle,LandVehicle,TrackedVehicle]:
#         print(isinstance(cls1,cls2), end="\t")
#     print()     #To get a new line


#is Operator
# class SampleClass:
#     def __init__(self,val):
#         self.val=val

# object_1=SampleClass(0)
# object_2=SampleClass(2)
# object_3=object_1
# object_3.val+=1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val,object_2.val,object_3.val)

# string_1="Mary had a little lamb"
# string_2="Mary had a little lamb"
# string_1+=" lamb"

# print(string_1==string_2,string_1 is string_2)

#Using str method and Super class
# class Super:
#     def __init__(self,name):
#         self.name=name

#     def __str__(self):
#         return "my name is " + self.name +"."

# class Sub(Super):
#     def __init__(self,name):
#         Super.__init__(self,name)    #Super class

# obj=Sub("Andy")
# print(obj)

#super() method
# class Super:
#     def __init__(self,name):
#         self.name=name

#     def __str__(self):
#         return "my name is " + self.name +"."

# class Sub(Super):
#     def __init__(self,name):
#         super().__init__(name)    #Super method ---->Implicitly calling the parent class

# obj=Sub("Andy")
# print(obj)

#Multiple Inheritance
# class SuperA:
#     var_a=10
#     def fun_a(self):
#         return 11
    
# class SuperB:
#     var_b=20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA,SuperB):    #Class inheriting properties from two parent classes
#     pass

# obj=Sub()
# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())


#If in multi level inheritance the both grandparent,parent or child have same var name or method name then python will search from bottom so child class output
# class Level1:
#     variable_1=100
#     def fun(self):
#         return 102
    
# class Level2(Level1):
#     variable_1=200
#     def fun(self):
#         return 202
    
# class Level3(Level2):          #Python searches from bottom to top
#     pass
    
# obj=Level3()
# print(obj.variable_1,obj.fun())

#Multiple Inheritance conflicts
# class Left:
#     var="LL"                #Checks from left to right
#     var_left="LLL"
#     def fun(self):
#         return "Left"
    
# class Right:
#     var="RR"               #same name as Left.var
#     var_right="RRR"
#     def fun(self):         #same name as Left.fun()
#         return "Right"
    
# class Sub(Left,Right):
#     pass

# obj=Sub()
# print(obj.var,obj.var_left,obj.var_right,obj.fun())

#Polymorphism Example----> same name but different function
# class One:
#     def do_it(self):
#         print("do it from One")

#     def doanything(self):
#         self.do_it()       #the doanything calls self.do_it (two=Two()) which checks the do_it method in Two and if not present then it prints the output of One 

# class Two(One):
#     def do_it(self):
#         print("do it from Two")

# one=One()
# two=Two()
# one.doanything()
# two.doanything()

#try-except example
# def reciprocal(n):
#     try:
#         n=1/n
#     except ZeroDivisionError:
#         print("Division failed")      #if this executes else will not be printed
#         return None
#     else:
#         print("Everything went fine")
#         return n
        
# print("---------------")
# print("reciprocal(2) : ", reciprocal(2))
# print("--------------")
# print("reciprocal(0) : ", reciprocal(0))


#try-except-else-finally
# def reciprocal(n):
#     try:
#         n=1/n
#     except ZeroDivisionError:
#         print("Division failed")      #if this executes else will not be printed
#         n = None
#     else:
#         print("Everything went fine")
#     finally:
#         print("its time to say goodbye")
#     return n
        
# print("---------------")
# print("reciprocal(2) : ", reciprocal(2))
# print("--------------")
# print("reciprocal(0) : ", reciprocal(0))

try:
    i=int("Hello")
except Exception as e:         #base class with all the error (Whatever the error will generate,it will be stored in e)
    print(e)
    print(e.__str__())


#Create your own Exception error
# class MyZeroDivisionError(ZeroDivisionError):
#     pass

# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("sone worse news")
#     else:
#         raise ZeroDivisionError("Some bad news")
    
# do_the_division(True)

# import time
# print("start")
# time.sleep(2)
# print("end")







        






















                                                                                                                                            





