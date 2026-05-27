my_tuple=(1,10,100)
t1=my_tuple + (1000,10000)
t2=my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
print("----------------------")

my_tuple=(1,2,3)
my_tuple+=(4,5)
print(my_tuple)

tuple_1=(1,2,3)
for elem in tuple_1:
    print(elem)

print("--------------------------")
tuple_2=(1,2,3,4)
print(5 in tuple_2)
print(5 not in tuple_2)

tuple_3=(1,2,3,4)
print(len(tuple_3))
print(5 not in tuple_3)

tuple_4=tuple_1 + tuple_2
tuple_5=tuple_3 * 2
print(tuple_4)
print(tuple_5)
print("---------------------")

My_tuple=tuple((1,2,"string"))
print(My_tuple)
print(type(My_tuple))

my_list=[1,2,4]
print(my_list)
print(type(my_list))
tup=tuple(my_list)   
print(tup)      
print(type(tup))   #outputs<class 'tuple'>

var=123
t1=(1,)
t2=(2,)
t3=(3,var)
t1,t2,t3 = t2,t3,t1
print(t1,t2,t3)
print(type(t1),type(t2),type(t3))