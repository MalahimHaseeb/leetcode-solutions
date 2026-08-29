# 8. String to Integer (atoi)

**Difficulty:** Medium

**LeetCode:** [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

---

## Problem

Implement the `myAtoi(string s)` function to convert a string into a **32-bit signed integer**.

The conversion follows these rules:

1. Ignore leading whitespace.
2. Check for an optional `+` or `-` sign.
3. Read consecutive digits and convert them into an integer.
4. Stop reading when a non-digit character is encountered.
5. Clamp the result to the 32-bit signed integer range:

```text
[-2^31, 2^31 - 1]
```

If no digits are found, return `0`.

---

## Examples

### Example 1

**Input:**

```text
s = "42"
```

**Output:**

```text
42
```

**Explanation:**

There is no leading whitespace or sign. The digits `42` are read and converted to the integer `42`.

### Example 2

**Input:**

```text
s = " -042"
```

**Output:**

```text
-42
```

**Explanation:**

Leading whitespace is removed, the `-` sign is detected, and the digits `042` are converted to `42`.

Therefore, the result is `-42`.

### Example 3

**Input:**

```text
s = "1337c0d3"
```

**Output:**

```text
1337
```

**Explanation:**

The digits `1337` are read until the first non-digit character `c` is encountered.

### Example 4

**Input:**

```text
s = "0-1"
```

**Output:**

```text
0
```

**Explanation:**

The first character is a digit, so `0` is read. The conversion stops when `-` is encountered.

### Example 5

**Input:**

```text
s = "words and 987"
```

**Output:**

```text
0
```

**Explanation:**

The first character is not a digit or a valid sign, so no number can be extracted.

---

## Constraints

* `0 <= s.length <= 200`
* `s` consists of English letters, digits (`0-9`), spaces, `+`, `-`, and `.`.

---

## Approach

This solution processes the string in several steps.

### Step 1: Remove Leading and Trailing Whitespace

The solution first removes whitespace using:

```python
s = s.strip()
```

If the resulting string is empty, there is no number to convert:

```python
if not s:
    return 0
```

### Step 2: Determine the Sign

The solution starts with a positive sign:

```python
sign = 1
```

If the first character is `-`, the sign becomes negative:

```python
if s[i] == '-':
    sign = -1
    i += 1
```

If the first character is `+`, the sign remains positive and the pointer moves forward:

```python
elif s[i] == '+':
    i += 1
```

### Step 3: Convert Consecutive Digits

The solution reads digits one at a time:

```python
while i < len(s) and s[i].isdigit():
    num = num * 10 + int(s[i])
    i += 1
```

For example, converting `"123"` works as follows:

```text
num = 0
num = 0 * 10 + 1 = 1
num = 1 * 10 + 2 = 12
num = 12 * 10 + 3 = 123
```

The loop stops as soon as a non-digit character is encountered.

### Step 4: Apply the Sign

After reading the digits, the sign is applied:

```python
result = sign * num
```

For example:

```text
sign = -1
num = 42

result = -1 * 42
       = -42
```

### Step 5: Clamp to 32-bit Integer Range

The solution checks whether the result is outside the signed 32-bit integer range.

For values below the minimum:

```python
if result < -2**31:
    return -2**31
```

For values above the maximum:

```python
if result > 2**31 - 1:
    return 2**31 - 1
```

Otherwise, the result is returned normally.

---

## Example

For:

```text
s = " -042"
```

The processing is:

```text
" -042"
   ↓
"-042"        remove whitespace
   ↓
sign = -1     detect '-'
   ↓
"042"         read digits
   ↓
num = 42
   ↓
result = -42
```

Final result:

```text
-42
```

---

## Complexity

Let `n` be the length of the input string.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The string is scanned once to process the characters. `strip()` creates a processed string, resulting in `O(n)` additional space.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
