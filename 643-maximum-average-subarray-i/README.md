# 643. Maximum Average Subarray I

**Difficulty:** Easy

**LeetCode:** [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

---

## Problem

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than `10^-5` will be accepted.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

**Output:**

```text
12.75000
```

**Explanation:**

Maximum average is `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`.

---

### Example 2

**Input:**

```text
nums = [5]
k = 1
```

**Output:**

```text
5.00000
```

---

## Constraints

- `n == nums.length`
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach

Use a sliding window of fixed size `k`:

- First, compute the sum of the first `k` elements. This is the initial window sum, and dividing it by `k` gives the initial max average.
- Then slide the window one step at a time across the rest of the array.

To move the window from position `i-k` to `i`:

1. Add the new element entering the window, `nums[i]`.
2. Subtract the element leaving the window, `nums[i-k]`.
3. Divide the updated sum by `k` and compare it to the current max average, keeping the larger one.

This way, every window sum is computed in constant time instead of resumming the whole window each time.

---

## Example Walkthrough

For:

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

First window sum, indices `0` to `3`:

```text
current_sum = 1 + 12 + (-5) + (-6) = 2
max_avg = 2 / 4 = 0.5
```

Slide to `i = 4`. Add `nums[4] = 50`, remove `nums[0] = 1`:

```text
current_sum = 2 + 50 - 1 = 51
max_avg = max(0.5, 51/4) = 12.75
```

Slide to `i = 5`. Add `nums[5] = 3`, remove `nums[1] = 12`:

```text
current_sum = 51 + 3 - 12 = 42
max_avg = max(12.75, 42/4) = 12.75
```

The final result is `12.75`.

---

## Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

Each element is visited once when it enters and once when it leaves the window, and only a fixed number of variables are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
