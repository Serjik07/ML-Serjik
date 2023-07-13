import numpy as np

arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[1,2,3],[4,5,6]])
x = [1,2,3,4,5,6]
y = [[1,2,3],[4,5,6]]


print(arr1d)
print(arr2d)


print(arr1d[0])
print(arr1d[1:4])


math_arr1 = np.array([1,2,3])
math_arr2 = np.array([4,5,6])

print(math_arr1 + math_arr2)
print(math_arr1 * math_arr2)









arr_r = np.array([1,2,3,4,5,6])

print(arr_r.reshape(2,3))








arr_s = np.array([1,2,3,4,5,6])

print("Mean: ", arr_s.mean())
print("Max: ", arr_s.max())
print("Sum: ", arr_s.sum())
print(np.array_equal(math_arr1, math_arr2))














