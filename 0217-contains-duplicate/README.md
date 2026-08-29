# 217. Contains Duplicate

**Difficulty:** Easy

**LeetCode:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array.

Return `false` if every element in the array is distinct.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,2,3,1]
```

**Output:**

```text
true
```

**Explanation:**

The value `1` appears more than once in the array.

### Example 2

**Input:**

```text
nums = [1,2,3,4]
```

**Output:**

```text
false
```

**Explanation:**

All elements are distinct.

### Example 3

**Input:**

```text
nums = [1,1,1,3,3,4,3,2,4,2]
```

**Output:**

```text
true
```

**Explanation:**

Several values appear more than once in the array.

---

## Constraints

* `1 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

---

## Approach

This solution uses a **set** to efficiently detect duplicate values.

### Step 1: Handle `None`

The solution first checks whether `None` exists in the input:

```python
if None in nums:
    return False
```

If `None` is present, the solution returns `False`.

### Step 2: Compare Array and Set Lengths

A Python `set` only keeps unique values.

The solution compares the length of the original array with the length of the set:

```python
has_duplicate = len(nums) != len(set(nums))
```

If the lengths are different, it means at least one value appeared more than once.

For example:

```text
nums = [1,2,3,1]
```

The original length is:

```text
4
```

The set contains:

```text
{1,2,3}
```

Its length is:

```text
3
```

Since the lengths are different, a duplicate exists.

### Step 3: Return the Result

The boolean result is returned:

```python
return has_duplicate
```

---

## Complexity

Let `n` be the number of elements in `nums`.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Creating the set requires `O(n)` time on average and uses `O(n)` additional space to store the unique values.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
