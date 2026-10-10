# 437. Path Sum III

**Difficulty:** Medium

**LeetCode:** [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

---

## Problem

Given the `root` of a binary tree and an integer `targetSum`, return the number of paths where the sum of the values along the path equals `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards, traveling only from parent nodes to child nodes.

---

## Examples

### Example 1

**Input:**

```text
root = [10,5,-3,3,2,null,11,3,-2,null,1]
targetSum = 8
```

**Output:**

```text
3
```

**Explanation:**

The paths that sum to `8` are:

```text
5 -> 3
5 -> 2 -> 1
-3 -> 11
```

---

### Example 2

**Input:**

```text
root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
targetSum = 22
```

**Output:**

```text
3
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 1000]`.
- `-10^9 <= Node.val <= 10^9`
- `-1000 <= targetSum <= 1000`

---

## Approach

Use DFS with a prefix sum hash map, similar to the "subarray sum equals K" technique.

- `curr` is the sum of values from the root to the current node.
- `prefix` stores how many times each root-to-node sum has appeared on the **current path**.

A downward path ending at the current node has sum `targetSum` if some earlier prefix on the path equals:

```text
curr - targetSum
```

For each node:

1. Add the node's value to `curr`.
2. Add `prefix[curr - targetSum]` to the count, since each match is a valid path ending at this node.
3. Record `curr` in `prefix`.
4. Recurse into the left and right children.
5. Remove `curr` from `prefix` (backtrack) so it does not affect other branches.

The map starts as `{0: 1}` so paths starting at the root are counted.

---

## Example Walkthrough

For:

```text
root = [10,5,-3,3,2,null,11,3,-2,null,1]
targetSum = 8
```

Consider the path `10 -> 5 -> 3`.

The running sums along the path are:

```text
10, 15, 18
```

So `prefix` holds:

```text
{0: 1, 10: 1, 15: 1, 18: 1}
```

At node `3`, `curr = 18`:

```text
curr - targetSum = 18 - 8 = 10
```

`10` exists in `prefix`, so there is one path ending here with sum `8`:

```text
5 -> 3
```

After finishing a node, its prefix sum is removed so sibling branches only see their own ancestors.

---

## Complexity

Let `n` be the number of nodes in the binary tree and `h` its height.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(h)`

Each node is visited once. The hash map and recursion stack hold at most one entry per node on the current path.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
