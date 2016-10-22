
## Determinant matrix
def det(m):
    return m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1]) - m[1][0]*(m[0][1]*m[2][2] - m[0][2]*m[2][1]) + m[2][0]*(m[0][1]*m[1][2] - m[0][2]*m[1][1])

x = [[5,-2,1], [0, 3,-1], [2,0,7]]
print(det(x))