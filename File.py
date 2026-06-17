# with open("data.txt","r") as file:
#     data=file.read()

# print(data)

# #Creating a file if not exists anf write 
# with open('students.txt','w') as f:
#     f.write('Rahul,56,Bhopal\n')
#     f.write('diksha,59,Indore\n')
#     f.write('Sakshi,50,Jabalpur\n')

# with open('students.txt','a') as f:
#     f.write('Sneha,88,Bhopal\n')

# with open('students.txt','r') as f:
#     content=f.read()
# print(content)

# with open('students.txt','r') as f:
#     for line in f:
#         name,marks,city=line.strip().split(',')
#         print(f'{name:<15} | {marks:>5} | {city}')
#         print("----------------")

# import csv

# records=[
#     ['Name','Marks','City','Grade'],
#     ['Rahul',67,'Indore','A'],
#     ['Priya',96,'Bhopal','A'],
#     ['Amit',78,'Jabalpur','B'],
# ]

# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]} : {row["Marks"]} marks ({row["City"]})')

import csv

record=[
    ['Name','Age','Sub1','Marks1','Sub2','Marks2','Sub3','Marks3'],
    ['Sakshi',20,'Maths',99,'Physics', 78,'Chem', 89],
    ['Amit',21,'Maths',99,'Physics', 78,'Chem', 89],
    ['Jay',19,'Maths',99,'Physics', 78,'Chem', 89],
       
]

with open('record.csv','w',newline='') as f:
    csv.writer(f).writerows(record)

name=input("Enter student name to search")
found=False
with open('record.csv','r') as f:
    for row in csv.DictReader(f):
        if row["Name"]==name:
            print(f'Found {name}')
            print(f'{row["Name"]} : {row["Age"]} | {row["Sub1"]} : {row["Marks1"]} marks | {row["Sub2"]} : {row["Marks2"]} marks | {row["Sub3"]} : {row["Marks3"]} marks')
            found=True
            break
if not found:
    print("Student not found!")




