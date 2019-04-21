# -*- coding: utf-8 -*-

import argparse
from yolo import YOLO
from cache import detect_cam

FLAGS = None

if __name__ == '__main__':
  parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
  '''
  Command line options
  '''
  parser.add_argument(
    "--camera", nargs='?', type=int, required=False, default=0,
    help = "Camera mode, will ignore all positional arguments, please input your camera number"
  )

  parser.add_argument(
    "--width", nargs='?', type=int, default=2560,
    help = "[Optional] Camera width"
  )

  parser.add_argument(
    "--height", nargs='?', type=int, default=960,
    help = "[Optional] Camera height"
  )

  parser.add_argument(
    "--output", nargs='?', type=str, default="",
    help = "[Optional] Video output path"
  )

  FLAGS = parser.parse_args()

  detect_cam(YOLO(**vars(FLAGS)), FLAGS.camera, FLAGS.width, FLAGS.height, FLAGS.output)
