# 1. Two Sum

**Difficulty:** Easy

**LeetCode:** [1. Two Sum](https://leetcode.com/problems/two-sum/)

---

## Problem

Given an array of integers `nums` and an integer `target`, return the **indices of the two numbers** such that they add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

The answer can be returned in any order.

---

## Examples

### Example 1

**Input:**

```text
nums = [2,7,11,15]
target = 9
```

**Output:**

```text
[0,1]
```

**Explanation:**

```text
nums[0] + nums[1] = 2 + 7 = 9
```

Therefore, the answer is `[0, 1]`.

### Example 2

**Input:**

```text
nums = [3,2,4]
target = 6
```

**Output:**

```text
[1,2]
```

### Example 3

**Input:**

```text
nums = [3,3]
target = 6
```

**Output:**

```text
[0,1]
```

---

## Constraints

* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* Only one valid answer exists.

---

## Approach

This solution iterates through the array and calculates the number required to reach the target.

For every number, the required value is calculated as:

```python
remainder = target - current
```

If this remainder exists in the array, its index is found and returned together with the current index.

### Step 1: Iterate Through the Array

The solution uses `enumerate()` to keep track of both the index and value:

```python
for i, num in enumerate(nums):
    curr = num
```

For example:

```text
nums = [2,7,11,15]
target = 9
```

On the first iteration:

```text
curr = 2
i = 0
```

### Step 2: Calculate the Required Number

The required number is calculated by subtracting the current number from the target:

```python
rem = target - curr
```

For the first number:

```text
target = 9
curr = 2

rem = 9 - 2
rem = 7
```

So the solution looks for `7` in the array.

### Step 3: Check Whether the Remainder Exists

The solution checks:

```python
if rem in nums:
```

If the remainder exists, its index is found using:

```python
j = nums.index(rem)
```

For the example:

```text
nums = [2,7,11,15]

rem = 7
index of 7 = 1
```

### Step 4: Make Sure the Same Element Is Not Used

The problem does not allow using the same array element twice.

Therefore, the solution checks:

```python
if i != j:
    return [i, j]
```

For the first iteration:

```text
i = 0
j = 1
```

Since the indices are different, the solution returns:

```text
[0,1]
```

---

## Example Walkthrough

For:

```text
nums = [2,7,11,15]
target = 9
```

The solution performs:

```text
Current number: 2
Current index: 0

Required number:
9 - 2 = 7

7 exists in nums
Index of 7 = 1

0 != 1
```

Therefore:

```text
[0,1]
```

---

## Complexity

Let `n` be the number of elements in `nums`.

The solution uses:

* `in` to check whether the remainder exists in the list.
* `.index()` to find the remainder's index.

Both operations can take `O(n)` in the worst case.

Since this is done while iterating through the array:

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`

---

## Follow-up

The problem asks whether it is possible to solve Two Sum in less than `O(n²)` time.

A common optimization is to use a **hash map** to store previously seen values and their indices, allowing the required complement to be found in approximately `O(1)` average time.

That optimized approach can achieve:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

This repository keeps the implementation shown above as the original solution.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
