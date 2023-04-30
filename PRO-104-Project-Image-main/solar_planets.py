import cv2
image = cv2.imread("poster.jpg")
cv2.imshow("output", img)
gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale", gray_image)
cv2.waitkey(0)
cv2.putText(image, "sun", (20,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.putText(image, "mercury", (50,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.putText(image, "venus", (70,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.putText(image, "earth", (90,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.putText(image, "mars", (100,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.putText(image, "jupiter", (120,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.putText(image, "saturn", (140,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.putText(image, "urnaus", (160,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.putText(image, "neptune", (180,220),
            fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontscale = 1,
            color = (0,0,255))
cv2.imwrite("solar_systemwithname", img)