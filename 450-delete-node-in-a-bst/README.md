# 450. Delete Node in a BST

**Difficulty:** Medium

**LeetCode:** [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

---

## Problem

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

---

## Examples

### Example 1

**Input:**

```text
root = [5,3,6,2,4,null,7]
key = 3
```

**Output:**

```text
[5,4,6,2,null,null,7]
```

**Explanation:**

Given key to delete is `3`. So we find the node with value `3` and delete it.

One valid answer is `[5,4,6,2,null,null,7]`. Another valid answer is `[5,2,6,null,4,null,7]` and it's also accepted.

---

### Example 2

**Input:**

```text
root = [5,3,6,2,4,null,7]
key = 0
```

**Output:**

```text
[5,3,6,2,4,null,7]
```

**Explanation:**

The tree does not contain a node with value `0`.

---

### Example 3

**Input:**

```text
root = []
key = 0
```

**Output:**

```text
[]
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- Each node has a unique value.
- `root` is a valid binary search tree.
- `-10^5 <= key <= 10^5`

---

## Approach

Use recursion that returns the new root of each subtree, so the parent can reattach whatever comes back:

1. If `root` is `None`, there is nothing to delete, so return `None`.
2. If `key < root.val`, the target is in the left subtree. Set `root.left` to the result of deleting from `root.left`, then return `root`.
3. If `key > root.val`, do the same on the right side with `root.right`.
4. Otherwise `root` is the node to delete. There are three cases:
   - No left child: replace the node with its right child.
   - No right child: replace the node with its left child.
   - Two children: find the smallest node in the right subtree by walking left from `root.right`. Attach the deleted node's left subtree as that smallest node's left child, then replace the node with its right child.

In the two children case, every value in the old left subtree is smaller than everything in the right subtree, so hanging it off the leftmost node of the right subtree keeps the BST property intact.

---

## Example Walkthrough

For:

```text
root = [5,3,6,2,4,null,7]
key = 3
```

The tree looks like this:

```text
      5
     / \
    3   6
   / \   \
  2   4   7
```

At `5`, `3 < 5`, so go left and set `root.left` to whatever comes back from deleting in the subtree rooted at `3`.

At `3`, the key matches. It has both a left child `2` and a right child `4`, so use the two children case.

Find the smallest node in the right subtree. Start at `4`. It has no left child, so:

```text
smallest = 4
```

Attach the left subtree of `3` to it:

```text
4.left = 2
```

Return `root.right`, which is `4`, to replace `3`. Back at `5`:

```text
5.left = 4
```

The tree now looks like this:

```text
      5
     / \
    4   6
   /     \
  2       7
```

The final result is `[5,4,6,2,null,null,7]`.

---

## Complexity

Let `h` be the height of the tree.

- **Time Complexity:** `O(h)`
- **Space Complexity:** `O(h)`

The search walks down one path of the tree, and finding the smallest node in the right subtree walks down at most one more path. The recursion stack grows up to the height of the tree, which is `O(n)` in the worst case of a skewed tree.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
