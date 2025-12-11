import numpy as np
path = 'Module_1/W_3-4/assets/'

a1 = np.arange(10)
a2 = np.random.rand(5, 5)
a3 = np.zeros((3, 3, 3))
#save multiple aeeary to a single .npz file
np.savez(path+'data_a1.npz',arr1=a1,arr2=a2,arr3=a3)

#loading multiple arrays
loaded=np.load(path+'data_a1.npz')
print(loaded['arr1'])
print(loaded['arr2'])
print(loaded['arr3'])
