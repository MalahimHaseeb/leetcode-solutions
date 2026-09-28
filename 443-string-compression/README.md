# 443. String Compression

**Difficulty:** Medium

**LeetCode:** [443. String Compression](https://leetcode.com/problems/string-compression/)

---

## Problem

Given an array of characters `chars`, compress it using the following algorithm.

For each group of consecutive repeating characters:

- If the group's length is `1`, keep only the character.
- Otherwise, write the character followed by its count.
- Counts of `10` or greater are written as multiple characters.

The compressed result must be stored directly inside the input array `chars`.

Return the new length of the compressed array.

The algorithm must use only constant extra space.

---

## Examples

### Example 1

**Input:**

```text
chars = ["a","a","b","b","c","c","c"]
```

**Output:**

```text
6
```

**Explanation:**

The groups are `"aa"`, `"bb"`, and `"ccc"`.

After compression:

```text
["a","2","b","2","c","3"]
```

---

### Example 2

**Input:**

```text
chars = ["a"]
```

**Output:**

```text
1
```

**Explanation:**

The character appears only once, so it remains unchanged.

---

### Example 3

**Input:**

```text
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
```

**Output:**

```text
4
```

**Explanation:**

The groups are `"a"` and `"bbbbbbbbbbbb"`.

After compression:

```text
["a","b","1","2"]
```

---

## Constraints

- `1 <= chars.length <= 2000`
- `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol.
- The algorithm must use `O(1)` extra space.

---

## Approach

Use two pointers:

- `read` scans the array and finds each group of consecutive identical characters.
- `write` tracks where the compressed result should be written.

For each group:

1. Store the current character.
2. Move `read` forward while the characters remain the same.
3. Count the number of occurrences.
4. Write the character at the `write` position.
5. If the count is greater than `1`, convert the count to a string and write each digit into the array.
6. Continue until all groups have been processed.

The compression is performed directly inside the input array, so no separate result array is required.

---

## Example Walkthrough

For:

```text
["a","a","b","b","c","c","c"]
```

Initially:

```text
read = 0
write = 0
```

The first group is `"aa"`.

After scanning the group:

```text
current = "a"
count = 2
```

Write the character and count:

```text
["a","2",...]
```

The next group is `"bb"`:

```text
["a","2","b","2",...]
```

The final group is `"ccc"`:

```text
["a","2","b","2","c","3",...]
```

The final value of `write` is `6`, so the method returns `6`.

---

## Complexity

Let `n` be the length of `chars`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` extra space

The array is modified in-place and only a constant number of variables are used.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
