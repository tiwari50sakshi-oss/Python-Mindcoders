dictionary={
    "cat":"chat",
    "dog":"chein",
    "horse":"cheval"

}
phone_numbers={'boss':7527356253,'Suzy':763766378738}
empty_dictionary={}

print(dictionary)
print(type(dictionary))
print(phone_numbers)
print(type(phone_numbers))
print(empty_dictionary)
print(type(empty_dictionary))

print(dictionary['cat'])
print(phone_numbers['Suzy'])

# print(phone_numbers['president'])   #KeyError : 'president'

words=['cat','lion','horse']
for word in words:
    if word in dictionary:
        print(word,"->",dictionary[word])
    else:
        print("-----",word,"is not in dictionary","-------")

print(dictionary.keys())
for key in dictionary.keys():
    print(key,"->",dictionary[key])


print("------------------------")
print(dictionary.items())
for key,value in dictionary.items():
    print(key,"->",value)

print("------------------------")
print(dictionary.values())
for value in dictionary.values():
    print(value)

print("------------------------")
pol_eng_dictionary={
    "zamek":"castle",
    "voda":"water",
    "gleba":"soil"

}
print("pol_eng_dictionary: ",pol_eng_dictionary)
copy_dictionary=pol_eng_dictionary.copy()

print("copy_dictioanry: ",copy_dictionary)

print("-------------------------------")
pol_eng_dictionary["zamek"]="lock"
item=pol_eng_dictionary["zamek"]
print(item)
print(pol_eng_dictionary)

print("-------------------------------")
phonebook={}
print(phonebook)
phonebook["Adam"]=734663746  #create/add a key-value pair
print(phonebook)     #outputs {'Adam:634875685684}

del phonebook["Adam"]
print(phonebook)

print("-------------------------------")
pol_eng_dictionary={"kwiat":"flower"}
pol_eng_dictionary.update(
    {
        "glebe":"soil"
    }
)
print(pol_eng_dictionary)
pol_eng_dictionary.popitem()
print(pol_eng_dictionary)

