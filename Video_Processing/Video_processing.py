import cv2,time

video=cv2.VideoCapture("video.mp4") #video path / 0 --> for webcam
"""
for webcam
"""
a=1
while True:
    a= a+1
    check, frame = video.read()
    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(2)
    resized =cv2.resize(gray,( int(gray.shape[1]),int(gray.shape[0]) )  )
    cv2.imshow("Capturing",resized)
    key = cv2.waitKey(1)

    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows

print(a)
