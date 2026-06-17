import pandas as pd

data={
    'Name' : ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age' :  [22,21,23,20,24],
    'Marks' : [85,92,88,73,56],
    'City' : ['Bhopal','Indore','Bhopal','Jabalpur','Indore'],

}
df=pd.DataFrame(data)     #df is object and Dataframe gives data in tabular format
print(df)

# print(df.shape)
# print(df.head(3))         #first three rows
# print(df.dtypes)          #Data type of each column
# print(df.describe())      #Statistical summary

print("====================")
print("df['Name] : \n",df['Name'])
print(df[['Name', 'Marks']])

#Filter rows
print("-------------------")
print(df[df['Marks']>=85] )
print(df[df['City'] == 'Bhopal'])
print(df[(df['Marks'] >=80) & (df['City'] == 'Indore')])

print("----------------")
def get_grade(x):
    if x>=90:
        return 'A'
    elif x>=75:
        return 'B'
    else:
        return 'C'
    
df['Grade'] =df['Marks'].apply(get_grade)
print(df['Grade'])
print("--------------")
print(df)

#GroupBy - like Excel Pivot
city_avg=df.groupby('City')['Marks'].mean()
print(city_avg)

#Read real csv file 
df2=pd.read_csv('students.csv')
#Cleaning
df2.to_csv('clean_output.csv',index=False)    #save 