# 4. Median of Two Sorted Arrays

**Difficulty:** Hard

**LeetCode:** [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

---

## Problem

Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n` respectively, return the **median** of the two sorted arrays.

The problem requires an overall time complexity of:

```text
O(log(m + n))
```

---

## Examples

### Example 1

**Input:**

```text
nums1 = [1,3]
nums2 = [2]
```

**Output:**

```text
2.00000
```

**Explanation:**

After combining and sorting the arrays:

```text
[1,2,3]
```

The median is `2`.

### Example 2

**Input:**

```text
nums1 = [1,2]
nums2 = [3,4]
```

**Output:**

```text
2.50000
```

**Explanation:**

After combining and sorting the arrays:

```text
[1,2,3,4]
```

The median is:

```text
(2 + 3) / 2 = 2.5
```

---

## Constraints

* `nums1.length == m`
* `nums2.length == n`
* `0 <= m <= 1000`
* `0 <= n <= 1000`
* `1 <= m + n <= 2000`
* `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

## Approach

This solution uses a straightforward **combine, sort, and calculate median** approach.

### Step 1: Combine the Arrays

The `extend()` method is used to add all elements of `nums2` to `nums1`.

```python
nums1.extend(nums2)
```

For example:

```text
nums1 = [1,3]
nums2 = [2]
```

After extending:

```text
[1,3,2]
```

### Step 2: Sort the Combined Array

The combined array is sorted using Python's built-in `sorted()` function.

```python
sorted_data = sorted(nums1)
```

The result becomes:

```text
[1,2,3]
```

### Step 3: Calculate the Median

Python's `statistics.median()` function is used to calculate the median of the sorted array.

```python
return statistics.median(sorted_data)
```

For:

```text
[1,2,3]
```

the median is:

```text
2
```

For an even number of elements such as:

```text
[1,2,3,4]
```

the median is:

```text
(2 + 3) / 2 = 2.5
```

---

## Complexity

Let `N = m + n` be the total number of elements.

* **Time Complexity:** `O(N log N)`
* **Space Complexity:** `O(N)`

The `O(N log N)` time complexity comes from sorting the combined array.

> **Note:** The problem asks for an `O(log(m+n))` solution. This implementation uses a simpler sorting-based approach and therefore does not meet the optimal time-complexity requirement.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
