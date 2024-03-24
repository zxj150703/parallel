import time


def sum_trivial(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def sum_scalar_optimized(numbers):
    if len(numbers) == 1:
        return numbers[0]

    mid = len(numbers) // 2
    left_sum = sum_scalar_optimized(numbers[:mid])
    right_sum = sum_scalar_optimized(numbers[mid:])

    return left_sum + right_sum


numbers = [1, 2, 3, 4, 5]

# 平凡算法（逐个累加）
total_time_trivial = 0
for _ in range(10000):
    start_time_trivial = time.time()
    result_trivial = sum_trivial(numbers)
    end_time_trivial = time.time()
    total_time_trivial += end_time_trivial - start_time_trivial
print("Total Time for Trivial Algorithm (1000 runs):", total_time_trivial)

# 超标量优化算法（两路链式累加）
total_time_scalar_optimized = 0
for _ in range(10000):
    start_time_scalar_optimized = time.time()
    result_scalar_optimized = sum_scalar_optimized(numbers)
    end_time_scalar_optimized = time.time()
    total_time_scalar_optimized += end_time_scalar_optimized - start_time_scalar_optimized
print("Total Time for Scalar Optimized Algorithm (1000 runs):", total_time_scalar_optimized)
