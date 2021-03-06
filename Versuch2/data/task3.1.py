import numpy as np
import cv2

# ------------------------------ Aufgabe3.1 ------------------------------ #

vec = np.zeros((10, 3079000))
anzahl = 0
mean = 0
value = 0

vec1 = np.zeros((480, 640))
vec2 = np.zeros((480, 640))
vec3 = np.zeros((480, 640))
vec4 = np.zeros((480, 640))
vec5 = np.zeros((480, 640))
vec6 = np.zeros((480, 640))
vec7 = np.zeros((480, 640))
vec8 = np.zeros((480, 640))
vec9 = np.zeros((480, 640))
vec10 = np.zeros((480, 640))
average = np.zeros((480, 640))

whitepic = ["white1", "white2", "white3", "white4", "white5", "white6", "white7", "white8", "white9", "white10"]
vector = [vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10]

for x in range(0, 10):
    whitepic[x] = cv2.imread('data/' + whitepic[x] + '.png')
    whitepic[x] = cv2.cvtColor(whitepic[x], cv2.COLOR_BGR2GRAY)

    print("Datei: " + str(x + 1) + ".png erfolgreich")
    b, g, r, a = cv2.mean(whitepic[x])
    print("Der Durchschnitt der Datei liegt bei " + str(b))
    print("-----------------------------------")

    value += b

value /= 10
print(b)

image = cv2.imread("data/whiteaverage.png")
for x in range(0, 480):
    for y in range(0, 640):
        image[x, y] = b

cv2.imwrite("data/whiteaverage.png", image)
cv2.imshow('image', image)

# Convert to YUV
image_contrast = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
# Apply histogram equalization
image_contrast[:, :, 0] = cv2.equalizeHist(image_contrast[:, :, 0])
# Convert to RGB
image_contrast = cv2.cvtColor(image_contrast, cv2.COLOR_YUV2RGB)

cv2.imwrite("data/contrastwhiteaverage1.png", image_contrast)
cv2.imshow('image_contrast', image_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()