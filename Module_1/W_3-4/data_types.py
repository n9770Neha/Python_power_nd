#Creat array with different data types
import numpy as np
path = 'Module_1/W_3-4/assets/'

int_array=np.array([1,2,3],dtype=np.int32)
float_array=np.array([1.1,2.2,3.3],dtype=np.float64)
bool_array=np.array([True,False,True],dtype=np.bool_)

np.savez(path+'dTypes.npz', integers=int_array,floats=float_array,booln= bool_array)
loaded=np.load(path+'dTypes.npz')

print(f"Integer array datatyprs:{loaded['integers']}")
print(f"Float array datatyprs:{loaded['floats']}")
print(f"Boolean array datatyprs:{loaded['booln']}")