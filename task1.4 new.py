import cv2
import numpy as np

img = cv2.imread('maze_2.png')
# cv2.imshow('original image ',img)
list =[]
z=100
q=200
for i in range(0,6):
    # print(z,q)
    cropped_image = img[100:200 , z:q]
    # cv2.waitKey(0)
    # print(z,q)
    cv2.imshow('corp 1',cropped_image)
    gray = cv2.cvtColor(cropped_image ,cv2.COLOR_RGB2HSV)
    cv2.imshow('gray image ',gray)
    for p in range(0,4):
        # print(p)
        if p==0:
            l_b =(25,50,70)
            h_b =(89,255,255)
        elif p==2:
            l_b =(128,50,70)
            h_b =(160,255,255)
        elif p==1:
            l_b =(90,50,70)
            h_b =(128,255,255)

        else :
            # print("ooooo")
            l_b =(0,50,70)
            h_b =(9,255,255)


        mask = cv2.inRange(gray ,l_b, h_b)
        res = cv2.bitwise_and(cropped_image ,cropped_image, mask=mask)
        cv2.imshow('res image ',res)
        imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        _, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
        cv2.imshow('thresh image ',thrash)
        contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cv2.waitKey(1)
        cv2.imshow(" new", img)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
            cv2.drawContours(cropped_image, [approx], 0, (0, 0, 255), 2)
            cv2.imshow('contour',cropped_image)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            if len(approx) == 3:
                # print('triangle',p)
                li=[]
                www=str(i+1)
                vv='shop_'+www
                li.append(vv)
                if p==0:    
                    li.append('green')
                elif p==1:
                    li.append('orange')
                elif p==2:
                    li.append('pink')
                else :
                    li.append('blue')
                li.append('triangle')
                M = cv2.moments(contour)
                if M['m00'] != 0:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                # cv.drawContours(image, [i], -1, (0, 255, 0), 2)
                l=[]
                e=i+1
                cx=e*100+cx
                cy=e*100+cy
                l.append(cx)
                l.append(cy)
                li.append(l)
                # print(cx,cy)
                # print(li)
                list.append(li)
                # cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            elif len(approx) == 4:
                
                li=[]
                ww=str(i+1)
                v='shop_'+ww
                li.append(v)
                if p==0:    
                    li.append('green')
                elif p==1:
                    li.append('orange')
                elif p==2:
                    li.append('pink')
                else :
                    li.append('blue')
                li.append('square')
                M = cv2.moments(contour)
                if M['m00'] != 0:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                # cv.drawContours(image, [i], -1, (0, 255, 0), 2)
                l=[]
                t=i+1
                cx=t*100+cx
                cy=t*100+cy
                l.append(cx)
                l.append(cy)
                li.append(l)
                # print(cx,cy)
                # print(li)
                list.append(li)
            else:
                li=[]
                w=str(i+1)
                f='shop_'+w
                li.append(f)
                if p==0:    
                    li.append('green')
                elif p==1:
                    li.append('orange')
                elif p==2:
                    li.append('pink')
                else :
                    li.append('blue')
                li.append('circle')
                M = cv2.moments(contour)
                if M['m00'] != 0:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                # cv.drawContours(image, [i], -1, (0, 255, 0), 2)
                l=[]
                g=i+1
                cx=g*100+cx
                cy=g*100+cy
                l.append(cx)
                l.append(cy)
                li.append(l)
                # print(cx,cy)
                # print(li)
                list.append(li)
                # cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    # cv2.waitKey()
    z=z+100
    q=q+100
print(list)
cv2.waitKey(0)