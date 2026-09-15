# 2095. Delete the Middle Node of a Linked List

**Difficulty:** Medium

**LeetCode:** [2095. Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

---

## Problem

Given the `head` of a linked list, delete the **middle node** and return the `head` of the modified linked list.

The middle node is the node at index `floor(n / 2)` using **0-based indexing**.

For example:

- `n = 1` → middle index `0`
- `n = 2` → middle index `1`
- `n = 3` → middle index `1`
- `n = 4` → middle index `2`
- `n = 5` → middle index `2`

---

## Examples

### Example 1

**Input:**

```text
head = [1,3,4,7,1,2,6]
```

**Output:**

```text
[1,3,4,1,2,6]
```

The middle node is `7`, so it is removed.

### Example 2

**Input:**

```text
head = [1,2,3,4]
```

**Output:**

```text
[1,2,4]
```

The middle node is `3`, so it is removed.

### Example 3

**Input:**

```text
head = [2,1]
```

**Output:**

```text
[2]
```

The middle node is `1`, so it is removed.

---

## Constraints

- The number of nodes is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`

---

## Approach

This solution uses the **Slow and Fast Pointer** technique.

We use two pointers:

- `slow` moves one node at a time.
- `fast` moves two nodes at a time.
- `prev` keeps track of the node before `slow`.

When `fast` reaches the end of the linked list, `slow` points to the middle node.

We can then delete the middle node by skipping it:

```python
prev.next = slow.next
```

For a single-node linked list, the middle node is the only node, so we return `None`.

---

## Example Walkthrough

For:

```text
head = [1,3,4,7,1,2,6]
```

The linked list is:

```text
1 → 3 → 4 → 7 → 1 → 2 → 6
```

The slow pointer moves one step at a time while the fast pointer moves two steps.

Eventually:

```text
prev → 4
slow → 7
fast → 6
```

So `7` is the middle node.

We remove it by connecting `4` directly to `1`:

```text
4.next = 1
```

The resulting list is:

```text
1 → 3 → 4 → 1 → 2 → 6
```

---

## Complexity

Let `n` be the number of nodes in the linked list.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

The linked list is traversed once and no additional data structure is required.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
