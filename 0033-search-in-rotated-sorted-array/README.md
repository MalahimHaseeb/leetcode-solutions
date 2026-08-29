# 33. Search in Rotated Sorted Array

**Difficulty:** Medium

**LeetCode:** [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

## Problem

There is an integer array `nums` sorted in ascending order with distinct values.

Before being passed to the function, `nums` is rotated at an unknown index.

For example:

```text
[0,1,2,4,5,6,7]
```

could become:

```text
[4,5,6,7,0,1,2]
```

Given the rotated array and an integer `target`, return the index of `target` if it exists.

Otherwise, return `-1`.

The algorithm must run in `O(log n)` time.

---

## Examples

### Example 1

**Input:**

```text
nums = [4,5,6,7,0,1,2]
target = 0
```

**Output:**

```text
4
```

### Example 2

**Input:**

```text
nums = [4,5,6,7,0,1,2]
target = 3
```

**Output:**

```text
-1
```

### Example 3

**Input:**

```text
nums = [1]
target = 0
```

**Output:**

```text
-1
```

---

## Constraints

* `1 <= nums.length <= 5000`
* `-10^4 <= nums[i] <= 10^4`
* All values of `nums` are unique.
* `nums` is sorted and rotated at an unknown index.
* `-10^4 <= target <= 10^4`

---

## Approach

This solution uses **Binary Search**.

Unlike a normal sorted array, a rotated sorted array is not completely sorted. However, at every step of the binary search, **at least one half of the current search range is sorted**.

The solution uses three pointers:

```python
low = 0
high = len(nums) - 1
mid = (low + high) // 2
```

### Step 1: Check the Middle Element

First, check whether the middle element is the target:

```python
if nums[mid] == target:
    return mid
```

If it is, return its index immediately.

### Step 2: Determine Which Half Is Sorted

We check:

```python
if nums[low] <= nums[mid]:
```

If this condition is true, the **left half is sorted**.

For example:

```text
[4, 5, 6, 7, 0, 1, 2]
 ↑        ↑
low      mid
```

The section from `low` to `mid` is sorted.

### Step 3: Check Whether Target Is in the Sorted Half

If the left half is sorted, check whether the target falls within its range:

```python
if nums[low] <= target < nums[mid]:
    high = mid - 1
```

If it does, search the left half.

Otherwise, discard the left half:

```python
low = mid + 1
```

### Step 4: Handle the Right Sorted Half

If the left half is not sorted, then the **right half must be sorted**.

```python
else:
    if nums[mid] < target <= nums[high]:
        low = mid + 1
    else:
        high = mid - 1
```

The target's range determines whether the search continues on the right or left.

### Step 5: Target Not Found

If `low` becomes greater than `high`, there is no valid search range remaining:

```python
return -1
```

---

## Example Walkthrough

Consider:

```text
nums = [4,5,6,7,0,1,2]
target = 0
```

Initial search:

```text
low = 0
high = 6
mid = 3
nums[mid] = 7
```

The left half:

```text
[4,5,6,7]
```

is sorted.

The target `0` is not inside that range, so we discard it:

```text
low = 4
```

Now:

```text
[0,1,2]
```

is the remaining search range.

The middle element is:

```text
nums[mid] = 1
```

Since `0 < 1`, we search the left side.

Eventually:

```text
nums[mid] = 0
```

and return:

```text
4
```

---

## Why This Works

A rotated sorted array contains two sorted sections.

For example:

```text
[4,5,6,7 | 0,1,2]
```

Although the complete array is not sorted, one side of the midpoint remains sorted.

By identifying the sorted side and checking whether the target belongs to that range, we can eliminate half of the remaining elements on every iteration.

This preserves the `O(log n)` complexity of Binary Search.

---

## Complexity

Let `n` be the number of elements in `nums`.

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

The search range is divided approximately in half after every iteration, and only a constant number of variables are used.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
