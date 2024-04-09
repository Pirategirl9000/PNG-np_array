import numpy as np
from skimage import io
import sys

im = io.imread("image.png") #RGBA format
imarr = np.array(im)

#remove alpha
imarr = imarr[ :, :, 0]

f = open("file.txt", "w")

np.set_printoptions(threshold=sys.maxsize) #stop truncation

#change to binary for grayscale and less memory
imarr[imarr == 0] = 1
imarr[imarr == 255] = 0

f.write(f"{imarr}")
f.close()