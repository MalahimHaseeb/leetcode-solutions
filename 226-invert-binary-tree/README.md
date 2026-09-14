# 226. Invert Binary Tree

**Difficulty:** Easy

**LeetCode:** [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

---

## Problem

Given the `root` of a binary tree, invert the tree and return its root.

Inverting a binary tree means swapping the **left** and **right** child of every node.

---

## Examples

### Example 1

**Input:**

```text
root = [4,2,7,1,3,6,9]
```

**Output:**

```text
[4,7,2,9,6,3,1]
```

The tree changes from:

```text
        4
       / \
      2   7
     / \ / \
    1  3 6  9
```

to:

```text
        4
       / \
      7   2
     / \ / \
    9  6 3  1
```

### Example 2

**Input:**

```text
root = [2,1,3]
```

**Output:**

```text
[2,3,1]
```

### Example 3

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

* The number of nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`

---

## Approach

This solution uses **recursion (DFS)**.

For every node, we swap its left and right children:

```text
left ↔ right
```

After swapping, we recursively invert both subtrees.

### Step-by-Step

For this tree:

```text
        4
       / \
      2   7
```

First, swap the children of `4`:

```text
        4
       / \
      7   2
```

Then recursively do the same thing for the subtrees rooted at `7` and `2`.

The process continues until every node has been inverted.

If the root is `None`, there is no tree to invert, so we return `None`.

---

## Complexity

Let `n` be the number of nodes in the tree.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(h)`

where `h` is the height of the tree because of the recursive call stack.

For a balanced tree, the recursion depth is `O(log n)`.

For a completely skewed tree, the recursion depth can be `O(n)`.

---

## Solution

The complete implementation is available in [`solution.py`](./solution.py).
