import concurrent.futures

# 定义累加函数
def accumulate(start, end):
    result = 0
    for i in range(start, end):
        result += i
    return result

# 总数
total_num = 10000000
# 使用两路并行累加
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(accumulate, 0, total_num // 2)
    future2 = executor.submit(accumulate, total_num // 2, total_num)
    result = future1.result() + future2.result()
print(f"并行累加结果: {result}")
