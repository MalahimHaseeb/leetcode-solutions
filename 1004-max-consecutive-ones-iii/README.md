# 1004. Max Consecutive Ones III

**Difficulty:** Medium

**LeetCode:** [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

---

## Problem

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

**Output:**

```text
6
```

**Explanation:**

`[1,1,1,0,0,1,1,1,1,1,1]`

The bolded numbers were flipped from `0` to `1`. The longest subarray is underlined.

---

### Example 2

**Input:**

```text
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
```

**Output:**

```text
10
```

**Explanation:**

`[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]`

The bolded numbers were flipped from `0` to `1`. The longest subarray is underlined.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

---

## Approach

Use a sliding window with two pointers, `left` and `right`, and a counter `zeros` for how many zeros are currently inside the window:

- Expand the window by moving `right` forward one step at a time.
- If `nums[right]` is `0`, increase `zeros`, since that zero would need a flip to keep the window all `1`s.
- If `zeros` exceeds `k`, the window has more zeros than we're allowed to flip, so shrink it from the left until `zeros` is back to `k` or less. Each time `nums[left]` is `0`, decrease `zeros`, then move `left` forward.
- After adjusting, the window `[left, right]` is always valid, meaning it has at most `k` zeros. Compare its length, `right - left + 1`, to the best length seen so far.

Since `left` only ever moves forward and never backward, the total movement of both pointers across the whole array is linear.

---

## Example Walkthrough

For:

```text
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

Start with `left = 0`, `zeros = 0`, `best = 0`.

Expand `right` through indices `0, 1, 2`, all `1`s, no zeros added. At `right = 2`:

```text
zeros = 0
best = 3
```

Expand to `right = 3`, `nums[3] = 0`:

```text
zeros = 1
best = 4
```

Expand to `right = 4`, `nums[4] = 0`:

```text
zeros = 2
best = 5
```

Expand to `right = 5`, `nums[5] = 0`:

```text
zeros = 3
```

Now `zeros > k`, so shrink from the left. `nums[0] = 1`, no change to `zeros`, move `left` to `1`. Still `zeros = 3 > k`. `nums[1] = 1`, move `left` to `2`. Still `zeros = 3 > k`. `nums[2] = 1`, move `left` to `3`. Still `zeros = 3 > k`. `nums[3] = 0`, decrease `zeros` to `2`, move `left` to `4`:

```text
zeros = 2
best = max(5, 5 - 4 + 1) = 5
```

Expand to `right = 6` through `right = 9`, all `1`s, no new zeros:

```text
zeros = 2
best = max(5, 9 - 4 + 1) = 6
```

Expand to `right = 10`, `nums[10] = 0`:

```text
zeros = 3
```

Shrink from the left. `nums[4] = 0`, decrease `zeros` to `2`, move `left` to `5`:

```text
zeros = 2
best = max(6, 10 - 5 + 1) = 6
```

The final result is `6`.

---

## Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

Both pointers move forward across the array at most `n` times combined, and only a fixed number of counters are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
