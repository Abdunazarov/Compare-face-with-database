from multiprocessing.connection import wait
from django.test import TestCase


import face_recognition
import cv2
from PIL import Image



# image = Image.open('me.jpg')
# image.show()


# loading both images me and frame
me_img = face_recognition.load_image_file('Dior.png')
me_encoding = face_recognition.face_encodings(me_img)[0]


frame_img = face_recognition.load_image_file('taken_pic.png')
frame_encoding = face_recognition.face_encodings(frame_img)[0]

result = face_recognition.compare_faces([me_encoding], frame_encoding)
print(result)