# -*-coding:utf-8-*-

# 画盘子
import math
from turtle import penup, setpos, pendown


def plate(a, b, angle, steps, rotateAngle):
    minAngle = (2 * math.pi / 360) * angle / steps
    rotateAngle = rotateAngle / 360 * 2 * math.pi
    penup() # 起笔
    setpos(b * math.sin(rotateAngle), -b * math.cos(rotateAngle))
    pendown() # 落笔
    for i in range(steps):
        nextPoint = [a * math.sin((i + 1) * minAngle), -b * math.cos((i + 1) * minAngle)]
        nextPoint = [nextPoint[0] * math.cos(rotateAngle) - nextPoint[1] * math.sin(rotateAngle),
                     nextPoint[0] * math.sin(rotateAngle) + nextPoint[1] * math.cos(rotateAngle)]
        setpos(nextPoint)

