# 46. Permutations

**Difficulty:** Medium

**LeetCode:** [46. Permutations](https://leetcode.com/problems/permutations/)

---

## Problem

Given an array `nums` of distinct integers, return all the possible **permutations**.

The answer can be returned in any order.

---

## Examples

### Example 1

**Input:**

```text
nums = [1,2,3]
```

**Output:**

```text
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2

**Input:**

```text
nums = [0,1]
```

**Output:**

```text
[[0,1],[1,0]]
```

### Example 3

**Input:**

```text
nums = [1]
```

**Output:**

```text
[[1]]
```

---

## Constraints

* `1 <= nums.length <= 6`
* `-10 <= nums[i] <= 10`
* All the integers of `nums` are **unique**.

---

## Approach

This solution generates all permutations using the **Next Permutation** technique.

First, the array is sorted so that we start with the smallest possible permutation.

For example:

```text
[1,2,3]
```

The total number of permutations is calculated as `n!`.

For each next permutation:

1. Find the largest index `k` where:

```text
nums[k] < nums[k + 1]
```

2. Find the largest index `l` greater than `k` where:

```text
nums[l] > nums[k]
```

3. Swap `nums[k]` and `nums[l]`.

4. Reverse the elements after `k` to get the next smallest permutation.

The generated permutation is then added to `results`.

This process continues until all `n!` permutations have been generated.

---

## Example Walkthrough

For:

```text
nums = [1,2,3]
```

The permutations are generated in this order:

```text
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
```

There are:

```text
3! = 6
```

total permutations.

---

## Complexity

Let `n` be the number of elements in `nums`.

* **Time Complexity:** `O(n × n!)`
* **Space Complexity:** `O(n × n!)`

There are `n!` permutations, and each permutation requires `O(n)` time to copy into the result.

---

## Solution

The solution is implemented in [`solution.py`](./solution.py).
