# -*- coding: utf-8 -*-

from stereo.ranging import depth, distance
import cv2

def camera(image, WIDTH, HEIGHT):
  def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
      print(threeD[y][x])  #设置回传函数，鼠标点击时回传信息

  disparity, disp = depth(image, int(WIDTH), int(HEIGHT))

  threeD = distance(disparity)

  #cv2.imshow("depth", disp)

  cv2.setMouseCallback("depth", callbackFunc, None)  #点击depth图触发函数

  return disp, threeD
