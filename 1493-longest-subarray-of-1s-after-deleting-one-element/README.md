# 1493. Longest Subarray of 1's After Deleting One Element

**Difficulty:** Medium

**LeetCode:** [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)

---

## Problem

Given a binary array `nums`, you should delete one element from it.

Return the size of the longest non-empty subarray containing only `1`'s in the resulting array. Return `0` if there is no such subarray.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,1,0,1]
```

**Output:**

```text
3
```

**Explanation:**

After deleting the number in position 2, `[1,1,1]` contains 3 numbers with value `1`.

---

### Example 2

**Input:**

```text
nums = [0,1,1,1,0,1,1,0,1]
```

**Output:**

```text
5
```

**Explanation:**

After deleting the number in position 4, `[0,1,1,1,1,1,0,1]` has its longest subarray of `1`s as `[1,1,1,1,1]`.

---

### Example 3

**Input:**

```text
nums = [1,1,1]
```

**Output:**

```text
2
```

**Explanation:**

You must delete one element, even if the array is all `1`s.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## Approach

This is a sliding window problem where the window is allowed to contain at most one zero, since deleting one element means we can tolerate exactly one zero inside the window (that zero is the one we delete).

Two edge cases are handled up front:

- If there is no `1` in `nums`, no subarray of `1`s can exist, so return `0`.
- If there is no `0` in `nums`, the whole array is `1`s, but one element must still be deleted, so return `len(nums) - 1`.

For the general case, use two pointers, `left` and `right`, and a counter `zero` for how many zeros are in the current window:

- Expand the window by moving `right` forward.
- If `nums[right]` is `0`, increase `zero`. If `zero` exceeds `1`, shrink the window from the left until it contains at most one zero again, decreasing `zero` whenever `nums[left]` is `0`.
- After adjusting, the window `[left, right]` always has at most one zero. Track the largest window length seen, `right - left + 1`, in `best`.

Since the window includes at most one zero (the element we would delete), the final answer is `best - 1`, the count of actual `1`s in the best window. If no valid window was ever found, return `0`.

---

## Example Walkthrough

For:

```text
nums = [0,1,1,1,0,1,1,0,1]
```

Start with `left = 0`, `zero = 0`, `best = 0`.

At `right = 0`, `nums[0] = 0`:

```text
zero = 1
best = max(0, 0 - 0 + 1) = 1
```

At `right = 1, 2, 3`, all `1`s, no change to `zero`:

```text
zero = 1
best = max(1, 3 - 0 + 1) = 4
```

At `right = 4`, `nums[4] = 0`:

```text
zero = 2
```

`zero > 1`, so shrink from the left. `nums[0] = 0`, decrease `zero` to `1`, move `left` to `1`:

```text
zero = 1
best = max(4, 4 - 1 + 1) = 4
```

At `right = 5, 6`, both `1`s:

```text
zero = 1
best = max(4, 6 - 1 + 1) = 6
```

At `right = 7`, `nums[7] = 0`:

```text
zero = 2
```

Shrink from the left. `nums[1] = 1`, no change, move `left` to `2`. Still `zero = 2 > 1`. `nums[2] = 1`, no change, move `left` to `3`. Still `zero = 2 > 1`. `nums[3] = 1`, no change, move `left` to `4`. Still `zero = 2 > 1`. `nums[4] = 0`, decrease `zero` to `1`, move `left` to `5`:

```text
zero = 1
best = max(6, 7 - 5 + 1) = 6
```

At `right = 8`, `nums[8] = 1`:

```text
zero = 1
best = max(6, 8 - 5 + 1) = 6
```

The best window has length `6`, so the final result is `6 - 1 = 5`.

---

## Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

Both pointers move forward across the array at most `n` times combined, and only a fixed number of counters are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
