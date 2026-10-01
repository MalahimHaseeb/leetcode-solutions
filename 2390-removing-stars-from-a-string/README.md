# 2390. Removing Stars From a String

**Difficulty:** Medium

**LeetCode:** [2390. Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/)

---

## Problem

You are given a string `s`, which contains stars `*`.

In one operation, you can:

- Choose a star in `s`.
- Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:

- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.

---

## Examples

### Example 1

**Input:**

```text
s = "leet**cod*e"
```

**Output:**

```text
"lecoe"
```

**Explanation:**

Performing the removals from left to right:

- The closest character to the 1st star is `t` in `"leet**cod*e"`. `s` becomes `"lee*cod*e"`.
- The closest character to the 2nd star is `e` in `"lee*cod*e"`. `s` becomes `"lecod*e"`.
- The closest character to the 3rd star is `d` in `"lecod*e"`. `s` becomes `"lecoe"`.

There are no more stars, so we return `"lecoe"`.

---

### Example 2

**Input:**

```text
s = "erase*****"
```

**Output:**

```text
""
```

**Explanation:**

The entire string is removed, so we return an empty string.

---

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters, uppercase English letters, and stars `*`.
- The input is generated such that the operation is always possible.

---

## Approach

Use a stack to simulate the removals as a single left-to-right pass:

- Walk through each character in `s`.
- If the character is a star, it means "remove the most recent character still standing," which is exactly the top of the stack, so pop the stack and skip adding the star.
- If the character is a regular letter, push it onto the stack.

Since the stack always holds the characters that haven't been cancelled out yet, in their original order, joining the stack at the end gives the final string directly.

---

## Example Walkthrough

For:

```text
s = "leet**cod*e"
```

Start with `stack = []`.

Push `l, e, e, t`:

```text
stack = ['l','e','e','t']
```

Hit `*`, pop the top:

```text
stack = ['l','e','e']
```

Hit `*`, pop the top:

```text
stack = ['l','e']
```

Push `c, o, d`:

```text
stack = ['l','e','c','o','d']
```

Hit `*`, pop the top:

```text
stack = ['l','e','c','o']
```

Push `e`:

```text
stack = ['l','e','c','o','e']
```

Join the stack to get the final result: `"lecoe"`.

---

## Complexity

Let `n` be the length of `s`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

Each character triggers at most one push and one pop, and the stack holds up to `n` characters.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
