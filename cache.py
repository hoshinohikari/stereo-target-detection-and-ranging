import cv2
from timer import timer_first, timer_back
from stereo.ranging import depth, distance
import numpy as np
from camera import camera

def detect_video(yolo, video_path, output_path=""):
    vid = cv2.VideoCapture(video_path)

    video_FourCC, video_fps, video_size, accum_time, curr_fps, fps, prev_time = timer_first(vid)

    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video")
    isOutput = True if output_path != "" else False
    if isOutput:
        #print("!!! TYPE:", type(output_path), type(video_FourCC), type(video_fps), type(video_size))
        out = cv2.VideoWriter(output_path, video_FourCC, video_fps, video_size)
    
    HEIGHT = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    WIDTH = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

    while True:
        return_value, frame = vid.read()
        
        result = camera(frame, HEIGHT, WIDTH, yolo)

        result = timer_back(accum_time, curr_fps, fps, prev_time, result)

        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.imshow("result", result)
        if isOutput:
            out.write(result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    yolo.close_session()

def detect_cam(yolo, camera_num, WIDTH, HEIGHT, output_path=""):
    vid = cv2.VideoCapture(camera_num)

    video_FourCC, video_fps, video_size, accum_time, curr_fps, fps, prev_time = timer_first(vid)

    vid.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    if not vid.isOpened():
        raise IOError("Couldn't open webcam or video")
    isOutput = True if output_path != "" else False
    if isOutput:
        #print("!!! TYPE:", type(output_path), type(video_FourCC), type(video_fps), type(video_size))
        out = cv2.VideoWriter(output_path, video_FourCC, video_fps, video_size)

    while True:
        return_value, frame = vid.read()
        
        result = camera(frame, HEIGHT, WIDTH, yolo)

        result = timer_back(accum_time, curr_fps, fps, prev_time, result)

        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.imshow("result", result)
        if isOutput:
            out.write(result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    yolo.close_session()
    vid.release()
    cv2.destroyAllWindows()
