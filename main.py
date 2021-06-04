def Lagrange(PointList, x):
    i = 0
    while i < len(PointList):
        j=0
        sum = 0
        L = 1
        while j < len(PointList):
            if i is not j:
                L *= (x - PointList[j][0]) / (PointList[i][0] - PointList[j][0])
        sum += L
    return sum

pointList = [[1, 1], [2, 0], [4, 1.5]]
print(Lagrange(pointList, 3))
