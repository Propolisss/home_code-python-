from PIL import Image
import cv2
import imutils

image_path = (r"C:\Users\Propolisss\Downloads\viktor-vasin_1507715461334424033.jpg")
fixed_width = 400
img = Image.open(image_path)
width_percent = (fixed_width / float(img.size[0]))
height_size = int((float(img.size[0]) * float(width_percent)))

new_image = img.resize((fixed_width, height_size))
#new_image.show()
new_image.save(r"C:\Users\Propolisss\Downloads\viktor-vasin_1507715461334424033.jpg")

img = cv2.imread(r"C:\Users\Propolisss\Downloads\viktor-vasin_1507715461334424033.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3),0)
img_edges = cv2.Canny(img_blur, 10, 250)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
closed = cv2.morphologyEx(img_edges, cv2.MORPH_CLOSE, kernel)

conters = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
conters = imutils.grab_contours(conters)

cv2.drawContours(img, conters, -1, (0, 255, 0), 4)

cv2.imshow('rez', img)
cv2.waitKey()