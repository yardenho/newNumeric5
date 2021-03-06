"""
    git: https://github.com/yardenho/newNumeric5.git
"""

"""
Team - members:
Yarden Hovav, 318230653
Chen Ben Tolila, 207278029
"""

"""       *** Lagrange ****       """


def Lagrange(PointList, x):
    """
    :param PointList: a list of points (that represent points in a function)
    :param x: an x value in the function for it we want to find the y value
    :return: a proximity of f(x)
    """
    i = 0          # index for going over the points
    sum = 0        # the sum of the polynomials we will create from the points
    while i < len(PointList):      # going over the points list
        j = 0      # start from the first point
        L = 1      # the polynomial of the current point
        while j < len(PointList):  # go over the points list
            if i is not j:         # if it's not the same point
                L *= (x - PointList[j][0]) / (PointList[i][0] - PointList[j][0])
            j += 1     # move forward to the next point
        sum += (L * PointList[i][1])    # add the polynomial to the sum of polynomials
        i += 1     # move forward to the
    return sum     # f(x)


"""       *** Linear ****       """


def Linear(PointList, x):
    """
    :param PointList: a list of points
    :param x: an x value for it we want to find the y value in the function
    :return: a proximity of f(x)
    """
    i = 0    # index for the points list
    y = None   # y = none if the x value isn't in the range of the points list
    while i < len(PointList) - 1:   # go over the points list
        if (x >= PointList[i][0]) and (x <= PointList[i+1][0]):  # if x is between the current two points in the list
            Xi = PointList[i][0]    # the x value of the start point of the range
            XiNext = PointList[i + 1][0]   # the x value of the end point of the range
            Yi = PointList[i][1]    # the y value of the start point of the range
            YiNext = PointList[i + 1][1]   # the y value of the end point of the range
            y = (((Yi - YiNext) / (Xi - XiNext)) * x) + (((YiNext * Xi) - (Yi * XiNext)) / (Xi - XiNext))   # create a line between the two points and finad the value of y for the requested x in that line
        i += 1   # move to the the next two points
    return y


"""       *** Neville ****       """


def neville(pointsList, m, n, X):
    """
    :param pointsList: a list of points
    :param m: the start point index
    :param n: the end point index
    :param X: an x value for it we want to find the y value in the function that is created from the given points
    :return: a proximity of f(x)
    """
    if m is n:  # the start index and end index are the same (the same point)
        return pointsList[m][1]   # return the y value of the point
    else:
        Xm = pointsList[m][0]  # the start point x value
        Xn = pointsList[n][0]  # the end point x value
        res = (X - Xm) * neville(pointsList, m+1, n, X) - (X - Xn) * neville(pointsList, m, n-1, X)
        res /= (Xn - Xm)
        return res   # the result (f(X))


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
    if flagC is True:  # linear equations does converge
        return x
    else:
        print("no result when using iterative Guass Seidel in order to solve the matrix")
        return None


# dominant diagonal part

def copyMat(A):
    """
    :param A: a matrix
    :return: a copy of the matrix
    """
    B = newMat(len(A), len(A[0]))  # create a zero matrix of the same size as A
    for i in range(len(A)):   # copy A
        for j in range(len(A[0])):
            B[i][j] = A[i][j]
    return B


def createDominantDiagonal(A, b=None):
    """
    :param A: a coefficients matrix
    :param b: the column vector of constant terms.
    :return: matrix A with dominant diagonal
    """
    max = 0   # the max value in the current row or column in the matrix
    maxIndex = 0  # the index of the max value
    for i in range((len(A))):  # calc the max value for each member on the main diagonal
        sum = 0  # the sum of the members in the current row in A
        for j in range(len(A)):  # go over the current row
            sum += abs(A[i][j])   # add the value of each member in the row
            if abs(A[i][j]) > max:   # search for the max value in the current row
                max = abs(A[i][j])
                maxIndex = j
        if (sum - max) <= max:   # if the max value in the row meets the condition of a dominant diagonal
            A = manualSwapCol(A, maxIndex, i)   # swap between the columns of the current value on the main diagonal and the max value in that row
        else:  # look for the max value in the current column
            max = 0
            maxIndex = 0
            for j in range(len(A)):   # go over the current column
                # sum += abs(A[j][i])
                if abs(A[j][i]) > max:  # search for the max value in the current column
                    max = abs(A[j][i])
                    maxIndex = j
            if rowSum(A[j]) - max <= max:    # if the max value in the row meets the condition of a dominant diagonal
                A, b = manualSwapRow(A, b, i, maxIndex)   # swap between the rows of the current value on the main diagonal and the max value in that column
            else:
                print("No dominant diagonal")   # A can't be changed into dominant diagonal matrix
                return None, None
    return A, b


