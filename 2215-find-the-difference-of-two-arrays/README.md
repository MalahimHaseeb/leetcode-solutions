# 2215. Find the Difference of Two Arrays

**Difficulty:** Easy

**LeetCode:** [2215. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/)

---

## Problem

Given two 0-indexed integer arrays `nums1` and `nums2`, return a list `answer` of size `2` where:

- `answer[0]` is a list of all distinct integers in `nums1` which are not present in `nums2`.
- `answer[1]` is a list of all distinct integers in `nums2` which are not present in `nums1`.

Note that the integers in the lists may be returned in any order.

---

## Examples

### Example 1

**Input:**

```text
nums1 = [1,2,3]
nums2 = [2,4,6]
```

**Output:**

```text
[[1,3],[4,6]]
```

**Explanation:**

For `nums1`, `nums1[1] = 2` is present at index `0` of `nums2`, whereas `nums1[0] = 1` and `nums1[2] = 3` are not present in `nums2`. Therefore, `answer[0] = [1,3]`.

For `nums2`, `nums2[0] = 2` is present at index `1` of `nums1`, whereas `nums2[1] = 4` and `nums2[2] = 6` are not present in `nums1`. Therefore, `answer[1] = [4,6]`.

---

### Example 2

**Input:**

```text
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
```

**Output:**

```text
[[3],[]]
```

**Explanation:**

For `nums1`, `nums1[2]` and `nums1[3]` are not present in `nums2`. Since `nums1[2] == nums1[3]`, their value is only included once and `answer[0] = [3]`.

Every integer in `nums2` is present in `nums1`. Therefore, `answer[1] = []`.

---

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`

---

## Approach

Convert both arrays into sets to remove duplicates and get fast membership checks:

- `val_s1` is the set of distinct values in `nums1`.
- `va_s2` is the set of distinct values in `nums2`.

Once both are sets, the two answers are just set differences:

1. `val_s1.difference(va_s2)` gives every value in `nums1` that does not appear anywhere in `nums2`, which is `answer[0]`.
2. `va_s2.difference(val_s1)` gives every value in `nums2` that does not appear anywhere in `nums1`, which is `answer[1]`.

Since sets only store unique values and set difference is a direct operation, no manual looping or duplicate checking is needed.

---

## Example Walkthrough

For:

```text
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
```

Convert to sets:

```text
val_s1 = {1,2,3}
va_s2 = {1,2}
```

Compute `val_s1.difference(va_s2)`, values in `val_s1` not in `va_s2`:

```text
{3}
```

Compute `va_s2.difference(val_s1)`, values in `va_s2` not in `val_s1`:

```text
{}
```

The final result is `[[3], []]`.

---

## Complexity

Let `n` be the length of `nums1` and `m` be the length of `nums2`.

- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(n + m)`

Building each set takes time proportional to its input size, and computing set differences takes time proportional to the size of the sets involved.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
