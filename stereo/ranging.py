# -*- coding: utf-8 -*-

import numpy as np
import cv2
import stereo.camera_config as camera_config

numberOfDisparities = ((1280 // 8) + 15) & -16

def depth(image, WIDTH, HEIGHT):
  imageL = image[0:HEIGHT, 0:WIDTH//2]
  imageR = image[0:HEIGHT, WIDTH//2:WIDTH]

  imgL = cv2.cvtColor(imageL, cv2.COLOR_BGR2GRAY)
  imgR = cv2.cvtColor(imageR, cv2.COLOR_BGR2GRAY)  #BGR图像转灰度图

  img1_rectified = cv2.remap(imgL, camera_config.left_map1, camera_config.left_map2, cv2.INTER_LINEAR)
  img2_rectified = cv2.remap(imgR, camera_config.right_map1, camera_config.right_map2, cv2.INTER_LINEAR)  #依据MATLAB测量数据重建无畸变图片

  stereo = cv2.StereoSGBM_create(minDisparity=0, numDisparities=numberOfDisparities, blockSize=9, 
                                 P1=8*1*9*9, P2=32*1*9*9, disp12MaxDiff=1, uniquenessRatio=10, 
                                 speckleWindowSize=100, speckleRange=32, mode=cv2.STEREO_SGBM_MODE_SGBM)
  disparity = stereo.compute(img1_rectified, img2_rectified)

  disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)  #归一化函数算法

  return disparity, disp

def distance(disparity):
  threeD = cv2.reprojectImageTo3D(disparity, camera_config.Q, handleMissingValues=True)
  threeD = threeD * 16

  return threeD
