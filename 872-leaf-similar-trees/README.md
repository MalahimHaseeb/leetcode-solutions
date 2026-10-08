# 872. Leaf-Similar Trees

**Difficulty:** Easy

**LeetCode:** [872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)

---

## Problem

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

---

## Examples

### Example 1

**Input:**

```text
root1 = [3,5,1,6,2,9,8,null,null,7,4]
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
```

**Output:**

```text
true
```

---

### Example 2

**Input:**

```text
root1 = [1,2,3]
root2 = [1,3,2]
```

**Output:**

```text
false
```

---

## Constraints

- The number of nodes in each tree will be in the range `[1, 200]`.
- Both of the given trees will have values in the range `[0, 200]`.

---

## Approach

Collect the leaf values of each tree in left to right order, then compare the two sequences:

- Write a helper, `getLeaves`, that walks a tree with DFS and appends the value of every leaf to a list.
- A node is a leaf when both `root.left` and `root.right` are `None`.
- Visiting the left child before the right child guarantees the leaves are collected in left to right order.

Steps:

1. Create two empty lists, `arr1` and `arr2`.
2. Run `getLeaves` on `root1` to fill `arr1`, and on `root2` to fill `arr2`.
3. Return whether `arr1 == arr2`.

If the two sequences match exactly, in the same order, the trees are leaf-similar.

---

## Example Walkthrough

For:

```text
root1 = [1,2,3]
root2 = [1,3,2]
```

For `root1`, node `1` has two children, so it is not a leaf. Go left to node `2`, which is a leaf:

```text
arr1 = [2]
```

Go right to node `3`, which is a leaf:

```text
arr1 = [2, 3]
```

For `root2`, node `1` is not a leaf. Go left to node `3`, which is a leaf:

```text
arr2 = [3]
```

Go right to node `2`, which is a leaf:

```text
arr2 = [3, 2]
```

Compare the sequences:

```text
[2, 3] != [3, 2]
```

The sequences differ, so the final result is `false`.

---

## Complexity

Let `n` be the number of nodes in `root1` and `m` be the number of nodes in `root2`.

- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(n + m)`

Each node of both trees is visited once. The leaf lists and the recursion stack together take space proportional to the sizes of the trees in the worst case.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
