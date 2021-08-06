import cv2
import numpy as np
import pose_estimation_module as pm


cap = cv2.VideoCapture(0)
detector = pm.PoseEstimation()

prev_time = 0
counts = 0
direction = 0

while cap.isOpened():
    success, img = cap.read()
    # img = cv2.imread('ai_trainer/2.jpg') # for testing
    img = cv2.resize(img, (img.shape[1]//3, img.shape[0]//3))
    img = detector.find_pose(img, False)
    landmarks = detector.find_positions(img, False)
    if len(landmarks) != 0:
        # right arm
        # detector.find_angle(img, (12, 14, 16)) # not visible in our test examples
        # left arm
        angle = detector.find_angle(img, [11, 13, 15])
        percentage = np.interp(angle, (20, 160), (0, 100))
        if angle >= 150 and direction == 0:
            counts += 0.5
            direction = 1
        if angle <= 30 and direction == 1:
            counts += 0.5
            direction = 0
        print(counts)
        cv2.putText(img, f"counts: {int(counts)}", (40, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.rectangle(img, (40, 250), (70, 450), (0, 0, 255), 2)
        cv2.rectangle(img, (70, 450), (40, 250+2*int(percentage)), (0, 0, 255), cv2.FILLED)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(img, f"fps: {int(fps)}", (40, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('AI Trainer', img)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break