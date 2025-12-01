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


#EXTEND THE LIST
my_list.extend([1,4,8,9])
print("Extended list: ",my_list)


#Sorting the list in acending order
num_list = [98, 65, 57, 12, 8, 44, 35]
print("Given list: ", num_list)
num_list.sort()
print("Sorted list: ",num_list)


#Reverse a list 
num_list.reverse()
print("Revesed list: ",num_list)

