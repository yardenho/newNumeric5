def Lagrange(PointList, x):
    i = 0
    sum = 0
    while i < len(PointList):
        j = 0
        L = 1
        while j < len(PointList):
            if i is not j:
                L *= (x - PointList[j][0]) / (PointList[i][0] - PointList[j][0])
            j += 1
        sum += (L * PointList[i][1])
        i += 1
    return sum


#pointList = [[1, 1], [2, 0], [4, 1.5]]
#print(Lagrange(pointList, 3))

def Linear(PointList, x):
    i = 0
    y = None
    while i < len(PointList) - 1:
        if (x > PointList[i][0]) and (x < PointList[i+1][0]):
            Xi = PointList[i][0]
            XiNext = PointList[i + 1][0]
            Yi = PointList[i][1]
            YiNext = PointList[i + 1][1]
            y = (((Yi - YiNext) / (Xi - XiNext)) * x) + (((YiNext * Xi) - (Yi * XiNext)) / (Xi - XiNext))
        i += 1
    return y


pointList = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
print(Linear(pointList, 3.666))


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




# polynomial method

def polynomial(pointsList, X):
    mat = newMat(len(pointList), len(pointsList))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = pointList[i][0]
    return


def Driver():
    pass