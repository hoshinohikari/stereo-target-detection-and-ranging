# -*- coding: utf-8 -*-

from stereo.ranging import depth, distance
import cv2
import numpy as np
import random

randomnum = 20

def Get_Average(list):
    sum = 0
    for item in list:
        sum += item
    return sum/len(list)

def camera(frame, HEIGHT, WIDTH, yolo):
    onject = frame[0:HEIGHT, 0:WIDTH//2]
    result, out_boxes, colors = yolo.detect_image(onject)
    disparity, disp = depth(frame, int(WIDTH), int(HEIGHT))
    threeD = distance(disparity)
    isize = frame.shape
    randomnum = 20
    cv2.imshow("depth", disp)
            
    def callbackFunc(e, x, y, f, p):
        if e == cv2.EVENT_LBUTTONDOWN:
            i = 0
            j = 0
            average_three = []
            while(i < randomnum):
                ran1 = random.randint(-20,21)
                ran2 = random.randint(-20,21)
                x_r = x + ran1
                y_r = y + ran2

                if (x_r > 1279):
                    x_r = 1279
                if (y_r > 959):
                    y_r = 959

                if (disp[y_r, x_r] >= 20):
                    average_three.append(threeD[y_r][x_r][2])
                    i = i + 1
                    #print('point is [{}, {}] threeD is {}'.format(x_r, y_r, threeD[y_r][x_r]))
                
                if (j > 50):
                    break

                j = j + 1

            for c in range(len(average_three)):
                if (average_three[c] > Get_Average(average_three) * 1.5):
                    average_three.pop(c)
            print('right point is [{}, {}] threeD is {}'.format(x, y, threeD[y][x]))
            print('average_three is {}'.format(Get_Average(average_three)))  #设置回传函数，鼠标点击时回传信息

        cv2.setMouseCallback("depth", callbackFunc, None)  #点击depth图触发函数

    '''for c in range(len(out_boxes)):
        box = out_boxes[c]
        top, left, bottom, right = box
        top = max(0, np.floor(top + 0.5).astype('int32'))
        left = max(0, np.floor(left + 0.5).astype('int32'))
        bottom = min(isize[0], np.floor(bottom + 0.5).astype('int32'))
        right = min(isize[1], np.floor(right + 0.5).astype('int32'))

        i = 0
        average_three = []
        while(i < randomnum):
            ran1 = random.randint(-20,21)
            ran2 = random.randint(-20,21)

            x_r = (left + right) // 2 + ran1
            y_r = (top + bottom) // 2 + ran2

            if (disp[y_r, x_r] >= 20):
                average_three.append(threeD[y_r][x_r][2])
                i = i + 1

        print('average_three is {}'.format(Get_Average(average_three)))'''

    return result