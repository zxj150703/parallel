import timeit
import numpy as np

def dot_product_trivial(matrix, vector):
    result = []
    for col in range(matrix.shape[1]):
        col_sum = 0
        for row in range(matrix.shape[0]):
            col_sum += matrix[row][col] * vector[row]
        result.append(col_sum)
    return result

def dot_product_cache_optimized(matrix, vector):
    result = []
    for col in range(matrix.shape[1]):
        col_sum = np.dot(matrix[:, col], vector)  # 使用numpy的dot函数进行优化
        result.append(col_sum)
    return result

# 更新测试数据为10x10的矩阵和1x10的向量
matrix = np.random.randint(1, 10, size=(10, 10))
vector = np.array([i for i in range(1, 11)])

# 测试算法一的执行时间
time_trivial = timeit.timeit(lambda: dot_product_trivial(matrix, vector), number=1000)

# 测试算法二的执行时间
time_cache_optimized = timeit.timeit(lambda: dot_product_cache_optimized(matrix, vector), number=1000)

print("Trivial Algorithm Time:", time_trivial)
print("Cache Optimized Algorithm Time:", time_cache_optimized)
