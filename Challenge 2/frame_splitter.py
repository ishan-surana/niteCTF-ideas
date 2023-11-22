import cv2
vidcap = cv2.VideoCapture("rr.mp4")
frame_count=1
while True:
    success, frame = vidcap.read()
    if not success:
        break
    filename = f"{frame_count}.jpg"
    cv2.imwrite(filename, frame)
    frame_count += 1
vidcap.release()