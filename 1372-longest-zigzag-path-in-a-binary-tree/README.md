# 1372. Longest ZigZag Path in a Binary Tree

**Difficulty:** Medium

**LeetCode:** [1372. Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)

---

## Problem

You are given the `root` of a binary tree.

A ZigZag path for a binary tree is defined as follows:

- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of `0`).

Return the longest ZigZag path contained in that tree.

---

## Examples

### Example 1

**Input:**

```text
root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
```

**Output:**

```text
3
```

**Explanation:**

The longest ZigZag path is right -> left -> right.

---

### Example 2

**Input:**

```text
root = [1,1,1,null,1,null,null,1,1,null,1]
```

**Output:**

```text
4
```

**Explanation:**

The longest ZigZag path is left -> right -> left -> right.

---

### Example 3

**Input:**

```text
root = [1]
```

**Output:**

```text
0
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 100`

---

## Approach

Run a DFS that carries two numbers down to every node:

- `left` is the length of the zigzag path that ends at this node after arriving by a move to the left child.
- `right` is the length of the zigzag path that ends at this node after arriving by a move to the right child.

At each node:

1. Update `best` with `max(best, left, right)`, since either value is a valid zigzag path ending here.
2. Go to the left child. A path that reaches the left child by moving left can only continue a zigzag if the previous move was a right move, so the new `left` is `right + 1`. The new `right` is `0`, because a fresh path starting at the left child would need to go right next and has no length yet.
3. Go to the right child. By the same logic, the new `right` is `left + 1` and the new `left` is `0`.

Every node is visited once, and each visit extends or restarts the zigzag in constant time. Starting the DFS at the root with `(0, 0)` covers paths that begin at any node, since a restart is built into the `0` reset.

---

## Example Walkthrough

For:

```text
root = [1,1,1,null,1,null,null,1,1,null,1]
```

The tree looks like this:

```text
        1
       / \
      1   1
       \
        1
       / \
      1   1
       \
        1
```

Start at the root with `left = 0`, `right = 0`:

```text
best = 0
```

Go to the left child of the root, passing `left = right + 1 = 1`, `right = 0`:

```text
best = 1
```

Go to the right child of that node, passing `left = 0`, `right = left + 1 = 2`:

```text
best = 2
```

Go to the left child of that node, passing `left = right + 1 = 3`, `right = 0`:

```text
best = 3
```

Go to the right child of that node, passing `left = 0`, `right = left + 1 = 4`:

```text
best = 4
```

The path left -> right -> left -> right has length `4`. No other path in the tree is longer, so the final result is `4`.

---

## Complexity

Let `n` be the number of nodes in the tree and `h` be its height.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(h)`

Each node is visited exactly once, and the recursion stack grows up to the height of the tree, which is `O(n)` in the worst case of a skewed tree.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
