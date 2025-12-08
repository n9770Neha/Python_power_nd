#PYTHON TUPLES
T=(20, "Python Power", 35.75, [20, 40, 60])
print("Original Tuple: ",T)

#Trvarseing through TUPLE element
for i in range(0, len(T)):
    print(T[i])


#Slising in tuple
# syntax =tuple[start:n]
tup =  ("Apple", "Banana", "Cherry", "Orange", "Kiwi", "Mango", "Pineapple")
print("Sliced Tuple: ", tup[1:4])  
print("Sliced Tuple from index 2 to end: ", tup[2:])      
print("Sliced Tuple from start to index 3: ", tup[:3])
print("Sliced Tuple with negative indices: ", tup[-4:-1])  
print("Sliced Tuple with step: ", tup[::2])  
print("Sliced Tuple with reverse: ", tup[::-1])  
print("Sliced Tuple with start, end and step: ", tup[1:5:2])


#MAX AND MIN FUNCTION 
T2=(1,8,96,77,55,44,44,3)
print("max : ",max(T2))
print("min : ",min(T2))
print("times os occurance : ",T2.count(44))
print("count of tuple : ",len(T2))






