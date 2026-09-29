# 1456. Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium

**LeetCode:** [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

---

## Problem

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Vowel letters in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

---

## Examples

### Example 1

**Input:**

```text
s = "abciiidef"
k = 3
```

**Output:**

```text
3
```

**Explanation:**

The substring `"iii"` contains 3 vowel letters.

---

### Example 2

**Input:**

```text
s = "aeiou"
k = 2
```

**Output:**

```text
2
```

**Explanation:**

Any substring of length 2 contains 2 vowels.

---

### Example 3

**Input:**

```text
s = "leetcode"
k = 3
```

**Output:**

```text
2
```

**Explanation:**

`"lee"`, `"eet"` and `"ode"` contain 2 vowels.

---

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= s.length`

---

## Approach

Use a sliding window of fixed size `k`:

- Build a set of vowels for quick lookup.
- Count the vowels in the first window of size `k`. This is the initial count and also the initial max.
- Slide the window one character at a time across the rest of the string.

To move the window from position `i-k` to `i`:

1. If the character entering the window, `s[i]`, is a vowel, increase the count.
2. If the character leaving the window, `s[i-k]`, is a vowel, decrease the count.
3. Compare the updated count to the current max and keep the larger one.

This avoids recounting vowels in the entire window every time it moves.

---

## Example Walkthrough

For:

```text
s = "leetcode"
k = 3
```

First window, indices `0` to `2`, which is `"lee"`:

```text
current_vowels = 2
max_vowels = 2
```

Slide to `i = 3`. Character entering is `s[3] = "t"`, not a vowel. Character leaving is `s[0] = "l"`, not a vowel:

```text
current_vowels = 2
max_vowels = 2
```

Slide to `i = 4`. Character entering is `s[4] = "c"`, not a vowel. Character leaving is `s[1] = "e"`, a vowel:

```text
current_vowels = 1
max_vowels = 2
```

Slide to `i = 5`. Character entering is `s[5] = "o"`, a vowel. Character leaving is `s[2] = "e"`, a vowel:

```text
current_vowels = 1
max_vowels = 2
```

Slide to `i = 6`. Character entering is `s[6] = "d"`, not a vowel. Character leaving is `s[3] = "t"`, not a vowel:

```text
current_vowels = 1
max_vowels = 2
```

Slide to `i = 7`. Character entering is `s[7] = "e"`, a vowel. Character leaving is `s[4] = "c"`, not a vowel:

```text
current_vowels = 2
max_vowels = 2
```

The final result is `2`.

---

## Complexity

Let `n` be the length of `s`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

Each character is visited once when it enters and once when it leaves the window, and only a fixed set of vowels and a few counters are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
