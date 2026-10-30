# 1466. Reorder Routes to Make All Paths Lead to the City Zero

**Difficulty:** Medium

**LeetCode:** [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

---

## Problem

There are `n` cities numbered from `0` to `n - 1` and `n - 1` roads such that there is only one way to travel between two different cities (this network forms a tree). Last year, the ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by `connections` where `connections[i] = [ai, bi]` represents a road from city `ai` to city `bi`.

This year, there will be a big event in the capital (city `0`), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city `0`. Return the minimum number of edges changed.

It's guaranteed that each city can reach city `0` after reorder.

---

## Examples

### Example 1

**Input:**

```text
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
```

**Output:**

```text
3
```

**Explanation:**

Change the direction of the roads `0 -> 1`, `1 -> 3` and `5 <- 4` appropriately so that every city can reach city `0`.

---

### Example 2

**Input:**

```text
n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
```

**Output:**

```text
2
```

**Explanation:**

Two roads point away from city `0` and need to be reversed.

---

### Example 3

**Input:**

```text
n = 3
connections = [[1,0],[2,0]]
```

**Output:**

```text
0
```

---

## Constraints

- `2 <= n <= 5 * 10^4`
- `connections.length == n - 1`
- `connections[i].length == 2`
- `0 <= ai, bi <= n - 1`
- `ai != bi`

---

## Approach

The roads form a tree, so there is exactly one path between city `0` and every other city. For every city to reach `0`, each road on those paths must point toward `0`. So walk outward from `0` and count the roads that point away from it.

Build two structures:

- `original` is a set of the directed roads `(a, b)` exactly as given.
- `graph` is an undirected adjacency list, where each road is added in both directions so the tree can be walked from `0` in any direction.

Then run an iterative DFS from city `0`. The stack holds pairs of `(city, parent)`, where `parent` is the city we came from. Starting with `(0, -1)`, since `0` has no parent.

While the stack is not empty:

1. Pop `(city, parent)`.
2. For every `neighbor` of `city` that is not `parent`, we are moving one step away from `0`.
3. If `(city, neighbor)` is in `original`, the road points away from `0`, so it must be reversed. Increase `changes` by `1`.
4. If `(city, neighbor)` is not in `original`, the road is stored as `(neighbor, city)`, which already points toward `0`, so nothing changes.
5. Push `(neighbor, city)` onto the stack.

Skipping `parent` keeps the walk from going back up the tree, so every road is checked exactly once.

---

## Example Walkthrough

For:

```text
n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
```

Build the structures:

```text
original = {(1,0), (1,2), (3,2), (3,4)}
graph = {0: [1], 1: [0,2], 2: [1,3], 3: [2,4], 4: [3]}
```

Start with:

```text
stack = [(0, -1)]
changes = 0
```

Pop `(0, -1)`. Its only neighbor is `1`. `(0, 1)` is not in `original`, since the road is `1 -> 0` and already points toward `0`. Push `(1, 0)`:

```text
changes = 0
```

Pop `(1, 0)`. Neighbor `0` is the parent, skip it. Neighbor `2`: `(1, 2)` is in `original`, so this road points away from `0` and must be reversed. Push `(2, 1)`:

```text
changes = 1
```

Pop `(2, 1)`. Neighbor `1` is the parent, skip it. Neighbor `3`: `(2, 3)` is not in `original`, since the road is `3 -> 2` and already points toward `0`. Push `(3, 2)`:

```text
changes = 1
```

Pop `(3, 2)`. Neighbor `2` is the parent, skip it. Neighbor `4`: `(3, 4)` is in `original`, so this road must be reversed. Push `(4, 3)`:

```text
changes = 2
```

Pop `(4, 3)`. Its only neighbor `3` is the parent, so nothing happens. The stack is empty.

The final result is `2`.

---

## Complexity

Let `n` be the number of cities.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

The tree has `n - 1` roads, and each one is added to the structures once and checked once during the walk. The `original` set, the `graph` and the stack each hold at most `O(n)` entries.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
