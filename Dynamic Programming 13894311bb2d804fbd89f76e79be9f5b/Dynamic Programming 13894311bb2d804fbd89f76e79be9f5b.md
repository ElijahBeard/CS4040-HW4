# Dynamic Programming

# Rod-Cutting Algorithm

## Initial Solution

```cpp
let r[0:n] be a new array
r[0] = 0
for j = 1 to n
	q = -inf
	for i = 1 to j
		q = max{q,p[i] + r[j-i]}
	r[j] = 1
return r[n]
```

## Sparse Rod Cutting Algorithm

In our sparse method we need to achieve two things. Using a lookup to get the price for each rod length i. and if it doesnt exist have it default to 0.

We also need to account for rod lengths longer than the available prices. For instance, if n is greater than the longest price the algorithm still works by using the lookup dictionary as the length would have no price associated.

```cpp
let r[0:n] be a new array
r[0] = 0 //assume revanue for rod 0 is 0
for j = 1 to n
	q = -inf
	for i = 1 to j
		price = prices.get(i,0)
		q = max{q,price + r[j-i]}
	r[j] = q
return r[n]
```

| **length** | **price** |
| --- | --- |
| 1 | 1 |
| 2 | 5 |
| 4 | 9 |
| 6 | 17 |
| 8 | 20 |
| 10 | 30 |
| 12 | 36 |
| 16 | 48 |

<aside>
<img src="https://www.notion.so/icons/timeline_gray.svg" alt="https://www.notion.so/icons/timeline_gray.svg" width="40px" /> **Time Complexity Analysis:**

```cpp
let r[0:n] be a new array      //O(n)
r[0] = 0                       //O(1)
for j = 1 to n                 //O(n)
	q = -inf                     //O(n)
	for i = 1 to j               //O(j)
		price = prices.get(i,0)    //O(j)
		q = max{q,price + r[j-i]}. //O(j)
	r[j] = q                     //O(n)
return r[n]                    //O(1)
```

j loop → $O(n)$ times [inner loop]

i loop → $O(j)$ times [outer loop]

everything else is a constant operation

**Best-Case v.s. Worst Case**

In both cases, the number of iterations in each loop depend on the rod length. There is no dependance on the price list or whether prices exist, the loops will always run from 1 to n and 1 to j.

therefore **T(n)** is tightly bounded along → 

$$
T(n)=\sum_{j=1}^nO(j)=\Theta(n^2)
$$

</aside>

## Analysis

![Screenshot 2024-11-17 at 1.18.15 PM.png](Dynamic%20Programming%2013894311bb2d804fbd89f76e79be9f5b/Screenshot_2024-11-17_at_1.18.15_PM.png)

The output matched my prediction of a quadratic time complexity.

# Coin Change Problem

## Initial Solution

```cpp
int getNumWays(x, coins[], num_coins)
	int ways[x + 1] = [0, 0, ...0]
	ways[0] = 1
	for (i = 0..num_coins -1)
		coin_value = coins[i]
		for (j=coin_value..x)
			ways[j] = ways[j-coin_value] + ways[j]
	return ways[x]
```

## Adapted  Solution

We need to adapt it to keep track of the coins used at each step. We can do this by filling the ways array

```python
def coin_change_reconstruct(coins, amount): #O(1)
    ways = [0] * (amount + 1) #O(1)
    ways[0] = 1 #O(1)
    
    combinations = [[] for _ in range(amount + 1)] #O(amount)
    
    for coin in coins: #O(n)
        for i in range(coin, amount + 1): #O(amount)
            ways[i] += ways[i - coin] #O(amount)
            if ways[i - coin] > 0: #O(amount)
                for comb in combinations[i - coin]: #O(i-coin) = O(k)
                    combinations[i].append(comb + [coin]) #O(k)
    
    return ways[amount], combinations[amount] #O(1)
```

<aside>
<img src="https://www.notion.so/icons/timeline_gray.svg" alt="https://www.notion.so/icons/timeline_gray.svg" width="40px" /> **Time Complexity Analysis:**

n (coins) → $O(n)$ times [inner loop]

amount → $O(a)$ times [outer loop]

amount ways → $O(w)$

**Big Theta**

**T(n)** is tightly bounded along → 

$$
T(n,a)=\sum_{n}^aO(w(i-a)=\Theta(n*a*2^a)
$$

</aside>

<aside>
<img src="https://www.notion.so/icons/timeline_gray.svg" alt="https://www.notion.so/icons/timeline_gray.svg" width="40px" />

Run time for **USD**

![Screenshot 2024-11-17 at 1.46.43 PM.png](Dynamic%20Programming%2013894311bb2d804fbd89f76e79be9f5b/Screenshot_2024-11-17_at_1.46.43_PM.png)

![Screenshot 2024-11-17 at 1.43.06 PM.png](Dynamic%20Programming%2013894311bb2d804fbd89f76e79be9f5b/Screenshot_2024-11-17_at_1.43.06_PM.png)

In these results I notice that the initial algorithm has a slight drop in efficiency around 1500 and 2000 compared to the new algorithm. Although, the difference is to the change in scale of 0.0010 seconds.

</aside>

<aside>
<img src="https://www.notion.so/icons/timeline_gray.svg" alt="https://www.notion.so/icons/timeline_gray.svg" width="40px" />

Run time for **Knuts**

![Screenshot 2024-11-17 at 1.45.42 PM.png](Dynamic%20Programming%2013894311bb2d804fbd89f76e79be9f5b/Screenshot_2024-11-17_at_1.45.42_PM.png)

![Screenshot 2024-11-17 at 1.48.35 PM.png](Dynamic%20Programming%2013894311bb2d804fbd89f76e79be9f5b/Screenshot_2024-11-17_at_1.48.35_PM.png)

In these results I notice that the initial algorithm has a slight drop in efficiency initially starting at a 0.1 second disadvantage, which is more significant than the previous example. Although the run time follows the same general trend and the results are significantly similar.

</aside>