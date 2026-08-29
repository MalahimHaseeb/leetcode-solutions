# 704. Binary Search

**Difficulty:** Easy

**LeetCode:** [704. Binary Search](https://leetcode.com/problems/binary-search/)

---

## Problem

Given an array of integers `nums` which is sorted in **ascending order**, and an integer `target`, write a function to search for `target` in `nums`.

If `target` exists in the array, return its index.

If `target` does not exist, return `-1`.

The algorithm must run in `O(log n)` time.

---

## Examples

### Example 1

**Input:**

```text
nums = [-1,0,3,5,9,12]
target = 9
```

**Output:**

```text
4
```

**Explanation:**

The value `9` is present at index `4`.

### Example 2

**Input:**

```text
nums = [-1,0,3,5,9,12]
target = 2
```

**Output:**

```text
-1
```

**Explanation:**

The value `2` does not exist in the array.

---

## Constraints

* `1 <= nums.length <= 10^4`
* `-10^4 < nums[i], target < 10^4`
* All integers in `nums` are unique.
* `nums` is sorted in ascending order.

---

## Approach

This solution uses the **Binary Search** algorithm.

Instead of checking every element one by one, the solution repeatedly divides the search range in half.

Three variables are used:

```python
low = 0
high = len(nums) - 1
```

`low` represents the beginning of the current search range, while `high` represents the end.

### Step 1: Handle an Empty Array

If the input array is empty, there is nothing to search:

```python
if not nums:
    return -1
```

### Step 2: Initialize the Search Range

The search starts with the entire array:

```python
low = 0
high = len(nums) - 1
```

For example:

```text
nums = [-1, 0, 3, 5, 9, 12]

low  = 0
high = 5
```

### Step 3: Find the Middle Element

While there is still a valid search range:

```python
while low <= high:
```

the middle index is calculated:

```python
mid = int(low + (high - low) / 2)
```

This identifies the element in the middle of the current search range.

### Step 4: Check the Middle Element

If the middle element is the target:

```python
if target == nums[mid]:
    return mid
```

the index is immediately returned.

### Step 5: Search the Right Half

If the target is greater than the middle element:

```python
if target > nums[mid]:
    low = mid + 1
```

Because the array is sorted, everything to the left of `mid` can be ignored.

The search continues in the right half.

### Step 6: Search the Left Half

If the target is smaller than the middle element:

```python
else:
    high = mid - 1
```

Everything to the right of `mid` can be ignored.

The search continues in the left half.

### Step 7: Target Not Found

If the loop finishes without finding the target:

```python
return -1
```

This means the target does not exist in the array.

---

## Example Walkthrough

For:

```text
nums = [-1,0,3,5,9,12]
target = 9
```

The search proceeds as follows:

```text
low = 0
high = 5
mid = 2
nums[mid] = 3
```

Since:

```text
9 > 3
```

search the right half:

```text
low = 3
high = 5
```

Next:

```text
mid = 4
nums[mid] = 9
```

The target is found at index `4`.

Therefore:

```text
4
```

is returned.

---

## Why Binary Search?

A linear search would check elements one by one and could require `O(n)` time.

Because the array is already sorted, Binary Search can eliminate approximately half of the remaining elements after every comparison.

For example:

```text
1000 elements
    ↓
500
    ↓
250
    ↓
125
    ↓
...
```

This gives a logarithmic time complexity.

---

## Complexity

Let `n` be the number of elements in `nums`.

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

The solution uses only a few variables and performs the search iteratively, so it requires constant extra space.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
