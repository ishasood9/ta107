#ta1 is the inital code
from sre_constants import SUCCESS
import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

#ta2 
tracker = cv2.TrackerGOTURN()
#read first image
returned,img=video.read()

#ta3
#select the bounding box in the image
bbox=cv2.selectROI("Tracking", img, False)

#Initialise the tracker on the img and the bounding box
tracker.init(img,bbox)

print(bbox)

#ta4
def drawBox(img,bbox):
    x,y,w,h= int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


while True:
    check,img = video.read()   
    #ta5
    #update the tracker on img and box
    SUCCESS,bbox =tracker.update(img)

    if SUCCESS:
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)    
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



