import cv2
cam = cv2.VideoCapture(0)

cv2.namedWindow("canny filter")

img_counter = 0

ret, image = cam.read()
if not ret:
    print("failed to grab frame")

    cv2.imshow("test", image)

    k = cv2.waitKey(1)

    # SPACE pressed
    img_name = "canny_image.png"
    grayed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(grayed_image, (5, 5), 0)
    canny_image = cv2.Canny(image, 105, 200)
    cv2.imwrite(img_name, canny_image)

cam.release()
cv2.imshow("canny filter applied", canny_image)
cv2.waitKey(1)

cv2.destroyAllWindows()