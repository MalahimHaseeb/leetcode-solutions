# 392. Is Subsequence

**Difficulty:** Easy

**LeetCode:** [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

---

## Problem

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence is formed by deleting some or none of the characters from the original string without changing the relative order of the remaining characters.

For example, `"ace"` is a subsequence of `"abcde"`, while `"aec"` is not.

---

## Examples

### Example 1

**Input:**

```text
s = "abc"
t = "ahbgdc"
```

**Output:**

```text
true
```

**Explanation:**

The characters `a`, `b`, and `c` appear in `t` in the same order.

---

### Example 2

**Input:**

```text
s = "axc"
t = "ahbgdc"
```

**Output:**

```text
false
```

**Explanation:**

Although `a` and `c` appear in `t`, there is no `x` after `a`.

---

## Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

---

## Approach

Use two pointers:

- `i` points to the current character in `s`.
- `j` points to the current character in `t`.

The goal is to find every character of `s` inside `t` while maintaining their order.

For each character in `t`:

1. Compare `s[i]` with `t[j]`.
2. If they match, move both pointers forward.
3. If they do not match, only move `j` forward because the current character of `t` cannot be used.
4. Continue until either all characters of `s` are matched or `t` has been completely scanned.

If `i` reaches the length of `s`, then every character was found in the correct order.

An empty `s` is always a subsequence, so the solution returns `true` immediately when `s` is empty.

---

## Example Walkthrough

For:

```text
s = "abc"
t = "ahbgdc"
```

Initially:

```text
i = 0
j = 0
```

Compare:

```text
s[0] = "a"
t[0] = "a"
```

They match, so move both pointers:

```text
i = 1
j = 1
```

Now compare `"b"` with the characters in `t`.

`"h"` does not match, so move `j`.

Eventually:

```text
s[1] = "b"
t[2] = "b"
```

They match.

Continue searching for `"c"` and find it later in `t`.

At the end:

```text
i = 3
```

Since `i == len(s)`, all characters of `s` were matched, so the result is `true`.

---

## Complexity

Let `n` be the length of `s` and `m` be the length of `t`.

- **Time Complexity:** `O(m)`
- **Space Complexity:** `O(1)`

The `t` string is scanned at most once, and only two pointer variables are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
