# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy

**LeetCode:** [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## Problem

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** so that each unique element appears only once.

Return the number of unique elements `k`.

After removing the duplicates:

* The first `k` elements of `nums` should contain the unique values.
* The unique values must remain in sorted order.
* Elements after index `k - 1` can be ignored.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,1,2]
```

**Output:**

```text
2
```

The modified array becomes:

```text
[1,2,_]
```

### Example 2

**Input:**

```text
nums = [0,0,1,1,1,2,2,3,3,4]
```

**Output:**

```text
5
```

The modified array becomes:

```text
[0,1,2,3,4,_,_,_,_,_]
```

---

## Constraints

* `1 <= nums.length <= 3 * 10^4`
* `-100 <= nums[i] <= 100`
* `nums` is sorted in non-decreasing order.

---

## Approach

This solution removes duplicates by converting the array into a `set`.

A set only stores **unique values**, so:

```python
set(nums)
```

removes all duplicate elements.

The solution then sorts the unique values and replaces the contents of the original list:

```python
nums[:] = sorted(set(nums))
```

Using `nums[:]` updates the original list **in-place**, which is important because the LeetCode judge checks the original array.

Finally, the number of unique elements is returned:

```python
return len(nums)
```

---

## Example Walkthrough

For:

```text
nums = [0,0,1,1,1,2,2,3,3,4]
```

First:

```python
set(nums)
```

produces the unique values:

```text
{0,1,2,3,4}
```

Then:

```python
sorted(set(nums))
```

produces:

```text
[0,1,2,3,4]
```

The slice assignment:

```python
nums[:] = [0,1,2,3,4]
```

updates the original array.

Finally:

```python
len(nums)
```

returns:

```text
5
```

---

## Complexity

Let `n` be the number of elements in `nums`.

* **Time Complexity:** `O(n log n)`
* **Space Complexity:** `O(n)`

The `set` requires `O(n)` additional space, and sorting the unique values takes `O(n log n)` in the worst case.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
