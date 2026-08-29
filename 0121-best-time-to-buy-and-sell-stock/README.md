# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy

**LeetCode:** [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

## Problem

You are given an array `prices`, where `prices[i]` represents the price of a stock on the `i`th day.

You can choose one day to **buy** the stock and a different day in the future to **sell** it.

Return the maximum profit that can be achieved.

If no profitable transaction is possible, return `0`.

---

## Examples

### Example 1

**Input:**

```text
prices = [7,1,5,3,6,4]
```

**Output:**

```text
5
```

**Explanation:**

Buy on day 2 at price `1` and sell on day 5 at price `6`.

```text
Profit = 6 - 1 = 5
```

The stock must be bought before it is sold.

### Example 2

**Input:**

```text
prices = [7,6,4,3,1]
```

**Output:**

```text
0
```

**Explanation:**

The prices continuously decrease, so no profitable transaction is possible.

---

## Constraints

* `1 <= prices.length <= 10^5`
* `0 <= prices[i] <= 10^4`

---

## Approach

This solution uses a **single-pass greedy approach**.

The main idea is to keep track of the **lowest stock price seen so far** and calculate the maximum possible profit at each price.

### Step 1: Track the Minimum Price

Initialize `min_price` to infinity:

```python
min_price = float('inf')
```

As we iterate through the prices, whenever a lower price is found, update `min_price`.

```python
if price < min_price:
    min_price = price
```

This represents the best possible buying price seen so far.

### Step 2: Calculate the Potential Profit

For every price that is not a new minimum, calculate the profit if the stock were sold at the current price:

```text
price - min_price
```

If this profit is greater than the current `max_profit`, update it:

```python
elif price - min_price > max_profit:
    max_profit = price - min_price
```

Because `min_price` always comes from an earlier position in the array, the solution automatically ensures that the stock is bought before it is sold.

### Example

For:

```text
prices = [7,1,5,3,6,4]
```

The minimum price and maximum profit change as follows:

```text
Price:       7   1   5   3   6   4
Min Price:   7   1   1   1   1   1
Profit:      0   0   4   2   5   3
```

The maximum profit is:

```text
5
```

---

## Complexity

Let `n` be the number of prices.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The array is traversed only once, and only two variables are used to track the minimum price and maximum profit.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
