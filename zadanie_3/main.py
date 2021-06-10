import cv2
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)


while True:

    sucess, imgWebcam = cap.read()

    barcodes = pyzbar.decode(imgWebcam)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(imgWebcam, (x, y), (x + w, y + h), (0, 0, 255), 2)

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(imgWebcam, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

    cv2.imshow('imgStacked', imgWebcam)
    cv2.waitKey(1)
