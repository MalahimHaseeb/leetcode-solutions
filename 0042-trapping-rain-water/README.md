# 42. Trapping Rain Water

**Difficulty:** Hard

**LeetCode:** [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

---

## Problem

Given an array `height` where each element represents the height of a bar and each bar has a width of `1`, calculate how much rain water can be trapped between the bars.

---

## Examples

### Example 1

**Input:**

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

**Output:**

```text
6
```

**Explanation:**

The elevation map can trap a total of `6` units of rain water.

### Example 2

**Input:**

```text
height = [4,2,0,3,2,5]
```

**Output:**

```text
9
```

---

## Constraints

* `n == height.length`
* `1 <= n <= 2 * 10^4`
* `0 <= height[i] <= 10^5`

---

## Approach

This solution finds the **highest bar** in the elevation map and uses it as the dividing point.

The highest bar acts as a boundary because no water can be trapped above it. The array is processed in two directions: from the left toward the highest bar and from the right toward the highest bar.

### Step 1: Find the Highest Bar

First, find the index of the tallest bar:

```python
maxIndex = height.index(max(height))
```

This index divides the elevation map into a left side and a right side.

### Step 2: Process the Left Side

Starting from the left, maintain the highest bar encountered so far using `left_max`.

For each bar:

* If the current bar is higher than `left_max`, update `left_max`.
* Otherwise, water can be trapped above the current bar.

The trapped water is:

```text
left_max - height[i]
```

### Step 3: Process the Right Side

Starting from the right, maintain the highest bar encountered so far using `right_max`.

For each bar:

* If the current bar is higher than `right_max`, update `right_max`.
* Otherwise, water can be trapped above the current bar.

The trapped water is:

```text
right_max - height[i]
```

### Step 4: Return the Total

The water calculated from both sides is accumulated in `water_trap` and returned.

---

## Example

For:

```text
height = [4,2,0,3,2,5]
```

The highest bar is `5`, so the array is processed toward that position.

The left scan calculates the water trapped before the highest bar, while the right scan calculates the water trapped after it.

The total trapped water is:

```text
9
```

---

## Complexity

Let `n` be the number of bars.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The array is scanned a constant number of times and only a few variables are used for additional storage.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
