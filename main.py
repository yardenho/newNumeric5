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


#pointList = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
#print(Linear(pointList, 3.666))


def neville(pointsList, m, n, X):
    if m is n:
        return pointsList[m][1]
    else:
        Xm = pointsList[m][0]
        Xn = pointsList[n][0]
        res = (X - Xm) * neville(pointsList, m+1, n, X) - (X - Xn) * neville(pointsList, m, n-1, X)
        res /= (Xn - Xm)
        return res


# polynomial method

def newMat(numRow, numCol):
    """
    :param numRow: the number of rows in the mat
    :param numCol: the number of columns in the mat
    :return: a zero matrix in the required size
    """
    mat = []   # the zero matrix the function returns
    for i in range(numRow):
        mat.append([])    # create a new row
        for j in range(numCol):
            mat[i].append(0)    # fill the row with
    return mat


def iterativGuassSeidel(A, b, epsilon, flagD):
    """
    :param A: a matrix
    :param b: the result vector
    :param epsilon: the mistake
    :param flagD: tell us if the system have dominant diagonal
    :return: None
    """
    flagC = False  # flagC = false if the linear equations does not converge
    x = newMat(len(b), 1)    # create the result vector
    for _ in range(99):    # max number of iterations is 99
        oldX1 = x[0][0]    # copy the old x value of the current iteration
        for i in range(len(x)):   # go over the all variables
            if A[i][i] == 0:   # preventing division by zero
                return None
            temp = b[i][0] / A[i][i]
            for j in range(len(x)):    # calculate the value of the variable in the new iteration
                if i != j:
                    temp -= (A[i][j] * x[j][0]) / A[i][i]
            x[i][0] = temp     # update the calculated value
        if abs(oldX1 - x[0][0]) < epsilon:   # check stop condition
            flagC = True
            break
    if flagC is True:
        return x
    else:
        #print("The system of linear equations does not converge :(")
        return None


def polynomial(pointsList, X):
    mat = newMat(len(pointsList), len(pointsList))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = pow(pointsList[i][0], j)
    b = newMat(len(pointsList), 1)
    for i in range(len(b)):
        b[i][0] = pointsList[i][1]
    matRes = iterativGuassSeidel(mat, b, 0.0001, True)
    # calc mat
    res = 0
    for i in range(len(matRes)):
        res += matRes[i][0] * pow(X, i)
    return res


points = [[1, 0.8415], [2, 0.9093], [3, 0.1411]]
print("polynomial")
#print(polynomial(points, 2.5))


def Driver():
    points = [[1, 1], [2, 4], [3, 9], [4, 16]]
    X = 2.5
    val = input("Choose the method you interest in finding the approximate value of the point:\n"
                "1 - for Linear Interpolation\n2- for Polynomial Interpolation\n3 - for Lagrange Interpolation "
                "\n4 - for Neville Algorithm\nany other number for all the methods\n")
    if val == "1":
        print("==== Linear Interpolation ==== ")
        print("f(" + str(X) + ") = " + str(Linear(points, X)))
    elif val == "2":
        print("==== Polynomial interpolation ==== ")
        print("f(" + str(X) + ") = " + str(polynomial(points, X)))
    elif val == "3":
        print("==== Lagrange Interpolation ==== ")
        print("f(" + str(X) + ") = " + str(Lagrange(points, X)))
    elif val == "4":
        print("==== Neville Algorithm ==== ")
        print("f(" + str(X) + ") = " + str(neville(points, 0, len(points) - 1, X)))
    else:
        print("==== All the methods ==== ")
        print("==== Linear Interpolation ==== ")
        print("f(" + str(X) + ") = " + str(Linear(points, X)))
        print("\n==== Polynomial interpolation ==== ")
        print("f(" + str(X) + ") = " + str(polynomial(points, X)))
        print("\n==== Lagrange Interpolation ==== ")
        print("f(" + str(X) + ") = " + str(Lagrange(points, X)))
        print("\n==== Neville Algorithm ==== ")
        print("f(" + str(X) + ") = " + str(neville(points, 0, len(points) - 1, X)))


Driver()
