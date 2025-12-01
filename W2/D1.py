#ADVANCE DATA STRUCTURE
#list
# creating a list that holds different types of data
my_list = [20, "Python Power", 35.75, [20, 40, 60]]
print(my_list)

# traversing through the elements of the LIST
for i in range(0, len(my_list)):
    print(my_list[i])

# test mutable property
my_list[2] = 89.99
print(my_list)
