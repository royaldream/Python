import cv2

print(cv2.__version__)
img_black = cv2.imread("bg-39.jpg", 0)
print(img_black.shape)
cv2.imshow("bg-39", img_black)
cv2.waitKey(0)
# cv2.waitKey(2000)
cv2.destroyAllWindows()

img_color = cv2.imread("bg-39.jpg", 1)
print(img_color.shape)
cv2.imshow("bg-39", img_color)
cv2.waitKey(0)
# cv2.waitKey(2000)
cv2.destroyAllWindows()


img_resize=cv2.resize(img_color,(1000,1000))
print(img_resize.shape)
cv2.imshow("bg-39", img_resize)
cv2.waitKey(0)
# cv2.waitKey(2000)
cv2.destroyAllWindows()

