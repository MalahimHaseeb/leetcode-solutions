# 200. Number of Islands

**Difficulty:** Medium

**LeetCode:** [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

---

## Problem

Given an `m x n` 2D binary grid containing `'1'` for land and `'0'` for water, return the **number of islands**.

An island is formed by connecting adjacent land cells horizontally or vertically.

The edges of the grid are considered to be surrounded by water.

---

## Examples

### Example 1

**Input:**

```text
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```

**Output:**

```text
1
```

**Explanation:**

All connected land cells form one island.

### Example 2

**Input:**

```text
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

**Output:**

```text
3
```

**Explanation:**

There are three separate groups of connected land cells, so there are three islands.

---

## Constraints

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j]` is `'0'` or `'1'`

---

## Approach

This solution uses **Depth-First Search (DFS)** to find and count connected islands.

### Step 1: Traverse the Grid

The grid is traversed using two nested loops.

```python
for r in range(rows):
    for c in range(cols):
```

Whenever a cell containing `"1"` is found, a new island has been discovered.

The island counter is then incremented:

```python
island += 1
```

### Step 2: Explore the Island Using DFS

After finding a land cell, DFS is used to visit all connected land cells.

The DFS checks four possible directions:

```text
Up
Down
Left
Right
```

The recursive calls are:

```python
dfs(r-1, c)
dfs(r+1, c)
dfs(r, c-1)
dfs(r, c+1)
```

### Step 3: Mark Visited Land

When a land cell is visited, it is changed from `"1"` to `"0"`:

```python
grid[r][c] = "0"
```

This marks the cell as visited and prevents it from being counted again.

Because every connected land cell is changed to `"0"`, the next time the grid traversal encounters a `"1"`, it must belong to a different island.

### Example

For:

```text
grid = [
  ["1","1","0"],
  ["1","0","0"],
  ["0","0","1"]
]
```

The first `"1"` starts a DFS that visits:

```text
1 -> 1
|
1
```

Those cells are marked as `"0"`.

Later, the remaining `"1"` is found and starts another DFS.

Therefore, the number of islands is:

```text
2
```

---

## Complexity

Let `m` be the number of rows and `n` be the number of columns.

* **Time Complexity:** `O(m × n)`
* **Space Complexity:** `O(m × n)` in the worst case due to the recursive DFS call stack.

Each cell is visited at most once by the DFS.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
