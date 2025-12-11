#create a nummpy array
import numpy as np
path = 'Module_1/W_3-4/assets/'

array = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", array)
print("Type:", type(array))

#use a taple to create a numpy array
arr1 = np.array((1, 2, 3, 4, 5))
print("Numpy Array from Tuple:", arr1)

# creating n-d array
#0-D array
arr2 = np.array(45)
print("0-D Array:", arr2)

#1-D array
arr3 = np.array([1, 2, 3, 4, 5])
print("1-D Array:", arr3)   

#2-D array
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D Array:\n", arr4)

#3-D array
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D Array:\n", arr5)

#save single array to .npy file
np.save(path+'data_a1.npy', arr3)
np.save(path+'data_a2.npy', arr4)
np.save(path+'data_a3.npy', arr5)