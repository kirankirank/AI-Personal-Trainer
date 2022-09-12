import cv2
import mediapipe as mp
import numpy as np
import math
po=mp.solutions.pose
p=po.Pose()
dr=mp.solutions.drawing_utils
lo=[23,25,27]
v=cv2.VideoCapture("C:/Users/kiran/Downloads/Pexels Videos 2785531.mp4")
pu=0
dir = 0
while True:
    #global pu
    a,b=v.read()
    RGB=cv2.cvtColor(b, cv2.COLOR_BGR2RGB)
    c=p.process(RGB)
    #print(c.pose_landmarks)
    if c.pose_landmarks:
        #dr.draw_landmarks(b,c.pose_landmarks,po.POSE_CONNECTIONS)
        li=[]
        for id,d in enumerate(c.pose_landmarks.landmark):
            h,w,l=b.shape
            xp,yp=int(d.x*w),int(d.y*h)
            li.append([id,xp,yp])
        
        
        x1,y1=li[lo[0]][1:]
        x2,y2=li[lo[1]][1:]
        x3,y3=li[lo[2]][1:]
        cv2.circle(b,(x1,y1),10,(0,0,255),cv2.FILLED)
        cv2.circle(b,(x1,y1),30,(0,0,255),5)
        cv2.line(b,(x1,y1),(x2,y2),(255,255,255),10)
        cv2.circle(b,(x2,y2),10,(0,0,255),cv2.FILLED)
        cv2.circle(b,(x2,y2),30,(0,0,255),5)
        cv2.line(b,(x2,y2),(x3,y3),(255,255,255),10)
        cv2.circle(b,(x3,y3),10,(0,0,255),cv2.FILLED)
        cv2.circle(b,(x3,y3),30,(0,0,255),5)
        
        
        
        ta=[]
        tanb=math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        print(tanb)
        ta.append(tanb)
        # print(ta)
        pre = np.interp(tanb,(72,170),(0,100)) 
        print(pre,"pre")
        if pre == 100:
            if dir == 0:
                pu = pu+0.5
                dir = 1
        if pre == 0:
            if dir == 1:
                pu = pu+0.5
                dir = 0
            
        cv2.putText(b, str(int(tanb)), (x2-5,y2-5),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,255),5, cv2.LINE_AA)
        cv2.putText(b, str(int(pu)), (500,500),cv2.FONT_HERSHEY_SIMPLEX,10,(255,0,255),10, cv2.LINE_AA)
    #print(pu)    
    ok=cv2.resize(b,(700,600)) 
    cv2.imshow("p",ok)
    if cv2.waitKey(25) & 0xFF == ord('p'):
      break
v.release()
cv2.destroyAllWindows()    

