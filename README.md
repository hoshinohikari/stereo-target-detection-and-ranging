# stereo-target-detection-and-ranging

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

A gadget that uses a stereo camera for target recognition and ranging, both working in sync and marked on the map.
Nanchang Aviation University Graduation design work in 2019.

## Todo
1. At present, stereo ranging uses SGBM in OpenCV, and object detection uses keras-yolo3.
2. In the future, stereo matching may be replaced with PSMNet.

## Progressing
1. The distance measurement section is currently complete.

---

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
