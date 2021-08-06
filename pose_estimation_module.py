import cv2
import mediapipe as mp
import time
import math
import numpy as np


class PoseEstimation:
    def __init__(self, mode=False, model=1, smooth_landmarks=True, detection_confidence=0.5, track_confidence=0.5):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(mode, model, smooth_landmarks, detection_confidence, track_confidence)
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None
        self.landmarks = []
    def find_pose(self, img, draw=True):
        img = cv2.resize(img, (1200,600))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        # print(self.results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mp_draw.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        return img

    def find_positions(self, img, draw=True):
        self.landmarks = []
        height, width, channels = img.shape
        if self.results.pose_landmarks:
            for lm_id, landmark in enumerate(self.results.pose_landmarks.landmark):
                cx, cy = int(landmark.x * width), int(landmark.y * height)
                self.landmarks.append([lm_id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255,0,0), cv2.FILLED)

        return self.landmarks

    def find_angle(self, img, points, draw=True):
        # get the landmarks
        x1, y1 = self.landmarks[points[0]][1:]
        x2, y2 = self.landmarks[points[1]][1:]
        x3, y3 = self.landmarks[points[2]][1:]
        a = np.array([x1, y1])
        b = np.array([x2, y2])
        c = np.array([x3, y3])
        # calculate the angle
        ba = a - b
        bc = c - b
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba, 2) * np.linalg.norm(bc, 2))
        angle_rad = np.arccos(cosine_angle)
        angle = np.degrees(angle_rad)

        if draw:
            cv2.line(img, (x1,y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2+40, y2),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle


def main():
    cap = cv2.VideoCapture('pose_videos/2.mp4')
    prev_time = 0
    while cap.isOpened():
        ret, img = cap.read()
        pose_detector = PoseEstimation()
        img = pose_detector.find_pose(img)
        #landmarks = pose_detector.find_positions(img)
        #print(landmarks)
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        cv2.putText(img, str(int(fps)), (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)
        cv2.imshow('pose estimation', img)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()