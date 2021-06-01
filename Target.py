"""Target.py"""
import math as math


class Target:
    """表示枪点的类"""
    x = 0
    y = 0
    z = 0
    r = 0

    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        if t == 1:
            self.r = 2
        elif t == 2:
            self.r = 4
        elif t == 3:
            self.r = 7
        elif t == 4:
            self.r = 9
        elif t == 0:
            self.r = 0

    def getDose(self, i, j, k):
        """计算枪点在某个像素点产生的辐射强度"""
        distance = math.sqrt(math.pow(i - self.x, 2) +
                             math.pow(j - self.y, 2) + math.pow(k - self.z, 2))

        if self.r == 2:
            lambda1 = 0.649
            lambda2 = 0.600
            r1 = 1.366
            r2 = 2.662
            e1 = 4.413
            e2 = 0.668
        elif self.r == 4:
            lambda1 = 0.401
            lambda2 = 0.649
            r1 = 7.036
            r2 = 4.849
            e1 = 5.702
            e2 = 1.149
        elif self.r == 7:
            lambda1 = 0.363
            lambda2 = 0.658
            r1 = 13.97
            r2 = 8.200
            e1 = 7.197
            e2 = 1.231
        elif self.r == 9:
            lambda1 = 0.382
            lambda2 = 0.653
            r1 = 17.68
            r2 = 10.32
            e1 = 8.195
            e2 = 1.441
        else:
            return 0

        return lambda1 * (1 - math.erf(distance - r1) / e1) + lambda2 + (
                1 - math.erf(distance - r2) / e2)  # return radio

    def conflict_detector(self, target):  # 若冲突返回false，否则返回true
        distance = math.sqrt(math.pow(target.x - self.x, 2) +
                             math.pow(target.y - self.y, 2) + math.pow(target.z - self.z, 2))
        return (self.r + target.r) < distance
