import time
import matplotlib.pyplot as plt
import numpy as np

def coin_change(coins, amount):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]
    return ways[amount]

coins_usd = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000]
amounts_usd = [10, 50, 100, 500, 1000, 1500, 2000, 3000, 5000]

run_times_usd = []

for amount in amounts_usd:
    start_time = time.time()
    coin_change(coins_usd, amount)
    end_time = time.time()
    run_times_usd.append(end_time - start_time)

amounts_usd_str = [str(amount) for amount in amounts_usd]
run_times_usd_np = np.array(run_times_usd)

plt.figure(figsize=(10, 6))
plt.plot(amounts_usd_str, run_times_usd_np, marker='o', linestyle='-', color='b')
plt.title('Run Time of Coin Change Algorithm [Initial Algorithm]')
plt.xlabel('Amount (cents)')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()