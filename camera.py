# -*- coding: utf-8 -*-

from stereo.ranging import depth, distance
import cv2

def camera(camera_num, WIDTH, HEIGHT):
  cap = cv2.VideoCapture(camera_num)
  if not cap.isOpened():
    raise IOError("Couldn't open webcam or cam")
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

  def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
      print(threeD[y][x])  #设置回传函数，鼠标点击时回传信息

  while True:
    return_value, image = cap.read()
    disparity, disp = depth(image, int(WIDTH), int(HEIGHT))

    threeD = distance(disparity)

    cv2.imshow("depth", disp)

    cv2.setMouseCallback("depth", callbackFunc, None)  #点击depth图触发函数

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()
  cv2.destroyAllWindows()
