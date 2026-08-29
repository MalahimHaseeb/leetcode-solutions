# 7. Reverse Integer

**Difficulty:** Medium

**LeetCode:** [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

---

## Problem

Given a signed 32-bit integer `x`, return the integer with its **digits reversed**.

If reversing the digits causes the result to go outside the signed 32-bit integer range:

```text
[-2^31, 2^31 - 1]
```

return `0`.

---

## Examples

### Example 1

**Input:**

```text
x = 123
```

**Output:**

```text
321
```

**Explanation:**

Reversing the digits of `123` produces `321`.

### Example 2

**Input:**

```text
x = -123
```

**Output:**

```text
-321
```

**Explanation:**

The digits of `123` are reversed to `321`, and the original negative sign is preserved.

### Example 3

**Input:**

```text
x = 120
```

**Output:**

```text
21
```

**Explanation:**

Reversing `120` produces `021`, which is interpreted as the integer `21`.

---

## Constraints

* `-2^31 <= x <= 2^31 - 1`

---

## Approach

This solution uses **string conversion and reversal** to reverse the digits.

### Step 1: Store the Sign

The sign of the original number is stored separately:

```python
sign = -1 if x < 0 else 1
```

This allows the digits to be reversed without worrying about the negative sign.

For example:

```text
x = -123
sign = -1
```

### Step 2: Get the Absolute Value

The absolute value is used to remove the negative sign:

```python
abs(x)
```

For:

```text
x = -123
```

the absolute value is:

```text
123
```

### Step 3: Reverse the Digits

The absolute value is converted to a string and reversed using Python slicing:

```python
str(abs(x))[::-1]
```

For example:

```text
"123"[::-1] → "321"
```

The reversed string is then converted back into an integer:

```python
rev = int(str(abs(x))[::-1]) * sign
```

The original sign is multiplied back into the reversed number.

### Step 4: Check the 32-bit Range

The resulting number must remain within:

```text
[-2^31, 2^31 - 1]
```

The solution checks both boundaries:

```python
if rev < -(2**31) or rev > (2**31 - 1):
    return 0
```

If the reversed number exceeds the allowed range, `0` is returned.

Otherwise, the reversed number is returned.

---

## Example

For:

```text
x = -123
```

The solution processes it as:

```text
Sign        → -1
Absolute    → 123
Reverse     → 321
Apply sign  → -321
Range check → valid
```

Final result:

```text
-321
```

For:

```text
x = 120
```

the reversed string is:

```text
"021"
```

Converting it to an integer removes the leading zero:

```text
21
```

---

## Complexity

Let `n` be the number of digits in `x`.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The number is converted into a string and a reversed string is created.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
