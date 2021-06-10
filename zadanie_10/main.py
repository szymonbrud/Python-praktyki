import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)

headTobiasz = cv2.imread('tobiaszHead.png')

# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    s_img = headTobiasz
    l_img = img
    for (x, y, w, h) in faces:
        print(w)
        if w:
            s_img = cv2.resize(s_img, (w, h))
            x_offset = x
            y_offset = y
            l_img[y_offset:y_offset+s_img.shape[0],
                  x_offset:x_offset+s_img.shape[1]] = s_img

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display

    cv2.imshow('img', l_img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release the VideoCapture object
cap.release()
