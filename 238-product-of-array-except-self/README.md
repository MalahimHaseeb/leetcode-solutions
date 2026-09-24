# 238. Product of Array Except Self

**Difficulty:** Medium

**LeetCode:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

---

## Problem

Given an integer array `nums`, return an array `answer` such that:

```text
answer[i] = product of all elements of nums except nums[i]
```

The solution must:

- Run in **O(n)** time.
- Not use the division operation.
- Use **O(1)** extra space, excluding the output array.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,2,3,4]
```

**Output:**

```text
[24,12,8,6]
```

For each position:

```text
1 → 2 × 3 × 4 = 24
2 → 1 × 3 × 4 = 12
3 → 1 × 2 × 4 = 8
4 → 1 × 2 × 3 = 6
```

### Example 2

**Input:**

```text
nums = [-1,1,0,-3,3]
```

**Output:**

```text
[0,0,9,0,0]
```

---

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` fits in a 32-bit integer.
- The answer for every position fits in a 32-bit integer.

---

## Approach

The key idea is to calculate the product of all elements **before** each position and the product of all elements **after** each position.

For every index:

```text
answer[i] = product of elements before i
            ×
            product of elements after i
```

We can calculate these two products using two passes.

### Step 1: Calculate Prefix Products

First, move from left to right.

`current` stores the product of all elements before the current index.

For:

```text
nums = [1,2,3,4]
```

The prefix products stored in `result` become:

```text
[1,1,2,6]
```

Because:

```text
index 0 → product before = 1
index 1 → product before = 1
index 2 → product before = 1 × 2 = 2
index 3 → product before = 1 × 2 × 3 = 6
```

### Step 2: Multiply by Suffix Products

Next, move from right to left.

`current` now stores the product of all elements after the current index.

For:

```text
nums = [1,2,3,4]
```

We update `result` using the suffix products:

```text
index 3 → suffix = 1
index 2 → suffix = 4
index 1 → suffix = 4 × 3 = 12
index 0 → suffix = 4 × 3 × 2 = 24
```

The final result becomes:

```text
[24,12,8,6]
```

---

## Example Walkthrough

For:

```text
nums = [1,2,3,4]
```

### First Pass: Prefix Products

Start with:

```text
current = 1
result = [1,1,1,1]
```

Process from left to right:

```text
i = 0
result[0] = 1
current = 1 × 1 = 1
```

```text
i = 1
result[1] = 1
current = 1 × 2 = 2
```

```text
i = 2
result[2] = 2
current = 2 × 3 = 6
```

```text
i = 3
result[3] = 6
current = 6 × 4 = 24
```

Now:

```text
result = [1,1,2,6]
```

### Second Pass: Suffix Products

Reset:

```text
current = 1
```

Process from right to left:

```text
i = 3
result[3] = 6 × 1 = 6
current = 1 × 4 = 4
```

```text
i = 2
result[2] = 2 × 4 = 8
current = 4 × 3 = 12
```

```text
i = 1
result[1] = 1 × 12 = 12
current = 12 × 2 = 24
```

```text
i = 0
result[0] = 1 × 24 = 24
```

Final result:

```text
[24,12,8,6]
```

---

## Why This Works

For every index `i`, the required answer is:

```text
elements before i × elements after i
```

The first loop stores the product of everything before each index.

The second loop multiplies each position by the product of everything after that index.

This means we never need to calculate the product of the entire array or use division.

It also works correctly when the array contains `0`, because the prefix and suffix products naturally become `0` where appropriate.

---

## Complexity

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` extra space

The `result` array is not counted as extra space because it is the required output array.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
