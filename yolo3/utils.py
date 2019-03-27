"""Miscellaneous utility functions."""

from functools import reduce

from PIL import Image
import numpy as np
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb
import cv2

def compose(*funcs):
  """Compose arbitrarily many functions, evaluated left to right.

  Reference: https://mathieularose.com/function-composition-in-python/
  """
  # return lambda x: reduce(lambda v, f: f(v), funcs, x)
  if funcs:
    return reduce(lambda f, g: lambda *a, **kw: g(f(*a, **kw)), funcs)
  else:
    raise ValueError('Composition of empty sequence not supported.')

def letterbox_image(image, size):
  '''resize image with unchanged aspect ratio using padding'''
  isize = image.shape
  ih = isize[0]
  iw = isize[1]
  #iw, ih = image.size
  w, h = size
  scale = min(float(w)/iw, float(h)/ih)
  nw = int(iw*scale)
  nh = int(ih*scale)

  image = cv2.resize(image, (nw, nh), interpolation = cv2.INTER_CUBIC)
  #image = image.resize((nw,nh), Image.BICUBIC)
  img = np.zeros((h, w), dtype = np.uint8)
  new_image = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
  new_image[:,:,0] = 128
  new_image[:,:,1] = 128
  new_image[:,:,2] = 128
  #new_image = Image.new('RGB', size, (128,128,128))
  new_image[(h-nh)//2:(h-nh)//2+nh, (w-nw)//2:(w-nw)//2+nw] = image
  #new_image.paste(image, ((w-nw)//2, (h-nh)//2))
  return new_image
