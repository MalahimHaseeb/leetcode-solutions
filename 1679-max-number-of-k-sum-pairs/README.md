# 1679. Max Number of K-Sum Pairs

**Difficulty:** Medium

**LeetCode:** [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/)

---

## Problem

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,2,3,4]
k = 5
```

**Output:**

```text
2
```

**Explanation:**

Starting with `nums = [1,2,3,4]`:

- Remove `1` and `4`, then `nums = [2,3]`
- Remove `2` and `3`, then `nums = []`

There are no more pairs that sum up to `5`, hence a total of 2 operations.

---

### Example 2

**Input:**

```text
nums = [3,1,3,4,3]
k = 6
```

**Output:**

```text
1
```

**Explanation:**

Starting with `nums = [3,1,3,4,3]`:

- Remove the first two `3`s, then `nums = [1,4,3]`

There are no more pairs that sum up to `6`, hence a total of 1 operation.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

---

## Approach

Use a hash map to track how many unmatched numbers we have seen so far:

- `seen` stores the count of each number that has not been paired yet.
- `count` stores the number of pairs formed.

For each number `x` in `nums`:

1. Compute the number needed to complete the pair: `target = k - x`.
2. If `target` is in `seen` with a count above `0`, we found a pair. Increase `count` and decrease `seen[target]` by one.
3. Otherwise, `x` has no partner yet, so add it to `seen` for a future number to pair with.

Since each number is either used in a pair or stored once, no element is ever paired twice. This also handles duplicates and the case where `x` and `target` are the same value (like `3 + 3 = 6`), because a number only pairs with an earlier one that is still unused.

---

## Example Walkthrough

For:

```text
nums = [3,1,3,4,3]
k = 6
```

Initially:

```text
count = 0
seen = {}
```

Process `3`, target is `3`. Not in `seen`, so store it:

```text
seen = {3: 1}
```

Process `1`, target is `5`. Not in `seen`, so store it:

```text
seen = {3: 1, 1: 1}
```

Process `3`, target is `3`. `seen[3] = 1`, so we found a pair:

```text
count = 1
seen = {3: 0, 1: 1}
```

Process `4`, target is `2`. Not in `seen`, so store it:

```text
seen = {3: 0, 1: 1, 4: 1}
```

Process `3`, target is `3`. `seen[3] = 0`, so no pair is available. Store it:

```text
seen = {3: 1, 1: 1, 4: 1}
```

At the end:

```text
count = 1
```

No other pair sums to `6`, so the result is `1`.

---

## Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

The array is scanned once, and each hash map lookup and update takes `O(1)` on average. In the worst case, every number is stored in the map.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
