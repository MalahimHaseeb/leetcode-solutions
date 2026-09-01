# 224. Basic Calculator

**Difficulty:** Hard

**LeetCode:** [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)

---

## Problem

Given a string `s` representing a valid mathematical expression, implement a basic calculator to evaluate the expression and return the result.

The expression can contain:

* Integers
* `+`
* `-`
* `(`
* `)`
* Spaces

Built-in functions such as `eval()` cannot be used to evaluate the expression.

---

## Examples

### Example 1

**Input:**

```text
s = "1 + 1"
```

**Output:**

```text
2
```

### Example 2

**Input:**

```text
s = " 2-1 + 2 "
```

**Output:**

```text
3
```

### Example 3

**Input:**

```text
s = "(1+(4+5+2)-3)+(6+8)"
```

**Output:**

```text
23
```

---

## Constraints

* `1 <= s.length <= 3 * 10^5`
* `s` consists of digits, `+`, `-`, `(`, `)`, and spaces.
* `s` represents a valid expression.
* `+` is not used as a unary operation.
* `-` can be used as a unary operation.
* There will be no two consecutive operators.
* Every number and running calculation fits in a signed 32-bit integer.

---

## Approach

This solution uses a **Stack** to handle parentheses while evaluating the expression from left to right.

The solution maintains three main variables:

```python
result = 0
number = 0
sign = 1
```

* `result` stores the current calculation.
* `number` builds the current multi-digit number.
* `sign` stores whether the current number should be added or subtracted.

A stack is used to temporarily store the calculation state before entering parentheses.

---

## Step 1: Build Numbers

When a digit is encountered:

```python
if char.isdigit():
    number = number * 10 + int(char)
```

This allows the solution to construct multi-digit numbers.

For example:

```text
"123"
```

is processed as:

```text
1
12
123
```

---

## Step 2: Handle `+`

When `+` is encountered, the current number is added using the previous sign:

```python
result += sign * number
```

Then the number is reset and the sign becomes positive:

```python
number = 0
sign = 1
```

---

## Step 3: Handle `-`

The same process is used for `-`:

```python
result += sign * number
number = 0
sign = -1
```

The current number is first added using the previous sign, and the new sign is stored for the next number.

---

## Step 4: Handle `(`

When an opening parenthesis is encountered, the current calculation needs to be saved before starting a new expression.

The solution stores:

```python
stack.append(result)
stack.append(sign)
```

Then starts a fresh calculation:

```python
result = 0
sign = 1
```

The stack therefore stores:

```text
previous result
previous sign
```

---

## Step 5: Handle `)`

When a closing parenthesis is encountered, the current expression inside the parentheses is completed:

```python
result += sign * number
number = 0
```

Then the sign that existed before the opening parenthesis is restored:

```python
result *= stack.pop()
```

Finally, the result from before the parenthesis is restored:

```python
result += stack.pop()
```

For example:

```text
2 + (3 + 4)
```

When processing `(3 + 4)`, the outer calculation `2 +` is temporarily stored.

After calculating `3 + 4 = 7`, the stored state is used to produce:

```text
2 + 7 = 9
```

---

## Example Walkthrough

Consider:

```text
(1+(4+5+2)-3)+(6+8)
```

The calculator processes the expression from left to right.

When it encounters:

```text
(
```

the current calculation state is pushed onto the stack.

Nested expressions are then evaluated independently.

For:

```text
(4+5+2)
```

the calculator produces:

```text
11
```

That value is then combined with the surrounding expression.

The entire expression evaluates to:

```text
23
```

---

## Why Use a Stack?

Parentheses create nested expressions.

For example:

```text
(1 + (4 + 5))
```

The calculator must temporarily remember the calculation outside the parentheses while evaluating the expression inside.

The stack provides exactly this functionality:

```text
Outer calculation
       ↓
     Stack
       ↓
Inner calculation
```

When `)` is encountered, the previous calculation state is retrieved.

---

## Complexity

Let `n` be the length of the expression.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Each character is processed once.

In the worst case, the stack can contain states for deeply nested parentheses, resulting in `O(n)` auxiliary space.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
