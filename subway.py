import cv2
import pygetwindow as gw
import time
import random

WINDOW_X_POS = 1524
WINDOW_Y_POS = 180
WINDOW_WIDTH = 291
WINDOW_HEIGHT = 854

TITLE = "video_window"

OSU_WINDOW_NAME = "osu!"

def is_in_editor():
    try:
        current_title = gw.getActiveWindow().title
        return OSU_WINDOW_NAME in current_title and ".osu" in current_title or current_title == TITLE
    except:
        return False

while True:
    if is_in_editor():
        cap = cv2.VideoCapture('subway.webm')
        cv2.namedWindow(TITLE, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(TITLE, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.moveWindow(TITLE, WINDOW_X_POS, WINDOW_Y_POS)
        cv2.resizeWindow(TITLE, WINDOW_WIDTH, WINDOW_HEIGHT)
        cv2.setWindowProperty(TITLE, cv2.WND_PROP_TOPMOST, 1)

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        start_frame = random.randint(0, total_frames)
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        while is_in_editor():
            start_time = time.time()
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow(TITLE, frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

            elapsed_time = time.time() - start_time
            delay_time = 0.01 - elapsed_time
            if delay_time > 0:
                time.sleep(delay_time)

        cv2.destroyAllWindows()
        cap.release()

    time.sleep(0.1)
