# 2130. Maximum Twin Sum of a Linked List

**Difficulty:** Medium

**LeetCode:** [2130. Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

---

## Problem

In a linked list of size `n`, where `n` is even, the `ith` node (0-indexed) of the linked list is known as the twin of the `(n-1-i)th` node, if `0 <= i <= (n / 2) - 1`.

- For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1` is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The twin sum is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return the maximum twin sum of the linked list.

---

## Examples

### Example 1

**Input:**

```text
head = [5,4,2,1]
```

**Output:**

```text
6
```

**Explanation:**

Nodes `0` and `1` are the twins of nodes `3` and `2`, respectively. All have twin sum `6`. There are no other nodes with twins in the linked list. Thus, the maximum twin sum of the linked list is `6`.

---

### Example 2

**Input:**

```text
head = [4,2,2,3]
```

**Output:**

```text
7
```

**Explanation:**

The nodes with twins present in this linked list are:

- Node `0` is the twin of node `3`, having a twin sum of `4 + 3 = 7`.
- Node `1` is the twin of node `2`, having a twin sum of `2 + 2 = 4`.

Thus, the maximum twin sum of the linked list is `max(7, 4) = 7`.

---

### Example 3

**Input:**

```text
head = [1,100000]
```

**Output:**

```text
100001
```

**Explanation:**

There is only one node with a twin in the linked list, having a twin sum of `1 + 100000 = 100001`.

---

## Constraints

- The number of nodes in the list is an even integer in the range `[2, 10^5]`.
- `1 <= Node.val <= 10^5`

---

## Approach

Twin sums pair up the list from both ends at once, index `i` with index `n-1-i`, which is much easier to do with direct index access than by walking pointers from both directions at once. So first flatten the linked list into a plain list of values:

- Walk the linked list once, appending each `head.val` to `vals`, until `head` becomes `None`.

With `vals` in hand, `n = len(vals)` gives the list length. Since twins only exist for `i` from `0` to `n/2 - 1`, loop over that range:

1. For each `i`, compute the twin sum `vals[i] + vals[n-1-i]`.
2. Track the largest twin sum seen in `best`.

After the loop, `best` holds the maximum twin sum across the whole list.

---

## Example Walkthrough

For:

```text
head = [4,2,2,3]
```

Flatten into a list:

```text
vals = [4, 2, 2, 3]
n = 4
```

Start with `best = 0`.

At `i = 0`, twin sum is `vals[0] + vals[3] = 4 + 3 = 7`:

```text
best = max(0, 7) = 7
```

At `i = 1`, twin sum is `vals[1] + vals[2] = 2 + 2 = 4`:

```text
best = max(7, 4) = 7
```

The loop ends since `n // 2 = 2`. The final result is `7`.

---

## Complexity

Let `n` be the number of nodes in the linked list.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

The list is traversed once to build `vals`, and then iterated once more over half its length. Storing all values takes `O(n)` extra space.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
