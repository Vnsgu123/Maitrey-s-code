# from pickletools import uint8
import cv2
import numpy as np
from pyzbar import pyzbar
img=cv2.imread('qr_1.png')
d=pyzbar.decode(img)
# print(d)
Dict ={}
for i in d:
    # print(i.data)
    li =[]
    k=i.data.decode('utf-8')
    # print(k)
    # print(i.rect)
    x,y,w,h=i.polygon
    # print(x[0])
    cx=(x[0]+y[0]+w[0]+h[0])/4
    cy=(x[1]+y[1]+w[1]+h[1])/4
    li.append(cx)
    li.append(cy)
    Dict[k]=li

    # print(cx,cy)
    # print(i.polygon)
print(Dict)
cv2.imshow('image',img)
cv2.waitKey(0)
