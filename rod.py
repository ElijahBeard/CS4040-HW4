import time
import matplotlib.pyplot as plt
import numpy as np

prices = {
    1: 1,
    2: 5,
    4: 9,
    6: 17,
    8: 20,
    10: 30,
    12: 36,
    16: 48
}

def sparse_rod_cutting(n, prices):
    r = [0] * (n + 1)
    
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            price = prices.get(i, 0)
            q = max(q, price + r[j - i])
        r[j] = q
    
    return r[n]

def time_execution(n, prices):
    start_time = time.time()
    sparse_rod_cutting(n, prices)
    end_time = time.time()
    return end_time - start_time

lengths = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

execution_times = []
for length in lengths:
    execution_time = time_execution(length, prices)
    execution_times.append(execution_time)

coeffs = np.polyfit(lengths, execution_times, 2)
quadratic_model = np.polyval(coeffs, lengths)

plt.figure(figsize=(10, 6))
plt.plot(lengths, execution_times, marker='o', color='b', linestyle='-', label='Exec Time')
plt.plot(lengths, quadratic_model, color='r', linestyle='--', label='Quadtratic Form')
plt.xlabel('Rod Length (n)', fontsize=14)
plt.ylabel('Execution Time (s)', fontsize=14)
plt.title('Sparse Rod Cutting Algorithm Analysis', fontsize=16)
plt.xscale('linear')
plt.yscale('linear')
plt.grid(True)
plt.xticks(lengths, rotation=45)
plt.legend()
plt.show()