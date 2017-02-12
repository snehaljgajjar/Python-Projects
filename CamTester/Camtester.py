import cv2,time,pandas
video=cv2.VideoCapture(0) #video path / 0 --> for webcam
while True:
    check, frame = video.read()
    cv2.imshow("Color Frame",frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows
