def warshall(R,n,k,i,j):
    if(k<0 or i<0 or j<0):
        return
    warshall(R, n, k-1, i, j)
    warshall(R, n, k, i-1, j)
    warshall(R, n, k, i, j-1)

    if(R[i][j] or (R[i][k] and R[k][j])):
        R[i][j]=1

    return R