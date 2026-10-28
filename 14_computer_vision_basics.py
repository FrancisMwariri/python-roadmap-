"""
Python Lesson 14: Computer Vision Basics

This lesson introduces how Python can process camera images.

We will learn:
- OpenCV basics
- webcam capture
- image shapes
- color channels
- drawing on images
"""

import cv2

# ------------------------------------------------------
# 1) Open a webcam
# ------------------------------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera could not be opened.")
    raise SystemExit

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to read frame from camera.")
        break

    # Flip the image horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # --------------------------------------------------
    # 2) Get image dimensions
    # --------------------------------------------------
    height, width, channels = frame.shape
    print(f"Frame size: {width} x {height}, channels={channels}")

    # --------------------------------------------------
    # 3) Draw shapes on the frame
    # --------------------------------------------------
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
    cv2.circle(frame, (500, 200), 60, (0, 0, 255), 2)
    cv2.line(frame, (0, 0), (width, height), (255, 0, 255), 2)

    # --------------------------------------------------
    # 4) Add text
    # --------------------------------------------------
    cv2.putText(
        frame,
        "Camera Preview",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
    )

    # Show the image
    cv2.imshow("Webcam Preview", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# ------------------------------------------------------
# Summary
# In this lesson we learned:
# - how to open a webcam with OpenCV
# - how image dimensions and channels work
# - basic drawing on frames
# - how to preview camera input
# ------------------------------------------------------
