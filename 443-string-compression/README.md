# 443. String Compression

**Difficulty:** Medium

**LeetCode:** [443. String Compression](https://leetcode.com/problems/string-compression/)

---

## Problem

Given an array of characters `chars`, compress it using the following algorithm.

For each group of consecutive repeating characters:

- If the group's length is `1`, keep only the character.
- Otherwise, write the character followed by the group's count.
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
