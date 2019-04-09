# stereo-target-detection-and-ranging

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

****
|Author|HoshinoKun|
|---|---
|E-mail|hoshinokun@346pro.club
****

## Introduction

A gadget that uses a stereo camera for target recognition and ranging, both working in sync and marked on the image.  
The combined work based on the two projects of [hoshinohikari/keras-yolo3-py2](https://github.com/hoshinohikari/keras-yolo3-py2) and [hoshinohikari/Double-target](https://github.com/hoshinohikari/Double-target)  
Nanchang Aviation University Graduation design work in 2019.  

## Todo
1. At present, stereo ranging uses SGBM in OpenCV, and object detection uses keras-yolo3.
2. In the future, stereo matching may be replaced with PSMNet.

## Progressing
1. The distance measurement section is currently complete.

---

## Some thing you need to do before you start

1. Buy or make a stereo camera,and test out its map, you can refer to my github([hoshinohikari/Double-target](https://github.com/hoshinohikari/Double-target))
2. Install the conda like minoconda or anaconda,and install  
```
Keras
Tensorflow
OpenCV
Opencv-contrib-python
```

## Quick Start

1. Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
2. Convert the Darknet YOLO model to a Keras model.
3. Run YOLO detection.

```
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```

For Tiny YOLOv3, just do in a similar way, just specify model path and anchor path with `--model model_file` and `--anchors anchor_file`.

### Usage
```
usage: run.py [-h] [--camera [CAMERA]] [--width [WIDTH]] [--height [HEIGHT]]
              [--output [OUTPUT]]

optional arguments:
  -h, --help         show this help message and exit
  --camera [CAMERA]  Camera mode, will ignore all positional arguments, please
                     input your camera number
  --width [WIDTH]    [Optional] Camera width
  --height [HEIGHT]  [Optional] Camera height
  --output [OUTPUT]  [Optional] Video output path
```

## Some issues to know

1. The test environment is
    - Python 2.7.15(Miniconda)
    - Keras 2.1.6
    - tensorflow 1.12.0
    - OpenCV 3.4.4
or
    - Python 3.6.8(Miniconda)
    - Keras 2.1.6
    - tensorflow 1.12.0
    - OpenCV 3.4.4

2. Theoretically supports multi-GPU, but I can't test it, so I didn't add this option.
