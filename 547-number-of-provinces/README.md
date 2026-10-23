# 547. Number of Provinces

**Difficulty:** Medium

**LeetCode:** [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

---

## Problem

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of provinces.

---

## Examples

### Example 1

**Input:**

```text
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
```

**Output:**

```text
2
```

---

### Example 2

**Input:**

```text
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
```

**Output:**

```text
3
```

---

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`.
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

---

## Approach

Treat the cities as nodes in a graph and count how many connected components it has. Each component is one province.

- `visited` is a list of booleans, one per city, marking cities already assigned to a province.
- `dfs(city)` marks `city` as visited, then recursively visits every directly connected city that has not been visited yet.

Loop over every city `i` from `0` to `n - 1`:

1. If `visited[i]` is `False`, city `i` belongs to a province we have not counted yet. Increase `provinces` by `1`.
2. Run `dfs(i)` to mark every city in that province as visited, so none of them get counted again.

Inside `dfs`, loop over every `nb` from `0` to `n - 1`. If `isConnected[city][nb] == 1` and `nb` is not visited, recurse into `nb`. This reaches indirect connections too, since each recursive call keeps following links outward.

After the loop, `provinces` holds the number of separate groups.

An empty matrix has no cities, so it returns `0`.

---

## Example Walkthrough

For:

```text
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
```

Start with:

```text
visited = [False, False, False]
provinces = 0
```

At `i = 0`, city `0` is not visited. Count a new province and run `dfs(0)`:

```text
provinces = 1
```

Inside `dfs(0)`, mark city `0` visited. Check its neighbors. `isConnected[0][1] = 1` and city `1` is not visited, so recurse into `dfs(1)`. City `2` is not connected to city `0`, so skip it:

```text
visited = [True, True, False]
```

Inside `dfs(1)`, city `0` is already visited and city `2` is not connected to city `1`, so nothing more happens.

At `i = 1`, city `1` is already visited, so skip it.

At `i = 2`, city `2` is not visited. Count a new province and run `dfs(2)`:

```text
provinces = 2
visited = [True, True, True]
```

The final result is `2`.

---

## Complexity

Let `n` be the number of cities.

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

Each city is visited once by `dfs`, and each visit scans a full row of the matrix, which costs `O(n)`. The `visited` list holds `n` entries, and the recursion stack can grow up to `n` calls deep when all cities form one long chain.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
