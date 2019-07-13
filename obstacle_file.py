import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import imutils
def read_img(path):
    """Given a path to an image file, returns a cv2 array
    str -> np.ndarray"""
    if os.path.isfile(path):
        return cv2.imread(path)
    else:
        raise ValueError('You gave incorrect path')
"""
 In image you should give one horizontal rectangle and in that rectangle any style rectangle. But that horizontal rectangle should be bigger one
    Obstacle should be not more than 6
"""

def process_list():
    path = '3.png'
    im = read_img(path)
    k=cv2.flip(im,-1)
    kp=cv2.flip(k,1)

    """INPUTTTTTTTTT"""
    obst=input("No of obstacles ? (Should be less than equal to 6)")
    #obst=6
    # print (obst)

    #cv2.imshow(" kp ",kp)
    gray = cv2.cvtColor(kp, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, bin = cv2.threshold(gray,120,255,1) # inverted threshold (light obj on dark bg)
    bin = cv2.dilate(bin, None)  # fill some holes
    # bin = cv2.dilate(bin, None)
    bin = cv2.erode(bin, None)   # dilate made our shape larger, revert that
    # bin = cv2.erode(bin, None)
    __, contours, hierarchy= cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    TempList=[]
    mylist=[]
    box=list
    my_temp_list = []
    cv2.imshow("kkkk",k)
    cv2.waitKey()
    t=0
    for i in range(int(obst)-1):
        """ Here we are increasing no by 2"""
        t=t+2
        try:
            rc=cv2.minAreaRect(contours[t])
            TempList.insert(i,rc)
        except:
            print("index out of range")
        # print(TempList[i])


    for i in range(int(obst)-1):
        try:
            box=cv2.boxPoints(TempList[i])
            # print ("Points of Contours :- ",i)
            for p in box:
                pt=(p[0],p[1])

                print ("This is pt----------->",pt)
                mylist.append(pt)
                # print (pt)
                cv2.circle(kp,pt,6,(200,0,0),2)
                # new_list = (p[0],p[1])
                # mylist.append(new_list)
        except:
            pass
    cv2.imshow('image',kp)
    cv2.waitKey()
    my_list = [mylist[i * 4:(i + 1) * 4] for i in range((len(mylist) + 4 - 1) // 4)]
    print("?????????", my_list)


    for i in my_list:
        i.append(i[0])


    print("<<<<<<<<<<",my_list)

    return my_list
