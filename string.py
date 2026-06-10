# city="Bhopal"
# print(city[0])
# print(city[1])
# print(city[-1])
# print(city[5])

# print(city[-3])
# print(city[3])

# print(len(city))
# name='Priya Sharma'
# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::2])      #returns every 2nd character
# print(name[::-1])     #Reverses the string
# print(len(name))

# text='  Hello Python World!  '

# #Case
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())     # first letter of each word reverses 

# #Strip Whitesapce
# print(text.strip())       #unwanted whitespace removed

# #Search
# print('Python' in text)      #True
# print(text.find('Python'))   #returns the index where found else -1
# print(text.count('l'))      #no. of occurrences

# #Replace
# print(text.replace('Python','AI'))

# #Split and Join
# csv='Rahul,22,Bhopal,Engineer'
# parts=csv.split(',')
# print(parts)
# print(parts[0])
# rejoined=' | '.join(parts)
# print(rejoined)

# #Returns true or false
# print('hello123'.isalnum())      #checks for the existence of numbers
# print('12345'.isdigit())         #Must be all digit
# print('Python'.isalpha())        #all letters
# print('  '.isspace())            #all spaces


# #checks start/end
# email='student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))

name,marks,rank='Anita',92.567,3

#f string
print(f'Hello, {name}')

#Format numbers
print(f'Marks: {marks:.2f}')
print(f'Marks: {marks:.0f}')
print(f'Count: {1000000:,}')

#padding and alignment
print(f'{name:<15} | {marks:>8.2f} | Rank:{rank}')
print(f'hello {name:^10}')
print(f'hello {name:>10}')
print(f'hello {name:<10}')
print(f'hello {name:*^11}')

#Expression inside {}
price,gst=500,0.18
print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} |Total:Rs{price*(1+gst):.2f}')

string="Hello, How are you doing today?"
#Count vowels in the string
str=string.lower()
count=0
for ch in str:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count+=1
    else:
        count=0
    
    print(count)

#Print you from the string
print(string[15:18])

#Print the string in reverse order
print(string[::-1])

#Check if the string is palindrome or not
non_palin,palin="abcdef","axttxa"
reverse=non_palin[::-1]
if reverse==non_palin:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

reverse1=palin[::-1]
if reverse1==palin:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


