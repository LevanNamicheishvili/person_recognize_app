import face_recognition
import cv2

image = cv2.imread("image.jpg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


face_locations = face_recognition.face_locations(rgb_image)


for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)


cv2.imshow("Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
