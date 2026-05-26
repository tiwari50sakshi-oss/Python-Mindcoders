# print("hello")

# age=4
# _Age="four"
# print(age)
# print(_Age)

# print("age")

# name="Sakshi Tiwari"
# profession="Student"
# Age=20

# print("Hello, I'm",name,".I'm a",profession,"and I'm",Age ,"years old.")

# x=5
# print(type(x))

# y=0.5
# print(type(y))

# str="Hello"
# print(type(str))

# a=1j
# print(a)
# print(type(a))

# b=["apple","mango"]
# print(type(b))

# c=("apple","mango")
# print(type(c))

# d=range(6)
# print(d)
# print(type(d))

# e={"name":"jphm","age":20}
# print(e)
# print(type(e))

# f={"apple","banana"}
# print(type(f))

# g=True
# print(g)
# print(type(g))

# h=frozenset({"apple","banana"})
# print(h)
# print(type(h))

# i=b"Hello"
# print(i)
# print(type(i))

# j=bytearray(5)
# print(j)
# print(type(j))

# x=memoryview(bytes(5))
# print(x)
# print(type(x))

# x=None
# print(x)
# print(type(x))

# x=1
# print(x:=3)

# x=4
# print(x<5 and x<10) #true
# print(x>5 or x>10)  #false
# print(x>3 or x>10)  #checked first and got true so didn't check second condition
# print(not(x>5 or x>10))  #Reverses 

# x=10
# y="10"
# print(x is y)


# #Practice
# print("-------PRACTICE-------")
# x=["Maruti","BMW"]
# y=["Maruti","BMW"]
# z=x

# print(x is y)
# print(x is z)
# print(y is not z)
# print("-----------")

# #Membership operator
# x=["Maruti","BMW"]
# y="Maruti"
# z=["tata","BMW"]

# print(y in x)
# print(y in z)
# print(y not in z)

# name=input("please enter name:")
# print("Hello",name)

# x=input("1st no.:")
# y=input("2nd no.:")

# z=x+y
# print(z)

# z=int(x)+int(y)
# print(z)


#IF else
#print the largest number

# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))

# if a>b:
#     Larger_number=a
# else:
#     Larger_number=b
# print("Larger number is",Larger_number)

#Print the largest number among three input numbers
# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# c=int(input("Enter 3rd number:"))

# Larger_number=a
# if b>a:
#     Larger_number=b
# if c>a:
#     Larger_number=c
# print("Larger number is",Larger_number)

#Using MIN and MAX Function
# largest_number=max(a,b,c)
# lowest_number=min(a,b,c)

# print("Largest number:",largest_number)
# print("Lowest number:",lowest_number)

#INFINITE LOOP
# while True:
#     print("Hello")

#WAP to print Largest number using while loop
# largest_number=-999999999

# number=int(input("Enter a number or type -1 to stop:"))

# while number!=-1:
#     if number>largest_number:
#         largest_number=number
#     number=int(input("Enter a number or type -1 to stop:"))

# print("The largest number is:",largest_number)

#Print numbers from 1 to 50 (Vertically)
# number=1
# while number!=51:
#     print(number)
#     number+=1

#Print numbers from 1 to 50 (Horizontally with user input)
# num=int(input("Enter a number:"))

# count=1
# while count<=num:
#     print(count, " ",end="")
#     count+=1


#Count and Print total number of even and odd numbers and the program terminates when 0 is entered
number=int(input("Enter a number:"))

even=0
odd=0
while number!=0:
    if number%2==0:
        even+=1
    else:
        odd+=1
    number=int(input("Enter a number:"))
print("Total number of even numbers:",even)
print("Total number of odd numbers:",odd)



    







