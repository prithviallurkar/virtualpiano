# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:36:34 2019

@author: Prithvi
"""
import cv2
import math
from playsound import playsound
import numpy as np
#playsound("dha.mp3")

notelow = ["kdha-low.mp3","dha-low.mp3","kni-low.mp3","ni-low.mp3","sa-low.mp3"]
notemid = ["kre.mp3","re.mp3","kga.mp3","ga.mp3","ma.mp3","tma.mp3"]
notehigh = ["pa.mp3","kdha.mp3","dha.mp3","kni.mp3","ni.mp3","sa.mp3"]
cap = cv2.VideoCapture(0)

while (True):
    px = py =0
    x1 = y1 = w1 = h1 = 0
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([99,115,150])
    upper_blue = np.array([110,255,255])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours :
        pass
    else :
        cont_sorted = sorted(contours, key=cv2.contourArea, reverse=True)#[:5]
    
        x1,y1,w1,h1 = cv2.boundingRect(cont_sorted[0])
    
        cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
        px = (int)((2*x1+w1)/2.0)
        py = (int)((2*y1+h1)/2.0)
    
    cv2.putText(frame,"CAM PIANO",(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)    
    cv2.putText(frame,"Low",(50,115),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,255,255),1)    
   
    x = 50
    y = 120
    w = 60
    h = 60
    
    text1 = "dDnNS"
    text2 = "rRgGMm"
    text3 = "PdDnNS"
    
    for i in range(5) :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        cx = (int)((2*x+w)/2.0)
        cy = (int)((2*y+h)/2.0)
        cv2.putText(frame,str(text1[i]),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        if (math.sqrt((px - cx)**2 + (py - cy)**2))<20 :
            playsound(notelow[i])
        x = x+w
        
    y = y+h+60
    x = 50 
    cv2.putText(frame,"High",(x,y),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,255,255),1)
    y = y+5

    for i in range(6) :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        cx = (int)((2*x+w)/2.0)
        cy = (int)((2*y+h)/2.0)
        cv2.putText(frame,str(text2[i]),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        if (math.sqrt((px - cx)**2 + (py - cy)**2))<20 :
            playsound(notemid[i])
        x = x+w 
        
    y = y+h+25
    x = 50  
    
    for i in range(6) :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        cx = (int)((2*x+w)/2.0)
        cy = (int)((2*y+h)/2.0)
        cv2.putText(frame,str(text3[i]),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        if (math.sqrt((px - cx)**2 + (py - cy)**2))<20 :
            playsound(notehigh[i])
        x = x+w 
    
    cv2.imshow('myPiano',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   # time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()    

