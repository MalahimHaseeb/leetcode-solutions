# 23. Merge k Sorted Lists

**Difficulty:** Hard

**LeetCode:** [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## Problem

You are given an array of `k` linked lists, where each linked list is sorted in ascending order.

Merge all the linked lists into one sorted linked list and return the resulting list.

---

## Examples

### Example 1

**Input:**

```text
lists = [[1,4,5],[1,3,4],[2,6]]
```

**Output:**

```text
[1,1,2,3,4,4,5,6]
```

**Explanation:**

The linked lists are:

```text
1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6
```

After merging them:

```text
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

### Example 2

**Input:**

```text
lists = []
```

**Output:**

```text
[]
```

### Example 3

**Input:**

```text
lists = [[]]
```

**Output:**

```text
[]
```

---

## Constraints

* `k == lists.length`
* `0 <= k <= 10^4`
* `0 <= lists[i].length <= 500`
* `-10^4 <= lists[i][j] <= 10^4`
* `lists[i]` is sorted in **ascending order**
* The sum of `lists[i].length` will not exceed `10^4`

---

## Approach

The solution uses a straightforward approach by collecting all node values first and then sorting them.

### Step 1: Collect Values

Iterate through every linked list and traverse each node.

Each node's value is added to a Python list called `values`.

### Step 2: Sort Values

After collecting all values from all linked lists, sort the `values` list using Python's built-in `sort()` method.

### Step 3: Build the Result

Create a new linked list using a dummy node.

For every value in the sorted `values` list:

* Create a new `ListNode`.
* Attach it to the result list.
* Move the `current` pointer forward.

Finally, return `dummy.next`.

### Example

Given:

```text
lists = [
    1 -> 4 -> 5,
    1 -> 3 -> 4,
    2 -> 6
]
```

All values are collected:

```text
[1, 4, 5, 1, 3, 4, 2, 6]
```

After sorting:

```text
[1, 1, 2, 3, 4, 4, 5, 6]
```

The final linked list becomes:

```text
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

---

## Complexity

Let `N` be the total number of nodes across all linked lists.

* **Time Complexity:** `O(N log N)`
* **Space Complexity:** `O(N)`

The `O(N log N)` time complexity comes from sorting all collected values.

The `O(N)` space complexity is used for storing the values and creating the resulting linked list.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
