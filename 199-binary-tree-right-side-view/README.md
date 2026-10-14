# 199. Binary Tree Right Side View

**Difficulty:** Medium

**LeetCode:** [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

---

## Problem

Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

---

## Examples

### Example 1

**Input:**

```text
root = [1,2,3,null,5,null,4]
```

**Output:**

```text
[1,3,4]
```

---

### Example 2

**Input:**

```text
root = [1,2,3,4,null,null,null,5]
```

**Output:**

```text
[1,3,4,5]
```

---

### Example 3

**Input:**

```text
root = [1,null,3]
```

**Output:**

```text
[1,3]
```

---

### Example 4

**Input:**

```text
root = []
```

**Output:**

```text
[]
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

---

## Approach

Use a DFS that visits the right child before the left child, and track the current depth:

- `result` holds the values visible from the right side, one per depth level.
- The first node reached at each new depth is the rightmost node of that level, since the right subtree is always explored first.

At each node:

1. If `node` is `None`, return.
2. If `depth == len(result)`, this is the first node seen at this depth, so append its value to `result`.
3. Recurse into `node.right` first, then `node.left`, both with `depth + 1`.

Nodes deeper in the left subtree can still show up in the view when the right side is shorter, because a depth that the right subtree never reached still has an empty slot in `result` when the left subtree gets there.

---

## Example Walkthrough

For:

```text
root = [1,2,3,null,5,null,4]
```

The tree looks like this:

```text
    1
   / \
  2   3
   \   \
    5   4
```

Start at `1` with `depth = 0`. `len(result) = 0`, so this is the first node at depth `0`:

```text
result = [1]
```

Go right to `3` with `depth = 1`. `len(result) = 1`, so append:

```text
result = [1, 3]
```

Go right to `4` with `depth = 2`. `len(result) = 2`, so append:

```text
result = [1, 3, 4]
```

`4` has no children, so go back up. `3` has no left child, so go back up to `1`.

Go left to `2` with `depth = 1`. `len(result) = 3`, so `depth != len(result)` and nothing is appended.

Go right to `5` with `depth = 2`. `len(result) = 3`, so nothing is appended.

The final result is `[1, 3, 4]`.

---

## Complexity

Let `n` be the number of nodes in the tree and `h` be its height.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(h)`

Each node is visited exactly once, and the recursion stack grows up to the height of the tree, which is `O(n)` in the worst case of a skewed tree.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
