import cv2

img = cv2.imread(r'C:\Users\buyma\PycharmProjects\opencv-programs-in-python\flower.jpg', 1)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", img)
cv2.waitKey()
cv2.destroyAllWindows()