# 34. Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium

**LeetCode:** [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

---

## Problem

Given an array of integers `nums` sorted in **non-decreasing order**, find the starting and ending position of a given `target` value.

If the target is not found in the array, return `[-1, -1]`.

The solution must run in **O(log n)** time.

---

## Examples

### Example 1

**Input:**

```text
nums = [5,7,7,8,8,10], target = 8
```

**Output:**

```text
[3,4]
```

### Example 2

**Input:**

```text
nums = [5,7,7,8,8,10], target = 6
```

**Output:**

```text
[-1,-1]
```

### Example 3

**Input:**

```text
nums = [], target = 0
```

**Output:**

```text
[-1,-1]
```

---

## Constraints

* `0 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`
* `nums` is a non-decreasing array.
* `-10^9 <= target <= 10^9`

---

## Approach

This solution uses **Binary Search** to find the first and last position of the target.

A single helper function `combined_logic()` is used for both searches.

The `isFirst` parameter determines which boundary to find:

* When `isFirst` is `True`, after finding the target, the search continues toward the **left** to find the first occurrence.
* When `isFirst` is `False`, after finding the target, the search continues toward the **right** to find the last occurrence.

If the target is not found, `bound` remains `-1`.

The helper function is called twice and the two positions are returned as:

```text
[first position, last position]
```

---

## Complexity

Let `n` be the number of elements in `nums`.

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

Binary search is performed twice, and each search takes `O(log n)` time.

---

## Solution

The solution is implemented in [`solution.py`](./solution.py).
