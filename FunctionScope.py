# def scope_test():
#     x=123   #Local variable
# scope_test()
# # print(x)

# def my_Function():
#     print("Do i know that variable?",var)
# var=1     #Global variable
# my_Function()
# print(var)

# def mult(x):
#     var=7
#     return x*var    
# var=3
# print(mult(7))   #Shadowing----->Output 49

# def my_function():
#     global var   #Making local variable global
#     var=2
#     print("Do i know that variable?",var)
# var=1
# my_function()
# print(var)

# #Overwrites
# var=2
# print(var)
# def return_var():
#     global var
#     var=5
#     return var
# print(return_var())
# print(var)

# def My_function(n):
#     print("I got",n)
#     n+=1
#     print("I have",n)
# var=1
# My_function(var)
# print(var)

# def my_function(my_list_1):
#     print("Print #1",my_list_1)
#     print("Print #1",my_list_2)
#     my_list_1=[0,1]
#     print("Print #1",my_list_1)
#     print("Print #1",my_list_2)
# my_list_2=[2,3]
# my_function(my_list_2)
# print("Print #5",my_list_2)

# print("-----------------------------")
# def my_function(my_list_1):
#     print("Print #1",my_list_1)
#     print("Print #1",my_list_2)
#     del my_list_1[0]  #Update
#     print("Print #1",my_list_1)
#     print("Print #1",my_list_2)
# my_list_2=[2,3]
# my_function(my_list_2)
# print("Print #5",my_list_2)

# def countDown(number):
#     print(number)
#     if number==0:
#         return
#     else:
#         print("Going in rec:",number)
#         countDown(number-1)
#         print("Out of rec:",number)
# print("Starting recursion")
# countDown(5)
# print("Completed Recursion")

def factorial(number):
    
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
print("Factorial of an number:",factorial(5))





