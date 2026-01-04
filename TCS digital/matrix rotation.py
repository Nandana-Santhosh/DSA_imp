n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

for i in range(n):
    mat.reverse()
for i in mat:
    print(i)