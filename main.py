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
        res = (X - pointsList[m][0]) * neville(pointsList, m+1, n, X) - (X - pointsList[n][0]) * neville(pointsList, m, n-1, X)
        res /= (pointsList[n][0] - pointsList[m][0])
        return res


points = [[1, 1], [2, 4], [3, 9], [4, 16]]
print(neville(points, 0, 3, 2.2))

