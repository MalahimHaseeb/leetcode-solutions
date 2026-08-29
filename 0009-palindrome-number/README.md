# 9. Palindrome Number

**Difficulty:** Easy

**LeetCode:** [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

## Problem

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

A palindrome reads the same from left to right and right to left.

---

## Examples

### Example 1

**Input:**

```text id="c1w0wp"
x = 121
```

**Output:**

```text id="2y7n2r"
true
```

**Explanation:**

`121` reads as `121` from both directions.

### Example 2

**Input:**

```text id="4x1k7m"
x = -121
```

**Output:**

```text id="3m2z0k"
false
```

**Explanation:**

From left to right, the number is `-121`.

Reversed, it becomes `121-`, so it is not a palindrome.

### Example 3

**Input:**

```text id="q1j3f8"
x = 10
```

**Output:**

```text id="8j7n4p"
false
```

**Explanation:**

`10` reversed is `01`, so it is not a palindrome.

---

## Constraints

* `-2^31 <= x <= 2^31 - 1`

---

## Approach

This solution uses **string conversion and reversal** to check whether the integer reads the same in both directions.

### Step 1: Handle Negative Numbers

A negative number cannot be a palindrome because the negative sign appears only on one side.

The solution checks whether the number is negative:

```python id="9x6r8k"
if x != abs(x):
    return False
```

For example:

```text id="qz8m1a"
x = -121
abs(x) = 121
```

Since `-121 != 121`, the method immediately returns `False`.

### Step 2: Convert the Number to a String

For non-negative numbers, the integer is converted into a string:

```python id="5s4y2k"
str(x)
```

This makes it possible to easily compare the number with its reversed representation.

### Step 3: Reverse the String

Python slicing is used to reverse the string:

```python id="r0e7pq"
str(x)[::-1]
```

For example:

```text id="b7q4kc"
"121"[::-1] → "121"
"123"[::-1] → "321"
```

### Step 4: Compare Both Strings

The original and reversed strings are compared:

```python id="x3a9mv"
if str(x) == str(x)[::-1]:
    return True
```

If they are identical, the number is a palindrome.

Otherwise, the method returns `False`.

---

## Example

For:

```text id="8c5r2f"
x = 121
```

The comparison becomes:

```text id="x4e6yn"
"121" == "121"
```

Therefore:

```text id="g0d5jw"
true
```

For:

```text id="r8s3vd"
x = 123
```

The comparison becomes:

```text id="w9a2kp"
"123" != "321"
```

Therefore:

```text id="p4n7yc"
false
```

---

## Complexity

Let `n` be the number of digits in `x`.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The integer is converted to a string and a reversed copy of the string is created.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
