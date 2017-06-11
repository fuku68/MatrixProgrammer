#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.pardir)
from modules.plotting import plot

def segment(pt1, pt2):
  num = 100
  # return [[x * ((i * 1.0) / num) + y * ((num - i * 1.0) / num) for i in range(num)] for (x, y) in zip(pt1, pt2)]
  return [[x * ((i * 1.0) / num) + y * ((num - i * 1.0) / num) for (x, y) in zip(pt1, pt2) ]for i in range(num)] 

plot(segment([3.5, 3], [0.5, 1]), 4, 1)

# プロセス終了時にファイルが削除されるため入力待ちに
row_input() if sys.version_info < (3, 0, 0) else input()
