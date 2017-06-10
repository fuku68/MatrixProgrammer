#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.pardir)
from modules.plotting import plot
from modules import image


data = image.file2image('./images/img01.png')
height = len(data)
S = { x + (height - y) * 1j for y, array in enumerate(data) for x, cell in enumerate(array) if cell[0] < 120 }
plot(S, height, 1) 

# プロセス終了時にファイルが削除されるため入力待ちに
row_input() if sys.version_info < (3, 0, 0) else input()
