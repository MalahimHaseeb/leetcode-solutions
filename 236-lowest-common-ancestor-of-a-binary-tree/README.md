# 236. Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium

**LeetCode:** [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

---

## Problem

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

---

## Examples

### Example 1

**Input:**

```text
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 1
```

**Output:**

```text
3
```

**Explanation:**

The LCA of nodes `5` and `1` is `3`.

---

### Example 2

**Input:**

```text
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 4
```

**Output:**

```text
5
```

**Explanation:**

The LCA of nodes `5` and `4` is `5`, since a node can be a descendant of itself according to the LCA definition.

---

### Example 3

**Input:**

```text
root = [1,2]
p = 1
q = 2
```

**Output:**

```text
1
```

---

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the tree.

---

## Approach

Use a recursive DFS that returns, for each subtree, either one of the target nodes found in it or `None`:

- If `root` is `None`, or `root` is `p` or `q`, return `root`. Hitting a target node means there is no need to search deeper below it, since if the other target is under it, this node is the answer anyway.
- Otherwise, search both subtrees: `left` from `root.left` and `right` from `root.right`.

Then decide based on what came back:

1. If both `left` and `right` are non-null, `p` was found on one side and `q` on the other, so `root` is the lowest node that has both as descendants. Return `root`.
2. If only one side is non-null, both targets (or the one target found) are on that side, so pass that result up.
3. If both are `None`, neither target is in this subtree, so return `None`.

The first node where the two targets split into different subtrees is the LCA. If one target sits above the other, the upper one is returned directly by the first rule and bubbles up unchanged.

---

## Example Walkthrough

For:

```text
root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 4
```

Start at `3`. It is not `p` or `q`, so search both subtrees.

Go left to `5`. `5` is `p`, so return it immediately without searching below:

```text
left = 5
```

Go right to `1`. It is not a target, so search its subtrees. Go to `0`, a leaf that is not a target, return `None`. Go to `8`, a leaf that is not a target, return `None`:

```text
right = None
```

Back at `3`, `left` is non-null and `right` is `None`, so only one side found something. Return `left`:

```text
result = 5
```

Node `4` sits below `5`, so it was never visited, but that is fine because `5` already covers it as an ancestor of itself. The final result is `5`.

---

## Complexity

Let `n` be the number of nodes in the tree and `h` be its height.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(h)`

Each node is visited at most once, and the recursion stack grows up to the height of the tree, which is `O(n)` in the worst case of a skewed tree.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
