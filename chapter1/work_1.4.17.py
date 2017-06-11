#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
from math import e, pi
sys.path.append(os.pardir)
from modules.plotting import plot

n = 20
w = e ** ((2 * pi * 1j) / 20)
list = { w ** i for i in range(n) }
plot(list, 4)

# プロセス終了時にファイルが削除されるため入力待ちに
row_input() if sys.version_info < (3, 0, 0) else input()
