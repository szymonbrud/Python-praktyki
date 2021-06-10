import cv2
import numpy as np

# cap = cv2.VideoCapture(0)


allColors = [
    ("czerwony", (170, 100, 20), (180, 255, 255)),
    ("niebieski", (90, 100, 20), (130, 255, 255)),
    ("fjoletowy", (140, 100, 20), (160, 255, 255)),
    ("pomaranczowy", (0, 100, 20), (20, 255, 255)),
    ("zolty", (25, 100, 20), (35, 255, 255)),
    ("zielony", (45, 100, 20), (70, 255, 255))
]


def preprocessTheImg(img):

    chnagedImg = img

    for colorName, colorMin, colorMax in allColors:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, colorMin, colorMax)

        contours, _ = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(
            chnagedImg, contours, -1, (0, 0, 0), 3)

        contours = [cv2.boundingRect(cnt) for cnt in contours]
        # drawing rectangle for each contour for visualising
        for cnt in contours:
            x, y, w, h = cnt
            cv2.putText(chnagedImg, colorName, (x, y), cv2.FONT_HERSHEY_SIMPLEX, .5,
                        (0, 0, 0), 1, cv2.LINE_AA, False)
            # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return chnagedImg


img = cv2.imread('colors.png')

img = preprocessTheImg(img)

cv2.imshow('contours', img)


cv2.waitKey()

# -------------------------------------------------------

# while True:

#     sucess, imgWebcam = cap.read()

#     img = preprocessTheImg(imgWebcam)

#     cv2.imshow('imgStacked', img)
#     cv2.waitKey(1)
