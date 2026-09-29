# 724. Find Pivot Index

**Difficulty:** Easy

**LeetCode:** [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

---

## Problem

Given an array of integers `nums`, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return `-1`.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,7,3,6,5,6]
```

**Output:**

```text
3
```

**Explanation:**

The pivot index is `3`.

Left sum = `nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11`

Right sum = `nums[4] + nums[5] = 5 + 6 = 11`

---

### Example 2

**Input:**

```text
nums = [1,2,3]
```

**Output:**

```text
-1
```

**Explanation:**

There is no index that satisfies the conditions in the problem statement.

---

### Example 3

**Input:**

```text
nums = [2,1,-1]
```

**Output:**

```text
0
```

**Explanation:**

The pivot index is `0`.

Left sum = `0` (no elements to the left of index `0`)

Right sum = `nums[1] + nums[2] = 1 + -1 = 0`

---

## Constraints

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

---

## Approach

Use the total sum of the array to avoid recomputing the right sum at every index:

- Compute `total`, the sum of the whole array, once up front.
- Track `left`, the running sum of everything strictly to the left of the current index, starting at `0`.

For each index `i` with value `x`:

1. The right sum at this index is everything except the left part and `x` itself, which is `total - left - x`.
2. If `left` equals that right sum, index `i` is a pivot, so return `i` immediately.
3. Otherwise, add `x` to `left` and move to the next index, since `x` now becomes part of the left sum for future indices.

Because indices are checked in order from left to right, the first match found is guaranteed to be the leftmost pivot. If no index satisfies the condition, return `-1`.

---

## Example Walkthrough

For:

```text
nums = [1,7,3,6,5,6]
```

`total = 1 + 7 + 3 + 6 + 5 + 6 = 28`

Start with `left = 0`.

At `i = 0`, `x = 1`. Right sum is `28 - 0 - 1 = 27`. `left (0) != 27`, so no match. Update `left`:

```text
left = 1
```

At `i = 1`, `x = 7`. Right sum is `28 - 1 - 7 = 20`. `left (1) != 20`, so no match. Update `left`:

```text
left = 8
```

At `i = 2`, `x = 3`. Right sum is `28 - 8 - 3 = 17`. `left (8) != 17`, so no match. Update `left`:

```text
left = 11
```

At `i = 3`, `x = 6`. Right sum is `28 - 11 - 6 = 11`. `left (11) == 11`, a match.

The final result is `3`.

---

## Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

The total sum is computed once, and the array is then scanned a single time while tracking a running left sum.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
