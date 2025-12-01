#Python dictionary
my_dict = {
    'Name': 'Alice', 
    'Age': 30, 
    'City': 'Barrackpore', 
    'Skills': ['Python', 'Data Analysis', 'Machine Learning']}

print("Original Dictionary: ", my_dict)

D = {
    1: 'Neha',
    2: 'Debapriya', 
    3: 'Tripan',
    4: 'Saikat' ,
    5: 'Suvendu'
}
print("Original Dictionary: ", D)

# accessing disctionary items using key
print("Name: ", my_dict['Name'])
print("Age: ", my_dict['Age'])

# accessing dictionary items using get function
print("City : ",my_dict.get("City"))
print("Skills : ",my_dict.get("Skills"))

# Adding an item in dictionary
my_dict["country"] = "INDIA"
print(" Updated dictionary: ", my_dict)

# Deleting an item from dictionary
del my_dict ["Skills"]
print(" Updated dictionary: ", my_dict)

#iterating through the dictionary
for key in my_dict:
    print(key, ":", my_dict[key])   
for key, value in D.items():
    print(key, ":", value)