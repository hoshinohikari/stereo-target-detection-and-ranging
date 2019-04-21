import cv2
from timeit import default_timer as timer

def timer_first(vid):
    video_FourCC    = int(vid.get(cv2.CAP_PROP_FOURCC))
    video_fps       = vid.get(cv2.CAP_PROP_FPS)
    video_size      = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    accum_time = 0
    curr_fps = 0
    fps = "FPS: ??"
    prev_time = timer()

    return video_FourCC, video_fps, video_size, accum_time, curr_fps, fps, prev_time

def timer_back(accum_time, curr_fps, fps, prev_time, result):
    curr_time = timer()
    exec_time = curr_time - prev_time
    prev_time = curr_time
    accum_time = accum_time + exec_time
    curr_fps = curr_fps + 1
    if accum_time > 1:
        accum_time = accum_time - 1
        fps = "FPS: " + str(curr_fps)
        curr_fps = 0
    cv2.putText(result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.50, color=(255, 0, 0), thickness=2)

    return result
