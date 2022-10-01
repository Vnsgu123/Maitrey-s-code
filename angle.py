import cv2 as cv
from cv2 import aruco
import numpy as np

frame=cv.imread('aruco_0.png')

marker_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
param_markers = aruco.DetectorParameters_create()
dict ={}
small =[]
cor ={}

gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
marker_corners, marker_IDs, reject = aruco.detectMarkers(gray_frame, marker_dict, parameters=param_markers)

if marker_corners:
    for ids, corners in zip(marker_IDs, marker_corners):
        # cv.polylines(
        #     frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA
        # )
        # aruco.drawDetectedMarkers(frame,marker_corners,marker_IDs)
        corners = corners.reshape(4, 2)
        corners = corners.astype(int)
        top_right = corners[0].ravel()
        top_left = corners[1].ravel()
        bottom_right = corners[2].ravel()
        lisst=[]
        bottom_left = corners[3].ravel()
        lp=[]
        lp.append(top_left[0])
        lp.append(top_left[1])
        lisst.append(lp)
        lp=[]
        lp.append(top_right[0])
        lp.append(top_right[1])
        lisst.append(lp)
        lp=[]
        lp.append(bottom_right[0])
        lp.append(bottom_right[1])
        lisst.append(lp)
        lp=[]
        lp.append(bottom_left[0])
        lp.append(bottom_left[1])
        lisst.append(lp)
        w=ids[0]
        cor[w]=lisst
       
        cx = (top_right[0]+top_left[0]+bottom_right[0]+bottom_left[0])/4
        cy = (top_right[1]+top_left[1]+bottom_right[1]+bottom_left[1])/4
        list =[]
        list.append(cx)
        list.append(cy)
        small.append(list)
        k=ids[0]
        k=int(k)
        # cor[k]= lisst
        dict[k] = list
big = []
Detected_ArUco_markers ={}
for i in range(0,marker_IDs.shape[0]):
    Detected_ArUco_markers[marker_IDs[i][0,]] = marker_corners[i][0,]
ArUco_marker_angles = {}
cnt = 0
ans_x = 0
ans_y = 0
midpoint_x = 0
midpoint_y = 0
right_x = 0
right_y = 0
m=0
for i in Detected_ArUco_markers:
    for j in Detected_ArUco_markers[i]:
        if (cnt%4) == 0:
            ans_x = j[0,]
            ans_y = j[1,]
            midpoint_x = ans_x
            midpoint_y = ans_y
            cnt = 1
        else:
            cnt += 1
            if cnt == 2:
                midpoint_x = (midpoint_x + j[0,])/2
                midpoint_y = (midpoint_y + j[1,])/2
                right_x = j[0,]
                right_y = j[1,]
            ans_x += j[0,]
            ans_y += j[1,]
    ans_x = int(ans_x/4)
    ans_y = int(ans_y/4)
    midpoint_x = int(midpoint_x)
    midpoint_y = int(midpoint_y)
    # cv.circle(frame,(ans_x,ans_y), 5, (0,0,255), -1)
    # cv.line(frame,(ans_x,ans_y),(midpoint_x,midpoint_y),(255,0,0),5)
    midpoint_x = midpoint_x - ans_x
    midpoint_y = -(midpoint_y - ans_y)

    ans_x = 0
    ans_y = 0
    id_str = str(i)
    font = cv.FONT_HERSHEY_SIMPLEX
    big =[]
    if midpoint_y < 0:
        ang = str(int((360-np.arccos(np.inner([1,0],[midpoint_x,midpoint_y])/np.linalg.norm([midpoint_x,midpoint_y]))*180/np.pi)))
        ang = ang.replace('(','').replace(')','')  
        ang=int(ang)
        angg=ang

        if angg>=90 and angg<=270 :
            angg=angg-90
        elif angg<=90 :
            angg=90-angg
            angg=-angg
        else :
            angg = 90 + (360-angg)
            angg=-angg
        ang=angg
        big.append(small[m])
        big.append(ang)
        ArUco_marker_angles[i] = big
        m=m+1
    else:
        ang = str(int((np.arccos(np.inner([1,0],[midpoint_x,midpoint_y])/np.linalg.norm([midpoint_x,midpoint_y]))*180/np.pi)))
        ang = ang.replace('(','').replace(')','')  
        ang=int(ang)
        angg=ang

        if angg>=90 or angg<=270 :
            angg=angg-90
        elif angg<=90 :
            angg=90-angg
            angg=-angg
        else :
            angg = 90 + (360-angg)
            angg=-angg
        ang=angg
        big.append(small[i])
        big.append(ang)
        ArUco_marker_angles[i] = big
        m=m+1

# dict1 = sorted(ArUco_marker_angles.items())
print(ArUco_marker_angles)
print(cor)
key = cv.waitKey(0)
cv.destroyAllWindows()