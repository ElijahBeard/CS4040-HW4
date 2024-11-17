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
amounts = [10, 50, 100, 500, 1000, 1500, 2000, 3000, 5000]

run_times = []

for amount in amounts:
    start_time = time.time() 

    coin_change(coins_usd, amount)
    
    end_time = time.time()
    run_times.append(end_time - start_time)

amounts_str = [str(amount) for amount in amounts]
run_times_np = np.array(run_times)

plt.figure(figsize=(10, 6))
plt.plot(amounts_str, run_times_np, marker='o', linestyle='-', color='b')
plt.title('Run Time of Coin Change Algorithm for Different Amounts (USD)')
plt.xlabel('Amount')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()