

import numpy as np
import cv2
import math

time = 0
tra = 200


def dft(x):
    X = []
    N = len(x)
    for k in range(N):
        re = 0
        im = 0
        for n in range(N):
            phi = (2*np.pi * k * n) / N
            re += x[n] * np.cos(phi)
            im += x[n] * np.sin(phi)
        re = re / N
        im = im / N

        freq = k
        amp = np.sqrt(re*re+im*im)
        phase = math.atan2(im,re)

        X.append([re,im,freq,amp,phase])

    return X

def epiCycles(x,y,rotation,fourier,img):
    global time,tra
    for i in range(0,len(fourier)):
        prevx = x
        prevy = y

        freq = fourier[i][2]
        radius = fourier[i][3]
        phase = fourier[i][4]

        x += radius * np.cos(freq * time + phase + rotation)
        y += radius * np.sin(freq * time + phase + rotation)
        x,y = int(x), int(y)
        radius = int(radius)

        cv2.circle(img, (x+tra,y+tra), 2, (120,120,120),-1)

        cv2.circle(img, (tra+prevx,tra+prevy), radius, (120,120,120),1)
        cv2.line(img,(tra+prevx,tra+prevy),(x+tra,y+tra),(255,255,255),1)


def main() :    
    global time, tra

    wave = [0]

    Y = []
    for i in range(360):
        angle = i
        Y.append(100*np.sin(angle))

    fourierY = dft(Y)

    X = []
    for i in range(360):
        angle = i * 2
        X.append(100*np.cos(angle))

    fourierX = dft(X)

    while True:
        img = np.zeros((800,1500), np.uint8)

        epiCycles(50,200,0,fourierY,img)
        epiCycles(400,0, np.pi/2,fourierX,img)
            
       # wave.insert(0,y)
       # cv2.line(img,(x+tra,y+tra),(tra*2, wave[0]+tra),(255,255,255),1)

      #  for i in range(0, len(wave)):
       #     cv2.circle(img, (i+tra*2,wave[i]+tra), 1, (225,225,225),-1)


        cv2.imshow('fourierSeries', img)

        dt = 2*np.pi / len(fourierY)
        time += 0.001
        print(time)

#        if len(wave) > 500:
 #           wave.pop(len(wave)-1)

        cv2.waitKey(10)

        ch = cv2.waitKey(1)
        if ch == 27:
            break

if __name__ == '__main__':
    main()


cv2.destroyAllWindows()
cv2.waitKey(1)
