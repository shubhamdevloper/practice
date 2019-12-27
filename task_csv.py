import csv
Matrix = []
with open('matrix1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        Matrix.append(row)

C,R = len(Matrix[0]), len(Matrix)
def path(i,j):
    return i in [0,R+1] or j in [0,C+1] or Matrix[i-1][j-1] == '0'
# add boundary
m = [[[1,0][path(i,j)] for j in range(C+2)] for i in range(R+2)]
q = [(1,i,1) for i in range(1,R+1) if m[i][1]]
v = set()
while q:
    s,i,j = q.pop()
    if (i,j) in v or not m[i][j]:
        continue
    if j == C:
        print(s)
        break
    v.add((i,j))
    q = [(s+1,i-1,j),
         (s+1,i+1,j),
         (s+1,i,j-1),
         (s+1,i,j+1)] + q
