# 394. Decode String

**Difficulty:** Medium

**LeetCode:** [394. Decode String](https://leetcode.com/problems/decode-string/)

---

## Problem

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed `10^5`.

---

## Examples

### Example 1

**Input:**

```text
s = "3[a]2[bc]"
```

**Output:**

```text
"aaabcbc"
```

---

### Example 2

**Input:**

```text
s = "3[a2[c]]"
```

**Output:**

```text
"accaccacc"
```

---

### Example 3

**Input:**

```text
s = "2[abc]3[cd]ef"
```

**Output:**

```text
"abcabccdcdcdef"
```

---

## Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be a valid input.
- All the integers in `s` are in the range `[1, 300]`.

---

## Approach

Use a stack to handle nested brackets, since decoding `3[a2[c]]` requires finishing the inner `2[c]` before the outer `3[...]` can repeat it.

Keep two running pieces of state while scanning left to right:

- `current`, a list of characters being built for whatever bracket level we're currently inside (or the top level before any bracket).
- `num`, the digits seen so far for the next `k` value.

For each character in `s`:

1. If it's a digit, accumulate it into `num`. Since `k` can be more than one digit (like `12[a]`), build it up as `num * 10 + int(char)` rather than assuming a single digit.
2. If it's `[`, we're about to enter a new nested level. Push the current `(current, num)` pair onto the stack so we can come back to it later, then reset `current` to an empty list and `num` to `0` to start building the new level fresh.
3. If it's `]`, the nested level just closed. Pop the `(prev, k)` pair that was saved when this level opened. Join `current` into a string, repeat it `k` times, and append that repeated string onto `prev`, the list from the outer level. Then set `current = prev` so we continue building from where the outer level left off.
4. Otherwise, it's a regular letter, so just append it to `current`.

At the end, `current` holds the fully decoded string at the top level, so join it into a string and return it.

---

## Example Walkthrough

For:

```text
s = "3[a2[c]]"
```

Start with `stack = []`, `current = []`, `num = 0`.

Char `3`, a digit:

```text
num = 3
```

Char `[`, push `(current, num)` and reset:

```text
stack = [([], 3)]
current = []
num = 0
```

Char `a`, append it:

```text
current = ['a']
```

Char `2`, a digit:

```text
num = 2
```

Char `[`, push `(current, num)` and reset:

```text
stack = [([], 3), (['a'], 2)]
current = []
num = 0
```

Char `c`, append it:

```text
current = ['c']
```

Char `]`, pop `(prev, k) = (['a'], 2)`. Join `current` to get `"c"`, repeat it `2` times to get `"cc"`, append to `prev`:

```text
current = ['a', 'cc']
```

Char `]`, pop `(prev, k) = ([], 3)`. Join `current` to get `"acc"`, repeat it `3` times to get `"accaccacc"`, append to `prev`:

```text
current = ['accaccacc']
```

Join `current` at the end to get the final result: `"accaccacc"`.

---

## Complexity

Let `n` be the length of the decoded output string.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

Each character of the final decoded string is appended and copied a bounded number of times as brackets close, and the stack depth is bounded by the nesting level of brackets in `s`.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
