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

coins_wizard = [1, 29, 493]
amounts_wizard = [10, 25, 50, 100]

run_times_wizard = []

for amount in amounts_wizard:
    start_time = time.time()
    coin_change(coins_wizard, amount)
    end_time = time.time()
    run_times_wizard.append(end_time - start_time)

amounts_wizard_str = [str(amount) for amount in amounts_wizard]
run_times_wizard_np = np.array(run_times_wizard)

plt.figure(figsize=(10, 6))
plt.plot(amounts_wizard_str, run_times_wizard_np, marker='o', linestyle='-', color='g')
plt.title('Run Time of Coin Change Algorithm for Le Epic Wizard [Initial Algorithm]')
plt.xlabel('Knuts')
plt.ylabel('Time (s)')
plt.grid(True)
plt.show()