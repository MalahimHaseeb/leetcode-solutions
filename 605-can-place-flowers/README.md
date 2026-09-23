# 605. Can Place Flowers

**Difficulty:** Easy

**LeetCode:** [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

---

## Problem

You have a flowerbed represented by an integer array `flowerbed`.

- `0` means the plot is empty.
- `1` means the plot already contains a flower.

Flowers cannot be planted in **adjacent plots**.

Given an integer `n`, return `true` if `n` new flowers can be planted without violating the no-adjacent-flowers rule. Otherwise, return `false`.

---

## Examples

### Example 1

**Input:**

```text
flowerbed = [1,0,0,0,1]
n = 1
```

**Output:**

```text
true
```

One flower can be planted in the middle:

```text
[1,0,1,0,1]
```

### Example 2

**Input:**

```text
flowerbed = [1,0,0,0,1]
n = 2
```

**Output:**

```text
false
```

Only one additional flower can be planted.

---

## Constraints

- `1 <= flowerbed.length <= 2 * 10^4`
- `flowerbed[i]` is either `0` or `1`.
- There are no two adjacent flowers in `flowerbed`.
- `0 <= n <= flowerbed.length`

---

## Approach

This solution checks each empty plot and determines whether a flower can be planted there.

To make the boundary cases easier to handle, we add an empty plot (`0`) to both ends of the flowerbed:

```text
[0] + flowerbed + [0]
```

For every position, we check three conditions:

- The left plot is empty.
- The current plot is empty.
- The right plot is empty.

If all three are `0`, we can safely plant a flower there.

After planting, we change the current position to `1` so that the next position knows that it is adjacent to a flower.

Each time a flower is planted, we decrease `n`.

At the end, if `n <= 0`, all required flowers were successfully planted.

---

## Example Walkthrough

For:

```text
flowerbed = [1,0,0,0,1]
n = 1
```

Add empty boundary plots:

```text
[0,1,0,0,0,1,0]
```

Check each position.

At the middle position:

```text
[0,1,0,0,0,1,0]
     ↑
```

Its neighbors are both empty:

```text
0 0 0
```

So we can plant a flower:

```text
[0,1,0,1,0,1,0]
```

Now:

```text
n = 0
```

Therefore:

```text
true
```

---

## Why This Works

A flower can only be planted when the current plot and both neighboring plots are empty.

Once a flower is planted, the current position becomes `1`. This prevents the next adjacent position from being selected.

Adding `0` to both ends means the first and last original positions can be checked using the same condition without special boundary logic.

---

## Complexity

Let `n` be the length of the flowerbed.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

The flowerbed is copied into a new list with two additional boundary elements.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
