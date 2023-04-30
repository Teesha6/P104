import cv2
image = cv2.imread("poster.jpg")
cv2.imshow("output", img)
gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale", gray_image)
cv2.waitkey(0)