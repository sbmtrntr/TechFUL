#py a.py

import cv2

img = cv2.imread("lena.png")

print(img)
print(img.shape)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()