import cv2

img = cv2.imread('Sequences/img.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Test", img)

img = cv2.Sobel(src = img, ddepth = cv2.cv.CV_32F, dx = 1,  dy = 1, ksize = 11)
# img = cv2.Canny(img, 30, 100)

print(img)

cv2.imshow("Test", abs(img))
cv2.waitKey(0)
