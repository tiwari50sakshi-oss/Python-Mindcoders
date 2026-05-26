# def message():              #Defination
#     print("Enter a value:")

# message()        #Calling a function/Invocation
# a=int(input())

# message()
# b=int(input())

# message()
# c=int(input())

# def message():
#     print("Enter a value:")

# print("We start here")
# print(message)   #returns memory
# message()
# print("We end here")

# def message():              #Defination
#     print("Enter a value:")
#     temp=int(input())
#     return temp

# a=message()
# b=message()
# c=message()

# print("a : ",a)
# print("b : ",b)
# print("c : ",c)

# def hi():            #TypeError
#     print("hi")
# hi(5)

# def hello(n):      #defining a function
#     print("Hello",n)    #Body of the function
# name=input("Enter your name:")  
# hello(name)    #calling the function

# def message(number):
#     print("Enter a number:",number)
# number=1234
# message(1)
# print(number)

# def message(what,number):
#     print("Enter",what,"number",number)
# message("Telephone",11)
# message(11,"telephone")
# message("price",5)
# message("number",number)

def introduction(first_name,last_name):
    print("Hello, my name is",first_name,last_name)

introduction("Luke","Skywalker")
introduction("Diksha","Skywalker")
introduction("Sakshi","Skywalker")


introduction(first_name="diksha",last_name="walkedr")
introduction(last_name="noor",first_name="jahan")

def adding(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)
adding(1,2,3)
adding(c=1,a=2,b=3)
adding(3,c=3,b=2)
# adding(3,a=1,b=2)  #Error

def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("one...")
    if not wishes:
        return
    print("Happy new year!")
happy_new_year()

def boring_function():
    print("Boredom mode:On")
    return 123
print("This lesson is interesting")
boring_function()
print("This lesson is boring....")

def checkMyVar(variable):
    if(variable==10):
        print("Variable is 10")
        return 2
    else:
        print("variable is not up to the mark")
        return
checkMyVar(10)

def list_sum(lst):
    s=0

    for elem in lst:
        s+=elem
    return s
print(list_sum([5,4,3]))
# print(list_sum(2))

def storage_list_fun(n):
    storage_list=[]

    for i in range(0,n):
        # storage_list.insert(0,i+1)
        storage_list.append(i+1)

    return storage_list
print(storage_list_fun(5))