def manualSwapRow(a, b, r1, r2):
    """
    manaul rows exchange (without e)
    :param a: The coefficient matrix
    :param b:  The column vector of constant terms
    :param r1: the first row to swap
    :param r2: the second row to swap
    :return: the matrix after the swap, The column vector of constant terms after swap
    """

    if r2 < len(a) and r1 < len(a):
        temp = a[r1]
        a[r1] = a[r2]
        a[r2] = temp
        if b is not None:  # if the result vector is not none swap him too
            temp = b[r1]
            b[r1] = b[r2]
            b[r2] = temp
    return a, b


def manualSwapCol(a, c1, c2):
    """
    :param a: The coefficient matrix
    :param c1: the first column to swap
    :param c2: the second column to swap
    :return: the matrix after the swap
    """
    if c2 < len(a) and c1 < len(a):
        for i in range(len(a)):
            temp = a[i][c1]
            a[i][c1] = a[i][c2]
            a[i][c2] = temp
    return a


def rowSum(line):
    """
    :param line: A list od numbers - line for the matrix
    :return: the sum of all the numbers in abs  in the list
    """
    lineSum = 0
    for index in range(len(line)):  # run over all the line`s members
        lineSum += abs(line[index])
    return lineSum

# end dominant part


def polynomial(pointsList, X):
    """
    :param pointsList: the list of the points
    :param X: the point that we want to find her approximate value
    :return: the approximate value of X
    """
    mat = newMat(len(pointsList), len(pointsList))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = pow(pointsList[i][0], j)  # The coefficient matrix
    b = newMat(len(pointsList), 1)
    for i in range(len(b)):
        b[i][0] = pointsList[i][1]  # The column vector of constant terms
    # check
    copyM = copyMat(mat)
    copyB = copyMat(b)
    copyM, copyB = createDominantDiagonal(copyM, copyB)  # change the matrix to be with dominant diagonal
    if (copyM is not None) and (copyB is not None):  # check if the return matrices are not none
        mat = copyM
        b = copyB
    # end check
    matRes = iterativGuassSeidel(mat, b, 0.0001, True)  # returns the solution matrix
    # calc mat
    if matRes is not None:
        res = 0
        for i in range(len(matRes)):
            res += matRes[i][0] * pow(X, i)  # calc the y value for the requested x
        return res
    return None


def Driver():
    # points = [[0, 0],
    #           [1, 0.8415],
    #           [2, 0.9093],
    #           [3, 0.1411],
    #           [4, -0.7568],
    #           [5, -0.9589],
    #           [6, -0.2794]]
    # X = 2.5
    points = [[0, 0], [1, 1], [2, 4], [3, 9]]
    X = 1.5
    val = input("Choose the method you interest in finding the approximate value of the point:\n"
                "1 - for Linear Interpolation\n2 - for Polynomial Interpolation\n3 - for Lagrange Interpolation "
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
        if len(points) >= 4:
            print("==== Neville Algorithm ==== ")
            print("f(" + str(X) + ") = " + str(neville(points, 0, len(points) - 1, X)))
        else:
            print("can't perform neville algorithm for less than 4 points")
    else:
        print("==== All the methods ==== ")
        print("==== Linear Interpolation ==== ")
        print("f(" + str(X) + ") = " + str(Linear(points, X)))
        print("\n==== Polynomial interpolation ==== ")
        print("f(" + str(X) + ") = " + str(polynomial(points, X)))
        print("\n==== Lagrange Interpolation ==== ")
        print("f(" + str(X) + ") = " + str(Lagrange(points, X)))
        print("\n==== Neville Algorithm ==== ")
        if len(points) >= 4:
            print("f(" + str(X) + ") = " + str(neville(points, 0, len(points) - 1, X)))
        else:
            print("can't perform neville algorithm for less than 4 points")


Driver()
