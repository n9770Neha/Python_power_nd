import numpy as np
path = 'Module_1/W_3-4/assets/'

data = np.array([[1.1, 2.2, 3.3],
                 [4.4, 5.5, 6.6],
                 [7.7, 8.8, 9.9]])

np.savetxt(path+'data.csv', data, delimiter=',', header='Column1,Column2,Column3', fmt='%.2f')

loaded_csv = np.loadtxt(path+'data.csv', delimiter=',', skiprows=1)

print("Original data:\n", data)
print("\nLoaded from CSV:\n", loaded_csv)