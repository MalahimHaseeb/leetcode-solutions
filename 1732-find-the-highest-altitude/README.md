# 1732. Find the Highest Altitude

**Difficulty:** Easy

**LeetCode:** [1732. Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/)

---

## Problem

There is a biker going on a road trip. The road trip consists of `n + 1` points at various altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1` for all `0 <= i < n`. Return the highest altitude of a point.

---

## Examples

### Example 1

**Input:**

```text
gain = [-5,1,5,0,-7]
```

**Output:**

```text
1
```

**Explanation:**

The altitudes are `[0,-5,-4,1,1,-6]`. The highest is `1`.

---

### Example 2

**Input:**

```text
gain = [-4,-3,-2,-1,4,3,2]
```

**Output:**

```text
0
```

**Explanation:**

The altitudes are `[0,-4,-7,-9,-10,-6,-3,-1]`. The highest is `0`.

---

## Constraints

- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

---

## Approach

Track the running altitude as a prefix sum:

- Start `altitude` at `0`, since the biker begins at point `0` with altitude `0`.
- Start `best` at `0` too, since point `0` is always part of the trip and could turn out to be the highest point.

For each value `g` in `gain`:

1. Add `g` to `altitude`, moving to the next point.
2. Compare `altitude` to `best` and keep the larger one.

By the end, `best` holds the highest altitude reached at any point along the trip.

---

## Example Walkthrough

For:

```text
gain = [-5,1,5,0,-7]
```

Start with `altitude = 0`, `best = 0`.

Process `-5`:

```text
altitude = -5
best = max(0, -5) = 0
```

Process `1`:

```text
altitude = -4
best = max(0, -4) = 0
```

Process `5`:

```text
altitude = 1
best = max(0, 1) = 1
```

Process `0`:

```text
altitude = 1
best = max(1, 1) = 1
```

Process `-7`:

```text
altitude = -6
best = max(1, -6) = 1
```

The final result is `1`.

---

## Complexity

Let `n` be the length of `gain`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

Each value is visited once, and only two counters are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
