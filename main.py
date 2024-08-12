import cv2
cam = cv2.VideoCapture(0)

cv2.namedWindow("canny filter")

if cam.read() == False:
    cam.open()

img_counter = 0

while True:
    ret, image = cam.read()
    if not ret:
        print("failed to grab frame")

        # cv2.imshow("test", image)


        # SPACE pressed
    if cv2.waitKey(1) & 0xFF == ord('k'):
        img_name = "canny_image.png"
        grayed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(grayed_image, (5, 5), 0)
        canny_image = cv2.Canny(image, 105, 200)
        cv2.imwrite(img_name, canny_image)
        break

cam.release()
cv2.imshow("canny filter applied", canny_image)
cv2.waitKey(1)

cv2.destroyAllWindows()
