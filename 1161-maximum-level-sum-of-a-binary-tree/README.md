# 1161. Maximum Level Sum of a Binary Tree

**Difficulty:** Medium

**LeetCode:** [1161. Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

---

## Problem

Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the smallest level `x` such that the sum of all the values of nodes at level `x` is maximal.

---

## Examples

### Example 1

**Input:**

```text
root = [1,7,0,7,-8,null,null]
```

**Output:**

```text
2
```

**Explanation:**

- Level 1 sum = `1`.
- Level 2 sum = `7 + 0 = 7`.
- Level 3 sum = `7 + -8 = -1`.

So we return the level with the maximum sum, which is level `2`.

---

### Example 2

**Input:**

```text
root = [989,null,10250,98693,-89388,null,null,null,-32127]
```

**Output:**

```text
2
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## Approach

Use a DFS that adds each node's value into a running total for its level:

- `best` is a dictionary mapping each level to the sum of all node values at that level.
- The root starts at level `1`.

At each node:

1. If `node` is `None`, return.
2. Add `node.val` to `best[level]`, starting from `0` if the level has not been seen yet.
3. Recurse into `node.left` and `node.right` with `level + 1`.

Once the DFS finishes, `best` holds the full sum for every level. Then pick the level with the largest sum using `max(best, key=best.get)`.

For ties, `max` returns the first key it encounters with the highest value. Since levels are inserted into the dictionary in increasing order (a level first appears when the DFS reaches it going down the leftmost path, and shallower levels are always inserted before deeper ones), the first match is the smallest level, which is exactly what the problem asks for.

---

## Example Walkthrough

For:

```text
root = [1,7,0,7,-8,null,null]
```

The tree looks like this:

```text
      1
     / \
    7   0
   / \
  7  -8
```

Start at `1` with `level = 1`:

```text
best = {1: 1}
```

Go left to `7` with `level = 2`:

```text
best = {1: 1, 2: 7}
```

Go left to `7` with `level = 3`:

```text
best = {1: 1, 2: 7, 3: 7}
```

Go back up and right to `-8` with `level = 3`:

```text
best = {1: 1, 2: 7, 3: -1}
```

Go back up to `1` and right to `0` with `level = 2`:

```text
best = {1: 1, 2: 7, 3: -1}
```

The sums per level are `1`, `7`, and `-1`. The largest is `7`, at level `2`, so the final result is `2`.

---

## Complexity

Let `n` be the number of nodes in the tree and `h` be its height.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(h)`

Each node is visited exactly once. The dictionary holds one entry per level, which is at most `h` entries, and the recursion stack also grows up to the height of the tree, which is `O(n)` in the worst case of a skewed tree.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
