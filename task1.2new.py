import cv2
import numpy as np

img=cv2.imread('maze_14.png')
# cv2.imshow('imge',img)
cv2.waitKey(0)
list=[]
# q=100
# w=200
q=100
w=200
for j in range(1,7):
    qq=96
    ww=105
        
    for i in range(1,8):
        
        crop_img=img[qq:ww ,q:w]
        # cv2.imshow('cropimge',crop_img)
        cv2.waitKey(2)
        gray = cv2.cvtColor(crop_img,cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(gray ,(0,0,231),(180,18,255))
        res = cv2.bitwise_and(crop_img ,crop_img, mask=mask)
        # cv2.imshow('res image ',res)
        imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        _, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
        # cv2.imshow('thresh image ',thrash)
        contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cv2.waitKey(1)
        # print(len(contours))
        # cv2.imshow(" new", img)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
            cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
            # cv2.imshow('contour',crop_img)
            
            
            if j==1 :    
                u='A'+str(i)
                z='B'+str(i)
                v=u+'-'+z
            elif j==2 :
                u='B'+str(i)
                z='C'+str(i)
                v=u+'-'+z
            elif j==3 :
                u='C'+str(i)
                z='D'+str(i)
                v=u+'-'+z
            elif j==4 :
                u='D'+str(i)
                z='E'+str(i)
                v=u+'-'+z
            elif j==5 :
                u='E'+str(i)
                z='F'+str(i)
                v=u+'-'+z
            elif j==6 :
                u='F'+str(i)
                z='G'+str(i)
                v=u+'-'+z
                
            # print(v)
            list.append(v)
            # print(list)
        


        qq=qq+100
        ww=ww+100
    q=q+100
    w=w+100
print("'horizontal_road_under_construction':",end ='')
print(list)

cv2.waitKey(0)