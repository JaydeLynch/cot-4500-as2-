
# Neville's method for polynomial interpolation\
def neville_method(x, y, target):\
    n = len(x)\
    Q = np.zeros((n, n))\
    Q[:, 0] = y  # Initialize the first column with y values\
    \
    for i in range(1, n):\
        for j in range(1, i + 1):\
            Q[i, j] = ((target - x[i - j]) * Q[i, j - 1] - (target - x[i]) * Q[i - 1, j - 1]) / (x[i] - x[i - j])\
    \
    return Q[n - 1, n - 1]  # Return the interpolated value\
\
# Newton's forward method for polynomial approximation\
def newton_forward(x, y, target):\
    n = len(x)\
    F = np.zeros((n, n))\
    F[:, 0] = y  # Initialize the first column with y values\
    \
    # Compute divided differences\
    for i in range(1, n):\
        for j in range(1, i + 1):\
            F[i, j] = (F[i, j - 1] - F[i - 1, j - 1]) / (x[i] - x[i - j])\
    \
    # Evaluate the polynomial at the target point\
    result = 0\
    for i in range(n):\
        term = F[i, i]\
        for j in range(i):\
            term *= (target - x[j])\
        result += term\
    \
    return result\
\
# Divided difference method for Hermite interpolation\
def divided_difference(x, y, y_prime):\
    n = len(x)\
    F = np.zeros((2 * n, 2 * n))\
    \
    # Initialize the table\
    for i in range(n):\
        F[2 * i, 0] = x[i]\
        F[2 * i + 1, 0] = x[i]\
        F[2 * i, 1] = y[i]\
        F[2 * i + 1, 1] = y[i]\
        F[2 * i + 1, 2] = y_prime[i]\
    \
    # Compute divided differences\
    for i in range(2, 2 * n):\
        for j in range(2, i + 1):\
            F[i, j] = (F[i, j - 1] - F[i - 1, j - 1]) / (F[i, 0] - F[i - j + 1, 0])\
    \
    return F\
\
# Cubic spline interpolation\
def cubic_spline(x, y):\
    n = len(x)\
    h = np.diff(x)  # Differences between x values\
    A = np.zeros((n, n))\
    b = np.zeros(n)\
    \
    # Set up the tridiagonal matrix A\
    A[0, 0] = 1\
    A[-1, -1] = 1\
    \
    for i in range(1, n - 1):\
        A[i, i - 1] = h[i - 1]\
        A[i, i] = 2 * (h[i - 1] + h[i])\
        A[i, i + 1] = h[i]\
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])\
    \
    # Solve for c coefficients\
    c = np.linalg.solve(A, b)\
    d = np.zeros(n - 1)\
    b_coeff = np.zeros(n - 1)\
    \
    # Compute b and d coefficients\
    for i in range(n - 1):\
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])\
        b_coeff[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3\
    \
    return A, b, c\
\
if __name__ == "__main__":\
    # Question 1: Neville's method\
    x1 = [3.6, 3.8, 3.9]\
    y1 = [1.675, 1.436, 1.318]\
    target1 = 3.7\
    result1 = neville_method(x1, y1, target1)\
    print(f"Question 1: \{result1\}")\
    \
    # Question 2: Newton's forward method\
    x2 = [7.2, 7.4, 7.5, 7.6]\
    y2 = [23.5492, 25.3913, 26.8224, 27.4589]\
    target2 = 7.3\
    result2 = newton_forward(x2, y2, target2)\
    print(f"Question 2: \{result2\}")\
    \
    # Question 3: Approximate f(7.3)\
    result3 = newton_forward(x2, y2, 7.3)\
    print(f"Question 3: \{result3\}")\
    \
    # Question 4: Divided difference method\
    x4 = [3.6, 3.8, 3.9]\
    y4 = [1.675, 1.436, 1.318]\
    y_prime4 = [-1.195, -1.188, -1.180]\
    result4 = divided_difference(x4, y4, y_prime4)\
    print("Question 4:")\
    print(result4)\
    \
    # Question 5: Cubic spline interpolation\
    x5 = [2, 5, 8, 10]\
    y5 = [3, 5, 7, 9]\
    A, b, c = cubic_spline(x5, y5)\
    print("Question 5:")\
    print("Matrix A:")\
    print(A)\
    print("Vector b:")\
    print(b)\
    print("Vector c:")\
    print(c)}
