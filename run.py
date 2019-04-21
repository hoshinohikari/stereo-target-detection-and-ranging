# -*- coding: utf-8 -*-

import argparse
from yolo import YOLO
from cache import detect_cam ,detect_video

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

  parser.add_argument(
    "--input", nargs='?', type=str, required=False, default='./path2your_video',
    help = "Video input path"
  )

  FLAGS = parser.parse_args()

  if ("input" in FLAGS):
    print("Video mode")
    detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
  if ("camera" in FLAGS):
    print("Camera mode")
    detect_cam(YOLO(**vars(FLAGS)), FLAGS.camera, FLAGS.width, FLAGS.height, FLAGS.output)
  else:
    print("Must specify at least video_input_path.  See usage with --help.")
