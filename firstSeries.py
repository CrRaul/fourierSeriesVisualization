
import numpy as np
import cv2


def main() :    
    time = 0
    wave = [0]
    tra = 400

    while True:
        img = np.zeros((800,1500), np.uint8)

        x = 0
        y = 0

        for i in range(0,10):
            prevx = x
            prevy = y


            n = i * 2 +1

            radius = 200 * (4/ (n * np.pi)) 
            radius = int(radius)

            x += radius * np.cos(n * time)
            y += radius * np.sin(n * time)
            x,y = int(x), int(y)

            cv2.circle(img, (x+tra,y+tra), 2, (120,120,120),-1)

            cv2.circle(img, (tra+prevx,tra+prevy), radius, (120,120,120),1)
            cv2.line(img,(tra+prevx,tra+prevy),(x+tra,y+tra),(255,255,255),1)
            
        wave.insert(0,y)
        cv2.line(img,(x+tra,y+tra),(tra*2, wave[0]+tra),(255,255,255),1)

        for i in range(0, len(wave)):
            cv2.circle(img, (i+tra*2,wave[i]+tra), 1, (225,225,225),-1)



        cv2.imshow('fourierSeries', img)
        time += 0.0088
        print(time)

        if len(wave) > 500:
            wave.pop(len(wave)-1)


        ch = cv2.waitKey(1)
        if ch == 27:
            break

if __name__ == '__main__':
    main()

cv2.destroyAllWindows()
cv2.waitKey(1)