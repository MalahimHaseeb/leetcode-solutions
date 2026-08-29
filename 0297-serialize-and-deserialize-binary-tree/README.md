# 297. Serialize and Deserialize Binary Tree

**Difficulty:** Hard

**LeetCode:** [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

---

## Problem

Serialization is the process of converting a data structure into a string so that it can be stored or transmitted and later reconstructed.

Design an algorithm to **serialize and deserialize a binary tree**.

The serialized string must contain enough information to reconstruct the original tree with the same structure and node values.

---

## Examples

### Example 1

**Input:**

```text
root = [1,2,3,null,null,4,5]
```

**Output:**

```text
[1,2,3,null,null,4,5]
```

The original tree is:

```text
        1
       / \
      2   3
         / \
        4   5
```

### Example 2

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

* The number of nodes in the tree is in the range `[0, 10^4]`.
* `-1000 <= Node.val <= 1000`

---

## Approach

This solution uses **Depth-First Search (DFS)** with **preorder traversal**.

The traversal order is:

```text
Root -> Left -> Right
```

The solution has two main parts: **serialization** and **deserialization**.

### Serialization

The `serialize()` method traverses the tree using DFS.

For every node:

1. If the node is `None`, add `"#"` to the result.
2. Otherwise, add the node's value as a string.
3. Recursively traverse the left child.
4. Recursively traverse the right child.

The values are then joined using commas.

For example, this tree:

```text
        1
       / \
      2   3
         / \
        4   5
```

is serialized as:

```text
1,2,#,#,3,4,#,#,5,#,#
```

The `#` symbols represent `None` nodes. They are important because they preserve the structure of the original tree.

### Deserialization

The `deserialize()` method first splits the serialized string by commas.

For example:

```text
1,2,#,#,3,4,#,#,5,#,#
```

becomes:

```text
["1", "2", "#", "#", "3", "4", "#", "#", "5", "#", "#"]
```

A recursive DFS function then processes these values in preorder.

For each value:

1. Remove the first value using `pop(0)`.
2. If the value is `"#"`, return `None`.
3. Otherwise, create a new `TreeNode`.
4. Recursively construct the left subtree.
5. Recursively construct the right subtree.

Because the same preorder order and `#` markers are used during serialization, the original tree structure can be reconstructed.

---

## Complexity

Let `N` be the number of nodes in the binary tree.

### Serialization

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(N)`

### Deserialization

* **Time Complexity:** `O(N²)` in this implementation because `values.pop(0)` shifts the remaining elements in the Python list.
* **Space Complexity:** `O(N)`

The recursive call stack and the list of serialized values require additional space.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
