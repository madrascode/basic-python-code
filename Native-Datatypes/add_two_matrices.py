X = [[12, 7, 3],
    [4,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]
# print(len(X))
# print(len(X[0]))
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for i in result:
    print(i)

# comprehension_result = [[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
# for i in comprehension_result:
#     print(i)
# print(comprehension_result)

# transpose of a matrix
traspose_result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(result)):
    for j in range(len(X[0])):
        traspose_result [i][j] = result[j][i]   #  here element in ith column will be placed in jth column and element in jth element will be placed in ith column. 

for i in traspose_result:
    print(i)