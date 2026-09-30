# 1207. Unique Number of Occurrences

**Difficulty:** Easy

**LeetCode:** [1207. Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)

---

## Problem

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is unique or `false` otherwise.

---

## Examples

### Example 1

**Input:**

```text
arr = [1,2,2,1,1,3]
```

**Output:**

```text
true
```

**Explanation:**

The value `1` has `3` occurrences, `2` has `2` and `3` has `1`. No two values have the same number of occurrences.

---

### Example 2

**Input:**

```text
arr = [1,2]
```

**Output:**

```text
false
```

---

### Example 3

**Input:**

```text
arr = [-3,0,1,-3,1,1,1,-3,10,0]
```

**Output:**

```text
true
```

---

## Constraints

- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`

---

## Approach

Break the problem into two steps: count occurrences, then check if those counts are all different.

- If `arr` has fewer than `2` elements, there can't be a clash between two different values' counts, so return `true` right away.
- Build a `count` dictionary mapping each value to how many times it appears in `arr`.
- Walk through the counts (the values of the dictionary, not the original array) and track which counts have already been seen using a `seen` set.
  - If a count is already in `seen`, two different values share the same number of occurrences, so return `false`.
  - Otherwise, add the count to `seen` and keep going.
- If every count was unique, return `true`.

---

## Example Walkthrough

For:

```text
arr = [1,2,2,1,1,3]
```

Build the count dictionary:

```text
count = {1: 3, 2: 2, 3: 1}
```

Start with `seen = {}`.

Check `count[1] = 3`. Not in `seen`, add it:

```text
seen = {3}
```

Check `count[2] = 2`. Not in `seen`, add it:

```text
seen = {3, 2}
```

Check `count[3] = 1`. Not in `seen`, add it:

```text
seen = {3, 2, 1}
```

All counts were unique, so the final result is `true`.

---

## Complexity

Let `n` be the length of `arr`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

Building the count dictionary takes one pass over `arr`, and checking uniqueness takes one pass over the distinct values, both bounded by `n`.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
