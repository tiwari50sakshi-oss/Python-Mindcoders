#Print the tax calculated
# income=float(input("Enter the income:"))
# if income<85528:
#     tax=((18/100)*income)-556.02
    
#     if income<0:
#         tax=0
    
# else:
#     tax=14839.02 + (income - 85528)*(32/100)
# print("The Tax:",round(tax))

#leap year or not
# year_number=int(input("Enter the Year :"))
# if year_number<1582:
#     print("Not within the gregorian era!")
# elif year_number%4!=0:
#     print(year_number,"is a common year according to gregorian calender")
# elif year_number%100!=0:
#     print(year_number,"is a leap year according to gregorian calender")

# elif year_number%400!=0:
#     print(year_number,"is a common year according to gregorian calender")
# else:
#     print(year_number,"is a leap year according to gregorian calender")

#Count Mississipi
# for count in range(1,6):
#     print(count,"mississippily")

# print("Ready or not,here I come")

#BLOCK QUESTION
# blocks=int(input("Enter no. of blocks:"))
# height=0
# layer=1

# while blocks>=layer:
#     blocks-=layer
#     height+=1
#     layer+=1

# print("Height of pyramid:",height)


#German mathematician
# c0=int(input("Enter a number:"))
# steps = 0
# while c0!=1:
#     if c0%2==0:
#         c0=c0//2
#     else:
#         c0=3*(c0+1)
#     print(c0)
#     steps+=1
# print("Steps : ",steps)

#Hat question
# My_list=[1,2,3,4,5]
# print(len(My_list))

# del My_list[4:]
# print(My_list)

# num=int(input("Enter a number:"))
# My_list[(len(My_list))//2]=num
# print(My_list)

#THE BEATLES
# beatles=[]
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")

# print(beatles)

# for member in ["Sakshi","Diksha"]:
#     userInput=input(f"Add {member} : ")
#     beatles.append(userInput)
    
# print(beatles)

# del beatles[3]
# del beatles[3]
# print(beatles)

# beatles.insert(0,"Ringo Starr")
# print("Final list : ",beatles)

#Print from 1 to 50 with a pattern
# for i in range(1,51):
#     if i%15==0:
#         print("FizzBuzz",end=" ")
#     elif i%3==0:
#         print("fiz",end=" ")
#     elif i%4==0:
#         print("Buzz",end=" ")
#     else:
#         print(i,end=" ")

#Count numbers of digits
# string="MindCoders password2 is : 1234"
# count=0
# for word in string:
#     if word.isdigit():
#         count+=1
# print("No. of digits : ",count)

#Count numbers of digits
# string="U r a a n S 0 f t S k i l l 1 s 1234"
# count=0
# for word in string:
#     if word.isdigit():
#         count+=1
# print("No. of digits : ",count)

#Occurences of s or S
# string="MindCoders"
# count=0
# for word in string:
#     if word=='s' or word=='S':
#         count+=1
# print("No. of digits : ",count)

#Count no. of reoeated characters and unique characters in a string
# string="UraanSoftSkills"
# repeated=0
# unique=0
# for ch in string:
#     if string.count(ch)>1:
#         repeated+=1
#     else:
#         unique+=1

# print("Repeated words : ",repeated)
# print("unique woeds : ",unique)

#Vowel eater
# user_word=input("Enter a word :")
# upper=user_word.upper()
# word_without_vowels=""

# for word in upper:
#     if 'A' in word:
#         continue
#     elif 'E' in word:
#         continue
#     elif 'I' in word:
#         continue
#     elif 'O' in word:
#         continue
#     elif 'U' in word:
#         continue
#     else:
#         word_without_vowels+=word

# print(word_without_vowels)

#Print 10 natural numbers
for num in range(1,11):
    print(num)

#Print even numbers
for i in range(1,11):
    if i%2==0:
        print("Even no. : ",i)

#Print sum of all natural numbers
sum=0
for i in range(1,16):
    sum+=i
print("Sum : ",sum)

#Sum of odd numbers
sum=0
for i in range(1,16):
    if i%2!=0:
        sum+=i
print("sum of odd no. : ",sum )

#print multiplication table of 15
for i in range(1,11):
    print("15 * ",i, ":",15 * i)

#Display list usinf for loop
My_list=[1,2,4,6,88,125]
for elem in My_list:
    print(elem)

#WAP to Count total no. of digits
number=129475
count=0
for num in str(number):
    if num.isdigit():
        count+=1
print("no. of digits : ",count)

#Palindrome or not
string="madam"
reverse=""
for ch in string:
    reverse=ch+reverse
    print(reverse)
print(reverse)
if reverse==string:
    print("palindrome")
else:
    print("not palindrome")

#Reverse the string
string="diksha"
reverse=""
for ch in string:
    reverse=ch+reverse
print("Reverse : ",reverse)

#Armstring or not
Number=153
OG=Number
arm=0
while Number>0:
    num=Number%10
    arm=arm+(num**3)
    Number=Number//10
if arm==OG:
    print("It is an armstrong number : ",arm)
else:
    print("It is not an armstrong number")

    
    




       

    

        







    
    
    







