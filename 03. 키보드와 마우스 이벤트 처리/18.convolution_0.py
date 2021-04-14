import numpy as np

mat0 = np.array([[0,1,0], [1,2,1], [0,1,0]])
mat1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(mat0)
print(mat1)

# 해당 원소끼리 곱한후 더한다
sum = 0
for i in range(3):
	for j in range(3):
		sum += mat0[i,j] * mat1[i,j]

print('sum =', sum)

# 해당 원소끼리 곱
mat_conv = mat0 * mat1
print('mat0 * mat1 =')
print(mat_conv)

# 해당 원소끼리 곱
mat_mul = np.multiply(mat0, mat1)
print('mat_mul')
print(mat_mul)

# 곱한값들의 합
print(mat_mul.sum())