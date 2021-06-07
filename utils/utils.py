import cv2
import numpy as np
import torch
import torch.nn as nn
import scipy.misc
import os
import errno
import sys

# tensor to numpy
def to_numpy(tensor):
    if torch.is_tensor(tensor):
        return tensor.cpu().numpy()
    elif type(tensor).__module__ != 'numpy':
        raise ValueError("Cannot convert {} to numpy array"
                         .format(type(tensor)))
    return tensor
# ndarray to torch
def to_torch(ndarray):
    if type(ndarray).__module__ =='numpy':
        return torch.from_numpy(ndarray)
    elif not  torch.is_tensor(ndarray):
        raise ValueError("Cannot convert {} to torch tensor"
                         .format(type(ndarray)))
    return ndarray


def im_to_numpy(img):
    img = to_numpy(img)
    img = np.transpose(img, (1, 2, 0)) # H*W*C
    return  img


#---------------osutils--------------------
def mkdir_p(dir_path):
    try:
        os.makedirs(dir_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
def isfile(fname):
    return os.path.isfile(fname)
def isdir(dirname):
    return os.path.isdir(dirname)
def join(path,*paths):
    return os.path.join(path,*paths)
def add_pypath(path):
    if path not in sys.path:
        sys.path.insert(0,path)




# 最小外接矩
# 输入数组形式 cnt
# 输出可以为四个角的坐标或者是面积
def min_Area_Rect(cnt):
    # cnt = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # 必须是array数组的形式
    rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
    box = cv2.boxPoints(rect) # 获取最小外接矩形的4个顶点坐标(ps: cv2.boxPoints(rect) for OpenCV 3.x)
    area = cv2.contourArea(box)  #获取最小外接矩形面积的大小
