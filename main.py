import geatpy as ea
import numpy as np

Nind = 10
Encoding = 'BG'
lens = [9, 9, 9, 2, 1] * 15
lb = [0, 0, 0, 0, 0] * 15
ub = [512, 512, 512, 4, 1] * 15
codes = [0] * 15 * 30
scales = [0] * 15 * 30
lbin = [1] * 12 * 15
vbin = [1] * 12 * 15
varTypes = [0] * 12 * 15

FieldD = np.array([lens, lb, ub, codes, scales, lbin, vbin, varTypes])
print(1)
