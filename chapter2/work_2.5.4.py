#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.pardir)
from modules.plotting import plot

def scalar_vector_mult(alpha, v):
  return [alpha*v[i] for i in range(len(v))]

L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]

plot([scalar_vector_mult(-0.5, scalar_vector_mult(0.5, v)) for v in L], 4)

# プロセス終了時にファイルが削除されるため入力待ちに
row_input() if sys.version_info < (3, 0, 0) else input()
