#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {(i-1)*n, i*n, (i+1)*n} 
# {(j-1)*n, j*n, (j+1)*n} 
# -> {(i+j-2)*n, (i+j-1)*n, (i+j)*n, (i+j+1)*n, (i+j+2)*n}
print('>>> {x*y for x in {1,2,4} for y in {8,16,32}}')
print({x*y for x in {1,2,4} for y in {8,16,32}})
