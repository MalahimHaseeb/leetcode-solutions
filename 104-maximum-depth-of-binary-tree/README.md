# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy

**LeetCode:** [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## Problem

Given the `root` of a binary tree, return its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## Examples

### Example 1

**Input:**

```text
root = [3,9,20,null,null,15,7]
```

**Output:**

```text
3
```

**Explanation:**

The longest path is:

```text
3 -> 20 -> 15
```

or:

```text
3 -> 20 -> 7
```

Both paths contain `3` nodes, so the maximum depth is `3`.

---

### Example 2

**Input:**

```text
root = [1,null,2]
```

**Output:**

```text
2
```

**Explanation:**

The longest path is:

```text
1 -> 2
```

So the maximum depth is `2`.

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

---

## Approach

Use recursion to calculate the depth of the left and right subtrees.

For every node:

1. If the node is `None`, its depth is `0`.
2. Recursively calculate the maximum depth of the left subtree.
3. Recursively calculate the maximum depth of the right subtree.
4. Take the larger of the two depths.
5. Add `1` for the current node.

The formula is:

```text
1 + max(left subtree depth, right subtree depth)
```

This process continues until the leaf nodes are reached.

---

## Example Walkthrough

For:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Start at node `3`.

The left subtree has depth:

```text
9 -> depth 1
```

The right subtree has depth:

```text
20
/ \
15  7
```

So its depth is `2`.

For node `3`:

```text
1 + max(1, 2)
```

which gives:

```text
3
```

Therefore, the maximum depth is `3`.

---

## Complexity

Let `n` be the number of nodes in the binary tree.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(h)`

where `h` is the height of the tree due to the recursive call stack.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
