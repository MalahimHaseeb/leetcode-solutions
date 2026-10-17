# 700. Search in a Binary Search Tree

**Difficulty:** Easy

**LeetCode:** [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)

---

## Problem

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

---

## Examples

### Example 1

**Input:**

```text
root = [4,2,7,1,3]
val = 2
```

**Output:**

```text
[2,1,3]
```

---

### Example 2

**Input:**

```text
root = [4,2,7,1,3]
val = 5
```

**Output:**

```text
[]
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 5000]`.
- `1 <= Node.val <= 10^7`
- `root` is a binary search tree.
- `1 <= val <= 10^7`

---

## Approach

Use the BST property to skip half of the tree at every step:

- Every value in a node's left subtree is smaller than the node.
- Every value in a node's right subtree is larger than the node.

Start with `head` at `root` and loop while `head` is not `None`:

1. If `val == head.val`, found it. Return `head`, which is the root of the subtree we want.
2. If `val < head.val`, the target can only be in the left subtree, so move `head` to `head.left`.
3. Otherwise, the target can only be in the right subtree, so move `head` to `head.right`.

If the loop ends because `head` became `None`, the value is not in the tree, so return `None`.

Since this is done with a loop instead of recursion, no call stack is needed.

---

## Example Walkthrough

For:

```text
root = [4,2,7,1,3]
val = 5
```

The tree looks like this:

```text
      4
     / \
    2   7
   / \
  1   3
```

Start with `head = 4`. `5 > 4`, so go right:

```text
head = 7
```

`5 < 7`, so go left:

```text
head = None
```

`head` is `None`, so the loop ends. The value `5` is not in the tree, so the final result is `None`, which is shown as `[]`.

---

## Complexity

Let `h` be the height of the tree.

- **Time Complexity:** `O(h)`
- **Space Complexity:** `O(1)`

Each step moves one level down the tree, so at most `h` nodes are visited. In the worst case of a skewed tree, `h` is `n`. Only one pointer variable is used, so no extra space grows with the input.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
