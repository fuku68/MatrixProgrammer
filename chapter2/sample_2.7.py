#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.pardir)
from modules.plotting import plot
from modules.vec import Vec

v = Vec({'A','B','C’'}, {'A':1})
for d in v.D:
  if d in v.f:
    print(v.f[d])

# プロセス終了時にファイルが削除されるため入力待ちに
#row_input() if sys.version_info < (3, 0, 0) else input()
