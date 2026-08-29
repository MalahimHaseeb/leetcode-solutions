# 295. Find Median from Data Stream

**Difficulty:** Hard

**LeetCode:** [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

---

## Problem

The **median** is the middle value in an ordered list of integers.

* If the list contains an odd number of elements, the median is the middle element.
* If the list contains an even number of elements, the median is the average of the two middle elements.

Implement the `MedianFinder` class with two operations:

* `addNum(num)` — Add an integer to the data structure.
* `findMedian()` — Return the median of all elements added so far.

---

## Examples

### Example 1

**Input:**

```text
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
```

**Output:**

```text
[null, null, null, 1.5, null, 2.0]
```

**Explanation:**

```text
addNum(1)       -> [1]
addNum(2)       -> [1, 2]
findMedian()    -> 1.5

addNum(3)       -> [1, 2, 3]
findMedian()    -> 2.0
```

---

## Constraints

* `-10^5 <= num <= 10^5`
* There will be at least one element before calling `findMedian()`.
* At most `5 * 10^4` calls will be made to `addNum()` and `findMedian()`.

---

## Approach

This solution maintains all numbers in a **sorted array**.

### Step 1: Initialize the Array

The `MedianFinder` class starts with an empty array:

```python
self.arr = []
```

The array is always kept sorted after every call to `addNum()`.

### Step 2: Find the Insertion Position

When a new number is added, **binary search** is used to find the correct position where the number should be inserted.

```python
low = 0
high = len(self.arr)

while low < high:
    mid = (low + high) // 2

    if self.arr[mid] < num:
        low = mid + 1
    else:
        high = mid
```

After the binary search, `low` represents the correct insertion position.

### Step 3: Insert the Number

The number is inserted at the position found by binary search:

```python
self.arr.insert(low, num)
```

This keeps the array sorted.

For example, if the current array is:

```text
[1, 3, 5, 7]
```

and `2` is added, binary search finds position `1`:

```text
[1, 2, 3, 5, 7]
```

### Step 4: Find the Median

The `findMedian()` method checks whether the number of elements is odd or even.

For an odd number of elements, the middle element is returned:

```python
return float(self.arr[mid])
```

For an even number of elements, the two middle elements are averaged:

```python
return (self.arr[mid - 1] + self.arr[mid]) / 2.0
```

For example:

```text
[1, 2, 3]       -> 3? 
```

The middle element is `2`, so the median is `2.0`.

For:

```text
[1, 2, 3, 4]
```

the median is:

```text
(2 + 3) / 2 = 2.5
```

---

## Complexity

Let `N` be the number of elements currently stored.

### `addNum()`

* **Binary Search:** `O(log N)`
* **Insertion:** `O(N)`
* **Overall:** `O(N)`

Although binary search finds the insertion position in `O(log N)`, inserting into a Python list can require shifting elements, resulting in `O(N)` time.

### `findMedian()`

* **Time:** `O(1)`
* **Space:** `O(N)`

---

## Solution

The implementation is available in [`solution.py`](solution.py).
