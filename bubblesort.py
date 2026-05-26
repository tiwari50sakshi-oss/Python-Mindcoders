# list=[1,2,3,4,5]    #[8,10,6,2,4]
# swapped=True
# count=0
# while swapped:
#     swapped=False
#     for iterator in range(len(list)-1):
#          count+=1 
#          if list[iterator]>list[iterator +1]:
#             swapped=True
#             list[iterator],list[iterator + 1]=list[iterator + 1],list[iterator]
# print(list)
# print(count)


# my_list=[8,10,4,2,6]
# my_list.sort()
# print(my_list)

# my_list=[4,2,1]
# my_list.reverse()
# print(my_list)

# myList=["A"," ","a","B"]
# myList.sort()
# print(myList)


# list_1=[1]
# list_2=list_1
# list_1[0]=2
# print(list_2)
# print(list_1)

# list_1=[1]
# list_2=list_1[:]
# list_1[0]=2
# print(list_2)
# print(list_1)

# myList=[10,8,6,4,2]
# newList=myList[1:3]     #3rd index not included
# print(newList)

# newList1=myList[1:-1]     #not[-1:1] -----> [] ----->Blank list
# print(newList1)

# newList1=myList[-5:3]     
# print(newList1)

# newList1=myList[:3]     
# print(newList1)

# newList1=myList[2:]     
# print(newList1)

# del myList[1:3]     
# print(myList)

# del my_list[:]
# print(my_list)

# # del my_list
# # print(my_list)

# myList=[10,8,6,4,2]
# print(5 in myList)
# print(2 not in myList)

# row=[]
# for i in range(8):
#     row.append("WHITE PAWN")
# print(row)

# #LIST COMPREHENSIONS
# row=["WHITE PAWN" for i in range(8)]
# print(row)

# squares=[x**2 for x in range(1,11)]
# print(squares)

# twos=[2**i for i in range(8)]
# print(twos)

# squares=[x**2 for x in range(1,11)]
# odds=[x for x in squares if x%2!=0]
# print(odds)

# board=[]
# for i in range(8):
#     row=["EMPTY" for i in range(8)]
#     board.append(row)

# for element in board:
#     print(element)
# print(len(board))

# print(board[0][0])

# print("------------\n")
# board[0][0]="Rooks"
# board[0][7]="Rooks"
# board[7][0]="Rooks"
# board[7][7]="Rooks"

# for element in board:
#     print(element)

# print("------------\n")
# board[0][1]="Knight"
# board[0][6]="Knight"
# board[7][1]="Knight"
# board[7][6]="Knight"

# for element in board:
#     print(element)

temps=[[0.0 for h in range(24)] for d in range(31)]
for element in temps:
    print(element)

print("----------------------------------\n")

#AVERAGE NOON TEMPERATURE
temp1=15      #Sample temperature values
temp2=32
count=0

for days in temps:
    if count==0:
        days[11]=temp1          #Why 11? cause indexing starts from 0 and at 12noon -->11th index as for 1A:M---->0(Calculating from midnight)
        count=1
    else:
        days[11]=temp2
        count=0

for element in temps:
    print(element)

total=0.0
for day in temps:
    total+=day[11]
average=total/31
print("Average temperature at noon: ",average)

#HIGHEST TEMPERATURE DURING WHOLE MONTH
print("-------------------------\n")

highest=-100.0         #Why -100.0? Beacause temperature will definitely be bigger than -100
for day in temps:
    for temp in day:
        if temp>highest:
            highest=temp
print("highest temperature during whole month: ",highest)


print("-------------------------------------------\n")

hot_days=0
for day in temps:
    if day[11]>20.0:
        hot_days+=1
print(hot_days, "days were hot days in the month")

print("----------------------------------------------------------------")
#3D LIST

rooms=[[[False for r in range(20)] for f in range(15)]for t in range(3)]
print(rooms)
print("------------------------------\n")

rooms[1][9][13]=True

rooms[1][9][1]=True

vacancy=0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy+=1
print("Vacancy in 15th floor of 3rd building : ",vacancy)




