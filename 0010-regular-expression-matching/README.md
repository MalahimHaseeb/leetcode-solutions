# 10. Regular Expression Matching

**Difficulty:** Hard

**LeetCode:** [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

---

## Problem

Given an input string `s` and a pattern `p`, implement regular expression matching with support for:

* `.` — Matches any single character.
* `*` — Matches zero or more occurrences of the preceding element.

The pattern must match the **entire input string**, not just a part of it.

---

## Examples

### Example 1

**Input:**

```text
s = "aa"
p = "a"
```

**Output:**

```text
false
```

**Explanation:**

The pattern `"a"` only matches one character, so it cannot match the entire string `"aa"`.

### Example 2

**Input:**

```text
s = "aa"
p = "a*"
```

**Output:**

```text
true
```

**Explanation:**

`a*` means zero or more occurrences of `a`, so it can match `"aa"`.

### Example 3

**Input:**

```text
s = "ab"
p = ".*"
```

**Output:**

```text
true
```

**Explanation:**

`.*` means zero or more occurrences of any character, so it can match the entire string `"ab"`.

---

## Constraints

* `1 <= s.length <= 20`
* `1 <= p.length <= 20`
* `s` contains only lowercase English letters.
* `p` contains only lowercase English letters, `.`, and `*`.
* Every `*` has a valid preceding character.

---

## Approach

This solution uses **recursive backtracking** to determine whether the string matches the pattern.

The method processes the string and pattern from left to right.

### Step 1: Handle an Empty Pattern

If the pattern is empty, the string must also be empty for the match to succeed:

```python
if not p:
    return not s
```

If there are still characters remaining in `s`, the pattern cannot match the entire string.

### Step 2: Check the First Character

The solution checks whether the first character of the string matches the first character of the pattern.

A match occurs when:

* The string is not empty, and
* The pattern character equals the string character, or the pattern character is `.`.

```python
first_match = bool(s) and p[0] in {s[0], '.'}
```

### Step 3: Handle `*`

If the second character of the pattern is `*`, there are two possible choices.

```python
if len(p) >= 2 and p[1] == '*':
```

#### Option 1: Match Zero Occurrences

Skip the character followed by `*`:

```python
self.isMatch(s, p[2:])
```

For example:

```text
a* 
```

can match zero `a` characters.

#### Option 2: Match One or More Occurrences

If the first characters match, consume one character from the string while keeping the same pattern:

```python
first_match and self.isMatch(s[1:], p)
```

This allows `*` to continue matching additional occurrences.

The solution returns `True` if either option succeeds:

```python
return self.isMatch(s, p[2:]) or (
    first_match and self.isMatch(s[1:], p)
)
```

### Step 4: Handle a Normal Character or `.`

If the next pattern character is not `*`, the current characters must match.

The solution then recursively processes the remaining string and pattern:

```python
return first_match and self.isMatch(s[1:], p[1:])
```

---

## Example

For:

```text
s = "aa"
p = "a*"
```

The first `a` matches.

Because the next pattern character is `*`, the algorithm considers:

```text
1. Use a* as zero occurrences
2. Use a* to consume the current "a"
```

The second option consumes the first `a` and recursively checks the remaining string with the same pattern.

Eventually the entire string is consumed, resulting in:

```text
true
```

---

## Complexity

Let `m` be the length of `s` and `n` be the length of `p`.

* **Time Complexity:** `O(2^(m+n))` in the worst case
* **Space Complexity:** `O(m+n)` due to the recursive call stack

The worst-case time complexity comes from the branching caused by patterns containing `*`, where multiple matching possibilities may need to be explored.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
