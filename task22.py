n,m = 14,13
down = """
0 3 0 0 4 3 4 1 2 1 4 4 2 1
4 2 4 4 2 3 4 0 4 4 2 1 0 3
3 3 3 1 2 2 2 3 3 0 3 3 0 4
1 1 2 4 4 4 4 4 2 0 1 0 1 1
0 1 0 3 1 0 3 0 3 3 0 1 0 4
4 2 0 3 0 2 3 4 1 2 4 4 2 1
3 2 2 1 2 0 3 1 1 4 1 1 4 3
1 2 3 4 2 2 4 3 3 3 4 3 0 3
1 2 4 2 3 4 4 2 4 2 2 3 1 2
4 2 0 0 2 4 0 4 0 1 2 2 3 3
0 2 2 0 2 1 4 3 4 0 3 1 1 3
1 2 1 2 0 3 3 4 2 3 2 3 1 4
0 3 0 1 4 3 0 0 4 3 0 1 4 3
4 2 2 0 4 3 0 0 4 4 0 2 0 4
"""
right = """
2 3 1 3 2 1 0 1 1 3 2 2 2
3 0 2 1 0 2 4 1 1 2 3 1 1
2 4 2 0 3 1 4 4 0 3 4 3 3
0 0 3 4 2 0 4 4 2 0 1 0 1
1 0 3 4 0 1 3 1 3 4 0 0 2
1 1 2 4 2 1 0 0 0 3 0 3 1
2 1 4 0 3 4 2 0 4 1 4 3 4
1 0 3 4 3 4 0 1 0 1 2 4 4
2 1 0 0 2 2 2 3 2 3 3 0 2
2 1 3 0 0 3 3 0 4 4 1 2 2
3 0 2 2 3 1 3 0 0 4 1 1 2
4 4 0 0 2 1 2 4 0 4 1 1 2
1 3 4 0 1 3 1 1 0 2 2 3 3
3 4 3 1 3 1 4 3 2 1 1 1 2
0 2 0 2 1 0 4 1 2 4 0 2 0

"""

import sys
def get_score(n, m, down, right):
    down = [[int(i) for i in item.strip().split()] for item in down.strip().split("\n")]
    right = [[int(i) for i in item.strip().split()] for item in right.strip().split("\n")]
    result = [[sys.maxint for j in range(m+1)] for i in range(n+1)]
    result[0][0] = 0
    for i in range(1, n+1):
        result[i][0] = result[i-1][0] + down[i-1][0]
    for j in range(1, m+1):
        result[0][j] = result[0][j-1] + right[0][j-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            result[i][j] = result[i-1][j] + down[i-1][j]
            if result[i][j-1] + right[i][j-1] > result[i][j]:
                result[i][j] = result[i][j-1] + right[i][j-1]
    print(result[-1][-1])

get_score(n, m, down, right)
