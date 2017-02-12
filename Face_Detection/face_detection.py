import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")
#Gray scale image is helpful to improve accuracy
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_image,
scaleFactor=1.1,
minNeighbors=5)#smaller value of scaleFactor improve accuracy=1.05 every time descrese image size and find faces
# minNeighbors=5

for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y) , (x+w,y+h) , (0,255,0) , 3)
#img=cv2.rectangle(img, (x,y) , (x+w,y+h) , BGR Value===> (0,255,0) , Rectangle width ==> 3)
print(type(faces))
print(faces)

resized =cv2.resize(img,( int(img.shape[1]/2),int(img.shape[0]/2) )  )

cv2.imshow("Face Detaction",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
