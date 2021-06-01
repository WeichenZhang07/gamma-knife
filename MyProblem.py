"""MyProblem.py"""
import numpy as np
import geatpy as ea
import Target as tg


def sumDoseOutTumor(targets, data):
    answer = 0.0
    for i in 0, 255:
        for j in 0, 255:
            for k in 0, 255:
                if data[i][j][k] == 0:
                    for t in 0, 14:
                        answer = answer + targets[t].getDose()

    return answer  # 返回个体的肿瘤外总剂量


def getNumOfTarget(targets):
    answer = 0
    for i in 0, 14:
        if targets[i].r > 0:
            answer += 1
    return answer


class MyProblem(ea.Problem):
    def __init__(self):
        name = 'MyProblem'
        M = 1;
        maxormins = [1]  # 初始化目标最小最大化标记列表， 1： min； -1： max
        Dim = 12 * 15  # 初始化Dim（决策变量维数）
        varTypes = [1] * Dim  # 初始化决策变量类型， 0： 连续； 1： 离散
        lb = [0] * Dim  # 决策变量下界
        ub = [1] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界
        ubin = [1] * Dim  # 决策变量上边界
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop, data):  # 假定输入的影像学数据都是512*512*512像素，且每个像素的长宽高都是1mm
        Vars = pop.Phen
        for i in range(0, 9):
            targets = [15]
            f = np.array([[0]])  # f 是目标函数结果列向量
            for j in range(0, 14):
                targetVector = Vars[i, j * 5:j * 5 + 5]  # 截取该部分的五个变量
                target = tg.Target(targetVector[0, 0], targetVector[0, 1],
                                   targetVector[0, 2],
                                   0 if targetVector[0, 4] == 0 else targetVector[0, 3])  # 创建一个target实例
                targets[j] = target  # 向target数组中添加一个target点对象
            DNS = sumDoseOutTumor(targets, data)
            N = getNumOfTarget(targets)
            fi = 0.9 * DNS + 0.1 * N  # 通过加权来代表多目标规划
            if i == 0:
                f = np.array([[fi]])
            else:
                f = np.append(f, [[fi]], axis=0)
