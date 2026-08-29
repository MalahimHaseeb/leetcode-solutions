# 11. Container With Most Water

**Difficulty:** Medium

**LeetCode:** [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## Problem

You are given an integer array `height` where each element represents the height of a vertical line.

Choose two lines that, together with the x-axis, form a container that can hold the maximum amount of water.

Return the **maximum amount of water** that the container can store.

The container cannot be slanted.

---

## Examples

### Example 1

**Input:**

```text
height = [1,8,6,2,5,4,8,3,7]
```

**Output:**

```text
49
```

**Explanation:**

The two lines with heights `8` and `7` create the maximum container.

The width between them is `7`, and the limiting height is `7`.

```text
Area = 7 × 7 = 49
```

### Example 2

**Input:**

```text
height = [1,1]
```

**Output:**

```text
1
```

---

## Constraints

* `n == height.length`
* `2 <= n <= 10^5`
* `0 <= height[i] <= 10^4`

---

## Approach

This solution uses the **Two Pointer** technique.

Two pointers are initialized at the two ends of the array:

```python
left = 0
right = len(height) - 1
```

At every step, the current container is calculated using the distance between the two pointers and the shorter of the two heights.

### Step 1: Calculate the Width

The width of the container is:

```python
width = right - left
```

### Step 2: Find the Limiting Height

The amount of water is limited by the shorter line:

```python
current_height = min(height[left], height[right])
```

The current container area is therefore:

```python
current_water = width * current_height
```

If the current area is greater than the maximum found so far, `max_water` is updated.

### Step 3: Move the Pointer

After calculating the current area, the pointer at the **shorter line** is moved inward.

```python
if height[left] < height[right]:
    left += 1
else:
    right -= 1
```

The reason is that moving the taller line cannot increase the container's height because the shorter line is still limiting the water level. Moving the shorter line gives the possibility of finding a taller boundary while the width decreases.

### Example

For:

```text
height = [1,8,6,2,5,4,8,3,7]
```

The pointers start at:

```text
left  = 0
right = 8
```

The algorithm repeatedly calculates the area and moves the pointer corresponding to the shorter height.

The maximum area found is:

```text
49
```

---

## Complexity

Let `n` be the number of heights.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

Each pointer moves toward the other pointer at most `n` times, and only a constant amount of additional memory is used.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
