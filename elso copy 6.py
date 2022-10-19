import cv2
import numpy as np

image  = cv2.imread("n2.jpg")

#átméretezés: hasonló felbontás érdekében
fxy = 1700 / image.shape[0]
image= cv2.resize(image,None,fx=fxy,fy=fxy)

#küszöb
I = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
I = cv2.GaussianBlur(I, (5,5), 0)
I = cv2.morphologyEx(I, cv2.MORPH_CLOSE, np.ones((3,3)))
I = cv2.adaptiveThreshold(I, 255, 1, 1, 11, 2)

#so-bors eltünteése
I=cv2.medianBlur(I,3)
cv2.imshow("szurt", I)


#kontur keresés
contours, _ = cv2.findContours(I, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

c = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 40:
            cv2.drawContours(image, contours, c, (0, 255, 0), 3)
        c+=1
cv2.imshow("vegso", image)


#TODO javítás ha más távolságról van a kép-> sok kicsi kontur terület ->csokkenteni a felbontást




cv2.waitKey(0)
cv2.destroyAllWindows()