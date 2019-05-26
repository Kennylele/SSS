from scipy import signal

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

# Einlesen der .csv Datei

num = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1", "links2",
       "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
num2 = ["ahoch1", "ahoch2", "ahoch3", "ahoch4", "ahoch5", "atief1", "atief2", "atief3", "atief4", "atief5", "alinks1", "alinks2",
        "alinks3", "alinks4", "alinks5", "arechts1", "arechts2", "arechts3", "arechts4", "arechts5"]
numm = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1", "links2",
        "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
nummm = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1", "links2",
        "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
capital = ["hoch", "tief", "links", "rechts"]
capital2 = ["hoch", "tief", "links", "rechts"]
gaussianwindow = signal.windows.gaussian(512, std=4)

# Darstellung des Amplitudenspektrums
plt.plot(gaussianwindow)
plt.grid(True)
plt.xlabel('Signalnr.')
plt.ylabel('Frequenz')
plt.savefig('data/img/gauss.png')
plt.show()

for a in range(0, 20):
    data = np.load('data/' + str(num[a]) + '.npy')
    data2 = np.load('data/' + str(num2[a]) + '.npy')
    num[a] = np.zeros((171, 512))
    num2[a] = np.zeros((171, 512))
    z = 256

    for y in range(0, 171):
        z = z - 256
        for x in range(0, 512):
            num[a][y, x] = np.mean(np.abs(np.fft.fft(data[z] * gaussianwindow)))
            num2[a][y, x] = np.mean(np.abs(np.fft.fft(data2[z] * gaussianwindow)))
            z = z + 1
        # plt.plot(num[a][y])
        # plt.title('Windownr' + str(y+1+(a*171)))
        # plt.xlabel('Signalnr.')
        # plt.ylabel('Frequenz')
        # plt.grid(True)
        # plt.savefig('data/img/' + str(y+1+(a*171)) + '.png')
        # plt.show()

    for y in range(0, 171):
        for x in range(0, 512):
            num[a][y, x] = num[a][y, x] * gaussianwindow[x]
            num2[a][y, x] = num2[a][y, x] * gaussianwindow[x]
        num[a][y] = np.abs(np.fft.fft(num[a][y]))
        num2[a][y] = np.abs(np.fft.fft(num2[a][y]))
        num[a][y] = np.mean(num[a][y])
        num2[a][y] = np.mean(num2[a][y])

    plt.plot(num[a], 'r')
    plt.title(str(nummm[a]))
    plt.grid(True)
    plt.xlabel('Signalnr.')
    plt.ylabel('Frequenz')
    plt.savefig('data/img/' + numm[a] + 'AlleRichtig.png')
    plt.show()

for z in range(0, 4):
    capital[z] = np.zeros((171, 512))
    capital2[z] = np.zeros((171, 512))
    for y in range(0, 171):
        for x in range(0, 512):
            if (z == 0):
                capital[z][y, x] = (num[0][y, x] + num[1][y, x] + num[2][y, x] + num[3][y, x] + num[4][y, x]) / 4
                capital2[z][y, x] = (num2[0][y, x] + num2[1][y, x] + num2[2][y, x] + num2[3][y, x] + num2[4][y, x]) / 4
            elif (z == 1):
                capital[z][y, x] = (num[5][y, x] + num[6][y, x] + num[7][y, x] + num[8][y, x] + num[9][y, x]) / 4
                capital2[z][y, x] = (num2[5][y, x] + num2[6][y, x] + num2[7][y, x] + num2[8][y, x] + num2[9][y, x]) / 4
            elif (z == 2):
                capital[z][y, x] = (num[10][y, x] + num[11][y, x] + num[12][y, x] + num[13][y, x] + num[14][y, x]) / 4
                capital2[z][y, x] = (num2[10][y, x] + num2[11][y, x] + num2[12][y, x] + num2[13][y, x] + num2[14][y, x]) / 4
            elif (z == 3):
                capital[z][y, x] = (num[15][y, x] + num[16][y, x] + num[17][y, x] + num[18][y, x] + num[19][y, x]) / 4
                capital2[z][y, x] = (num2[15][y, x] + num2[16][y, x] + num2[17][y, x] + num2[18][y, x] + num2[19][y, x]) / 4

    plt.plot(capital[z], 'r')
    plt.grid(True)
    plt.xlabel('Signalnr.')
    plt.ylabel('Frequenz')
    plt.savefig('data/img/' + capital2[z] + 'Average.png')
    plt.show()

