# print("STOP")
# for counter in range(100):
#     print(counter," ",end="")
#     pass


# print("START,STOP")
# for counter in range(2,8):
#     print("\nThe value of countet is currently:",counter)

# print("START,STOP,SKIP")
# for counter in range(2,8,3):
#     print("\nThe value of countet is currently:",counter)

# for counter in range(1,1):
#     print(counter)

# power=1
# for expo in range(16):
#     print("2 to the power of",expo,"is",power)
#     power*=2

# #BREAK
# print("The break instruction:")
# for counter in range(1,6):
#     if counter==3:
#         break
#     print("Inside the loop",counter)
# print("Outside the loop:",counter)

# #CONTINUE
# for counter in range(1,6):
#     if counter==3:
#         continue
#     print("Inside the loop",counter)
# print("Outside the loop:",counter)

# counter=1
# while counter<5:
#     print(counter)
#     counter+=1
# print("else:",counter)

# counter=5
# while counter<5:
#     print(counter)
#     counter+=1
# print("else:",counter)

# for counter in range(1,5):
#     print(counter)
# print("else:",counter)

# #Logical Expression
# print("\n---Logical Expression---")
# var=10
# print(var>0)
# print(not(var<=0))

# print(var!=0)
# print(not(var==0))

# #LIST
# numbers=[10,5,6,7,8]

# print(numbers)
# print(type(numbers))

# print("First element content : ",numbers[0])
# print("Second element content : ",numbers[1])
# print("Third element content : ",numbers[2])
# print("Fourth element content : ",numbers[3])
# print("Fifth element content : ",numbers[4])

# #UPDATE
# numbers[0]=111
# print("numbers[0]:",numbers[0])
# print(numbers)

# numbers[1]=numbers[4]
# print(numbers)
# print(len(numbers))   #len() function
# del numbers[2]        #del function
# print(numbers)
# print(len(numbers))

# num=[1,2,3]         #Negative indices
# print(num[-1])
# print(num[-2])
# print(num[-3])
# # print(num[-5])     #IndexError

# number=[1,2,3,4,5]
# print(len(number))
# del number[-1]    #OR len-1
# print(number)
# a=int(input("Enter a number : "))
# number[int(len(number)//2)]=a    #Floor division gives roundoff but still in float so typecasting
# print(number)

# list=[5,4,3,2,1]
# list.append(6)
# print(list)

# list.insert(0,10)
# print(list)

# my_list=[1,2,3,4,5,6,7,8,9,10]
# for iterator in range(len(my_list)):
#     print(my_list[iterator])

# list=[]
# print(list)
# for iterator in range(1,11):
#     list.append(iterator)
# print(list)

my_list1=[10,20,30,40,50,60,70,80,90,100]
for iterator in range(len(my_list1)):
    my_list1[iterator]+=1
print(my_list1)

#Sum using range
my_list1=[10,20,30,40,50,60,70,80,90,100]
sum=0
for iterator in range(len(my_list1)):
    sum+=my_list1[iterator]
print("Sum : ",sum)


#Sum without using range
list=[10,1,8,3,5]
total=0
for element in list:
    total+=element
print(total)


#Swapping of two variables using python formula,not by creating a temporary variable
var1=1
var2=2

print("Var1 : ",var1)
print("Var2 : ",var2)

var1,var2=var2,var1

print("Var1 : ",var1)
print("Var2 : ",var2)

#Swapping two elements in a list
list=[1,2,3,4,5]
list[1],list[4]=list[4],list[1]
print(list)













