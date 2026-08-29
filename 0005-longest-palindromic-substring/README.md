# 5. Longest Palindromic Substring

**Difficulty:** Medium

**LeetCode:** [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

---

## Problem

Given a string `s`, return the **longest palindromic substring** contained in `s`.

A palindrome is a string that reads the same forward and backward.

---

## Examples

### Example 1

**Input:**

```text id="5g1zq8"
s = "babad"
```

**Output:**

```text id="8j2m4x"
"bab"
```

**Explanation:**

`"aba"` is also a valid answer because it is also a longest palindromic substring.

### Example 2

**Input:**

```text id="3k7p1c"
s = "cbbd"
```

**Output:**

```text id="v5n9rx"
"bb"
```

---

## Constraints

* `1 <= s.length <= 1000`
* `s` consists of only digits and English letters.

---

## Approach

This solution uses the **Expand Around Center** technique.

Instead of checking every possible substring, the solution treats each character (and each gap between characters) as a possible center of a palindrome and expands outward.

A palindrome can have two types of centers:

* **Odd-length palindrome:** One character is the center.
* **Even-length palindrome:** The center is between two characters.

### Step 1: Handle an Empty String

If the input string is empty, return an empty string:

```python id="y3v8qn"
if not s:
    return ""
```

The solution then initializes the boundaries of the longest palindrome found so far:

```python id="p6x1kr"
start = end = 0
```

### Step 2: Expand Around a Center

The helper function `expand()` receives two positions:

```python id="d8q4mv"
def expand(left, right):
```

It expands outward while:

* `left` remains inside the string.
* `right` remains inside the string.
* The characters at both positions are equal.

```python id="a2j7fc"
while left >= 0 and right < len(s) and s[left] == s[right]:
    left -= 1
    right += 1
```

Once the characters no longer match, the pointers have moved one position beyond the actual palindrome.

Therefore, the valid palindrome boundaries are:

```python id="n5x3bz"
return left + 1, right - 1
```

### Step 3: Check Odd-Length Palindromes

For every character, the solution treats that character as the center:

```python id="k7q2hd"
l1, r1 = expand(i, i)
```

For example:

```text id="u3v6ca"
aba
 ^
center
```

The palindrome expands equally to the left and right.

### Step 4: Check Even-Length Palindromes

The solution also checks the gap between the current character and the next character:

```python id="f9m4st"
l2, r2 = expand(i, i + 1)
```

This handles palindromes such as:

```text id="p2c8wy"
bb
```

where there is no single middle character.

### Step 5: Update the Longest Palindrome

After checking both types of centers, the solution compares their lengths with the longest palindrome found so far:

```python id="z4n6qa"
if r1 - l1 > end - start:
    start, end = l1, r1

if r2 - l2 > end - start:
    start, end = l2, r2
```

Finally, the longest palindrome is returned:

```python id="c8v2hm"
return s[start:end + 1]
```

---

## Example

For:

```text id="a4k7ps"
s = "babad"
```

The algorithm checks every possible center.

For the center at the second character:

```text id="z6m3qr"
b a b
  ^
center
```

Expanding around `a` produces:

```text id="n8x1wv"
"bab"
```

The algorithm continues checking the remaining centers and keeps the longest palindrome found.

The result is:

```text id="t5r9kd"
"bab"
```

`"aba"` would also be a valid answer.

---

## Complexity

Let `n` be the length of the string.

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`

There are `O(n)` possible centers, and each center can require up to `O(n)` expansion.

The solution uses only a constant amount of additional space apart from the returned substring.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
