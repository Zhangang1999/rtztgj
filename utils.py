import cv2
import numpy as np


# 最小外接矩
# 输入数组形式 cnt
# 输出可以为四个角的坐标或者是面积
def min_Area_Rect(cnt):
    # cnt = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # 必须是array数组的形式
    rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
    box = cv2.boxPoints(rect) # 获取最小外接矩形的4个顶点坐标(ps: cv2.boxPoints(rect) for OpenCV 3.x)
    area = cv2.contourArea(box)  #获取最小外接矩形面积的大小
