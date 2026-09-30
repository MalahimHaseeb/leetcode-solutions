# 2352. Equal Row and Column Pairs

**Difficulty:** Medium

**LeetCode:** [2352. Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/)

---

## Problem

Given a 0-indexed `n x n` integer matrix `grid`, return the number of pairs `(ri, cj)` such that row `ri` and column `cj` are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

---

## Examples

### Example 1

**Input:**

```text
grid = [[3,2,1],[1,7,6],[2,7,7]]
```

**Output:**

```text
1
```

**Explanation:**

There is 1 equal row and column pair:

- (Row 2, Column 1): `[2,7,7]`

---

### Example 2

**Input:**

```text
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
```

**Output:**

```text
3
```

**Explanation:**

There are 3 equal row and column pairs:

- (Row 0, Column 0): `[3,1,2,2]`
- (Row 2, Column 2): `[2,4,2,2]`
- (Row 3, Column 2): `[2,4,2,2]`

---

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 10^5`

---

## Approach

Convert each row to a tuple so it can be used as a dictionary key, then count how many times each row pattern occurs:

- `rows` maps each distinct row (as a tuple) to how many rows in the grid look exactly like it.

Then for each column `j`:

1. Build the column as a tuple by reading `grid[i][j]` for every row `i`.
2. Look up that tuple in `rows`. If some rows match this exact column pattern, add that count to the running total, since each matching row forms one equal row-column pair with this column.

Summing this over all columns gives the total number of equal row-column pairs.

---

## Example Walkthrough

For:

```text
grid = [[3,2,1],[1,7,6],[2,7,7]]
```

Build `rows` from each row:

```text
rows = {(3,2,1): 1, (1,7,6): 1, (2,7,7): 1}
```

Start `count = 0`.

Column `0`: `(3,1,2)`. Not in `rows`, add `0`.

Column `1`: `(2,7,7)`. This matches a row in `rows` with count `1`, add `1`:

```text
count = 1
```

Column `2`: `(1,6,7)`. Not in `rows`, add `0`.

The final result is `1`.

---

## Complexity

Let `n` be the size of the grid.

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n^2)`

Building each row tuple and each column tuple takes `O(n)`, done for `n` rows and `n` columns, and the dictionary can hold up to `n` distinct row tuples of length `n`.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
