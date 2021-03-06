import random as rand

import numpy as np
import cv2

# ------------------------------ Random ------------------------------ #



randompixel = cv2.imread('data/zzzrandom.png')

for y in range(0, 1440):
    for z in range(0, 2560):
        r = rand.randint(150, 255)
        g = rand.randint(150, 255)
        b = rand.randint(150, 255)

        randompixel[y, z] = r, g, b

cv2.imwrite("data/zzzrandom.png", randompixel)
cv2.imshow('image', randompixel)
cv2.waitKey(0)
cv2.destroyAllWindows()
