import numpy as np
import time

# 定义数组大小
n = 10000
# 创建一个大数组
array = np.random.rand(n, n)

# 连续访问
start_time = time.time()
sum_sequential = 0
for i in range(n):
    for j in range(n):
        sum_sequential += array[i][j]
end_time = time.time()
print(f"连续访问时间: {end_time - start_time} 秒")

# 随机访问
start_time = time.time()
sum_random = 0
indices = np.random.permutation(n)
for i in indices:
    for j in indices:
        sum_random += array[i][j]
end_time = time.time()
print(f"随机访问时间: {end_time - start_time} 秒")
