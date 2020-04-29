import cv2 as cv
cap = cv.VideoCapture('vehicles.avi')
ret, frame = cap.read()
print('Select ONE Car and Press ENTER')
ROIs = []
while True:
  ROI = cv.selectROI('MultiTracker', frame)
  ROIs.append(ROI)
  if len(ROIs)<4:
    print("Select Another Car and Press ENTER")
  if len(ROIs)==4:
        print('Enter q')
        k = cv.waitKey(0) & 0xFF== ord('q')
        break
trackerType = "BOOSTING"
multiTracker = cv.MultiTracker_create()
for ROI in ROIs:
  multiTracker.add(cv.TrackerBoosting_create(), frame, ROI)
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    success, boxes = multiTracker.update(frame)
    for i, newbox in enumerate(boxes):
        p1 = (int(newbox[0]), int(newbox[1]))
        p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
        cv.rectangle(frame, p1, p2, (0,0,255), 2, 1)
    cv.imshow('MultiTracker', frame)
    if cv.waitKey(1) & 0xFF == 27:
        break