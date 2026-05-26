#Write a program to calculate hypotenuse between two sides
# x=int(input("Enter 1st side of a Triangle: "))
# y=int(input("Enter 2nd side of a Triangle: "))

# h=(x**2 + y**2)**0.5

# print("Hypotenuse of a Triangle is:",h)

#Write a program to print a square using only print function
#METHOD I
# print("+----------+")
# print("|          |")
# print("|          |")
# print("|          |")
# print("|          |")
# print("+----------+")

# #METHOD II
# print("+"+"-"*10+"+")
# print(("|"+" "*10+"|\n")*5,end="")
# print("+"+"-"*10+"+")

Plant=input("Enter a plant name:")
if Plant=="Spathiphyllum":
    print("Yes - Spathiphyllum is the best palnt ever")
elif Plant=="spathiphyllum":
    print("No I want a big Spathiphyllum")
else:
    print("Spathiphyllum! Not",Plant)

for temp in range(1,7):
    print(str(temp)*temp)



