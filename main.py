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
#print(Lagrange(pointList, 3))


def neville(pointsList, m, n, X):
    if m is n:
        return pointsList[m][1]
    else:
        Xm = pointsList[m][0]
        Xn = pointsList[n][0]
        res = (X - Xm) * neville(pointsList, m+1, n, X) - (X - Xn) * neville(pointsList, m, n-1, X)
        res /= (Xn - Xm)
        return res


points = [[1, 1], [2, 4], [3, 9], [4, 16]]
print(neville(points, 0, 3, 2.2))


def polynomial(pointsList, X):
    return
