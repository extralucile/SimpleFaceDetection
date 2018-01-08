# this simple code finds a face on a photo using cv2 and PIL
import cv2
from PIL import Image, ImageDraw

#path to the image
path = 'pablo.jpg'

#load the image as a numpy.ndarray
img_np = cv2.imread(path)

#load the image itself
img = Image.open(path)

#create the detector using opencv
detector = cv2.CascadeClassifier('/home/.../haarcascade_frontalface_default.xml')

#face is a numpy.ndarray defining the face on the image
face = detector.detectMultiScale(img_np)

#draw the rectangle around the face
draw = ImageDraw.Draw(img)
for (x, y, h, w) in face: draw.rectangle([x, y, x+h, y+w])


img.show()
