# 399. Evaluate Division

**Difficulty:** Medium

**LeetCode:** [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/)

---

## Problem

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the `jth` query where you must find the answer for `Cj / Dj = ?`.

Return the answers to all queries. If a single answer cannot be determined, return `-1.0`.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

---

## Examples

### Example 1

**Input:**

```text
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
```

**Output:**

```text
[6.00000,0.50000,-1.00000,1.00000,-1.00000]
```

**Explanation:**

Given: `a / b = 2.0`, `b / c = 3.0`

Queries are: `a / c = ?`, `b / a = ?`, `a / e = ?`, `a / a = ?`, `x / x = ?`

Return: `[6.0, 0.5, -1.0, 1.0, -1.0]`

Note: `x` is undefined, so the answer is `-1.0`.

---

### Example 2

**Input:**

```text
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
```

**Output:**

```text
[3.75000,0.40000,5.00000,0.20000]
```

---

### Example 3

**Input:**

```text
equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
```

**Output:**

```text
[0.50000,2.00000,-1.00000,-1.00000]
```

---

## Constraints

- `1 <= equations.length <= 20`
- `equations[i].length == 2`
- `1 <= Ai.length, Bi.length <= 5`
- `values.length == equations.length`
- `0.0 < values[i] <= 20.0`
- `1 <= queries.length <= 20`
- `queries[i].length == 2`
- `1 <= Cj.length, Dj.length <= 5`
- `Ai`, `Bi`, `Cj`, `Dj` consist of lower case English letters and digits.

---

## Approach

Treat every variable as a node in a graph and every equation as a weighted edge. If `a / b = 2.0`, then going from `a` to `b` costs `2.0`, and going from `b` to `a` costs `1 / 2.0 = 0.5`. A query `c / d` is then the product of the edge weights along a path from `c` to `d`.

Build the graph as a dictionary of dictionaries:

- `graph[a][b] = value` stores `a / b`.
- `graph[b][a] = 1 / value` stores the reverse, `b / a`.

Then write a DFS helper, `find(current, target, visited)`, that returns `current / target`:

1. If `current == target`, return `1.0`, since any variable divided by itself is `1`.
2. Add `current` to `visited` so the search never walks in circles.
3. For every `neighbour` of `current` that is not visited, recursively compute `find(neighbour, target, visited)`.
4. If that result is not `-1.0`, a path exists. Multiply it by `graph[current][neighbour]` and return it. This works because `(neighbour / target) * (current / neighbour) = current / target`.
5. If no neighbour leads to the target, return `-1.0`.

For each query `c, d`:

- If `c` or `d` is not in `graph`, the variable is undefined, so the answer is `-1.0`. This also covers a query like `x / x`, which is `-1.0` because `x` never appears in the equations.
- Otherwise, run `find(c, d, set())` with a fresh `visited` set and store the result.

Return the list of answers at the end.

---

## Example Walkthrough

For:

```text
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
```

Build the graph:

```text
graph = {
  "a": {"b": 2.0},
  "b": {"a": 0.5, "c": 3.0},
  "c": {"b": 0.3333}
}
```

Query `a / c`. Both are in `graph`, so run `find("a", "c", set())`. Mark `a` visited and go to neighbour `b`. Call `find("b", "c", ...)`. Mark `b` visited. Neighbour `a` is visited, so skip it. Neighbour `c` calls `find("c", "c", ...)`, which returns `1.0`:

```text
find("b", "c") = 1.0 * graph["b"]["c"] = 1.0 * 3.0 = 3.0
find("a", "c") = 3.0 * graph["a"]["b"] = 3.0 * 2.0 = 6.0
```

Query `b / a`. Run `find("b", "a", set())`. Mark `b` visited. Neighbour `a` calls `find("a", "a", ...)`, which returns `1.0`:

```text
find("b", "a") = 1.0 * graph["b"]["a"] = 1.0 * 0.5 = 0.5
```

Query `a / e`. `e` is not in `graph`, so the answer is `-1.0`.

Query `a / a`. Both are in `graph`, and `find("a", "a", ...)` returns `1.0` right away.

Query `x / x`. `x` is not in `graph`, so the answer is `-1.0`.

The final result is `[6.0, 0.5, -1.0, 1.0, -1.0]`.

---

## Complexity

Let `E` be the number of equations, `V` be the number of distinct variables, and `Q` be the number of queries.

- **Time Complexity:** `O(E + Q * (V + E))`
- **Space Complexity:** `O(V + E)`

Building the graph takes one pass over the equations. Each query runs a DFS that visits every variable at most once and looks at every edge at most twice, which is `O(V + E)`. The graph stores every variable and two entries per equation, and the `visited` set and the recursion stack each hold at most `V` entries.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
