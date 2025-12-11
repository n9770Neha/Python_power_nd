import numpy as np
path = 'Module_1/W_3-4/assets/'

#load array from .npy file
load_1d = np.load(path+'data_a1.npy')  
load_2d = np.load(path+'data_a2.npy')
load_3d = np.load(path+'data_a3.npy')

print(f"Loaded 1-D Array shape: {load_1d.shape}, contents:\n{load_1d}")
print(f"Loaded 2-D Array shape: {load_2d.shape}, contents:\n{load_2d}")
print(f"Loaded 3-D Array shape: {load_3d.shape}, contents:\n{load_3d}")



