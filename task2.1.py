import numpy as np
import cv2

# ------------------------------ Aufgabe2.1 ------------------------------ #

vec = np.zeros((10, 307200))
pixel = 0, 0, 0
anzahl = 0

blackpic = ["black1", "black2", "black3", "black4", "black5", "black6", "black7", "black8", "black9", "black10"]

for x in range(0, 10):
    blackpic[x] = cv2.imread('data/' + blackpic[x] + '.png')
    blackpic[x] = cv2.cvtColor(blackpic[x], cv2.COLOR_BGR2GRAY)

    for y in range(0, 640):
        for z in range(0, 480):
            b = float(blackpic[x][y, z])
            print(b)
            vec[x, anzahl] = b
            anzahl += 1


