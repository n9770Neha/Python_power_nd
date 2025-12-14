import numpy as np
from PIL import Image

path = 'Module_1/W_3-4/assets/'

# RGB format: R(0-255) G(0-255) B(0-255)
# Also exists: Cyan Magenta Yellow K-Black (CMYK)

img_arr = np.random.randint(0, 256, size=(100, 150, 3), dtype=np.uint8)

np.save(path + 'syntheticImage.npy', img_arr)

load_img = np.load(path + 'syntheticImage.npy') 
print(f"Image shape: {load_img.shape}")
print(f"Image Data Type: {load_img.dtype}")
image = Image.fromarray(load_img)
image.save(path+'synthetic.png')
