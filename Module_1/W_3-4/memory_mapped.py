# Create a memory-mapped array (doesn't load entire file into memory)
# Useful for arrays larger than available RAM
import numpy as np
path = 'Module_1/W_3-4/assets/'

map_arr=np.memmap(path+'big_array.dat',dtype='float32',mode='w+',shape=(1000, 1000))
map_arr[:]=np.random.randn(1000, 1000)

#flush to disk
map_arr.flush()
load_arr = np.memmap(path+ 'big_array.dat',dtype='float32', mode='r', shape=(1000, 1000))

print(f"Print first 10 elements: {load_arr[0, :10]}")

