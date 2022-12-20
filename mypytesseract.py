import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('Penstroke/penstroke5.jpg')

custom_config = r'--oem 3 --psm 6'
d = pytesseract.image_to_string(img, config=custom_config)
d2 = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d2['text'])
for i in range(n_boxes):
    if int(d2['conf'][i]) > 60:
        (x, y, w, h) = (d2['left'][i], d2['top'][i], d2['width'][i], d2['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite('results/penstroke/penstroke5.jpg',img)
print(d)