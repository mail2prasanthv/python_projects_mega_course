#Detecting moving objects
import cv2
import time

video = cv2.VideoCapture(0)# 0 for main camera
time.sleep(1)
first_frame = None;
 
while True:
   
    check, frame = video.read()
    #COLOR_BAYER_BG2GRAY - algorithm to convert to grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    gray_frame_gau = cv2.GaussianBlur(gray, (21,21), 0)
    
    
    if first_frame is None:
        first_frame = gray_frame_gau
    
    delta_frame = cv2.absdiff(first_frame,gray_frame_gau)
    
    cv2.imshow("My Video", delta_frame)
    
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        break
video.release()