# -*- coding: utf-8 -*-

import numpy as np
import cv2
import stereo.camera_config as camera_config

def depth(image, WIDTH, HEIGHT):
  imageL = image[0:HEIGHT, 0:WIDTH//2]
  imageR = image[0:HEIGHT, WIDTH//2:WIDTH]

  #cv2.imshow("imageL", imageL)
  #cv2.imshow("imageR", imageR)

  img1_rectified = cv2.remap(imageL, camera_config.left_map1, camera_config.left_map2, cv2.INTER_LINEAR)
  img2_rectified = cv2.remap(imageR, camera_config.right_map1, camera_config.right_map2, cv2.INTER_LINEAR)  #依据MATLAB测量数据重建无畸变图片

  imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
  imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)  #BGR图像转灰度图

  stereo = cv2.StereoSGBM_create(0, 16, 9)  #立体匹配
  disparity = stereo.compute(imgL, imgR)

  disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)  #归一化函数算法

  return disparity, disp

def distance(disparity):
  threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32)/16., camera_config.Q)  #计算三维坐标数据值

  return threeD
