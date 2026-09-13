# 211. Design Add and Search Words Data Structure

**Difficulty:** Medium

**LeetCode:** [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

---

## Problem

Design a data structure that supports two operations:

* `addWord(word)` → Adds a word to the data structure.
* `search(word)` → Checks whether a word exists that matches the given pattern.

The search pattern may contain `.`.

The `.` character can match **any single lowercase letter**.

---

## Examples

### Example 1

**Input:**

```text
["WordDictionary", "addWord", "addWord", "addWord",
 "search", "search", "search", "search"]

[[], ["bad"], ["dad"], ["mad"],
 ["pad"], ["bad"], [".ad"], ["b.."]]
```

**Output:**

```text
[null, null, null, null, false, true, true, true]
```

Explanation:

```text
addWord("bad")
addWord("dad")
addWord("mad")

search("pad") → false
search("bad") → true
search(".ad") → true
search("b..") → true
```

---

## Constraints

* `1 <= word.length <= 25`
* Words added contain lowercase English letters.
* Search words contain lowercase English letters or `.`.
* There will be at most `2` dots in a search query.
* At most `10^4` calls will be made to `addWord` and `search`.

---

## Approach

This solution uses a **Trie** to store the words.

The Trie is represented using nested Python dictionaries.

For example, adding:

```text
bad
```

creates a structure similar to:

```text
b
└── a
    └── d
```

A special key `$` is used to mark the **end of a complete word**.

### Adding a Word

For every character in the word:

1. Check whether the character already exists in the current node.
2. If it does not exist, create a new dictionary.
3. Move to that character's node.
4. Mark the end of the word using `$`.

---

### Searching a Word

For normal characters, we simply follow the corresponding Trie node.

For example:

```text
bad
```

follows:

```text
b → a → d
```

The interesting case is `.`.

For example:

```text
b..
```

After finding `b`, the first `.` can match any available child.

So we use **DFS (Depth-First Search)** to try each possible child.

Conceptually:

```text
b
├── a
│   └── d
├── e
│   └── ...
└── ...
```

If any possible path successfully matches the remaining characters, the search returns `True`.

---

## Example Walkthrough

Suppose the dictionary contains:

```text
bad
dad
mad
```

Searching:

```text
.ad
```

The first character is `.`.

It can match:

```text
b
d
m
```

The DFS tries the possible branches.

For the `b` branch:

```text
.ad
 ↓
bad
```

The remaining characters `ad` match, so the result is:

```text
True
```

Similarly:

```text
b..
```

can match:

```text
bad
```

because both `.` characters can represent `a` and `d`.

---

## Complexity

Let `L` be the length of the word.

### `addWord`

* **Time Complexity:** `O(L)`
* **Space Complexity:** `O(L)` for newly created Trie nodes.

### `search`

For a search without `.`:

* **Time Complexity:** `O(L)`

When `.` is present, DFS may explore multiple Trie branches.

In the worst case:

* **Time Complexity:** `O(26^L)`
* **Space Complexity:** `O(L)` for the DFS recursion.

In this problem, there are at most **2 dots**, which significantly limits the branching during searches.

---

## Solution

The complete implementation is available in [`solution.py`](./solution.py).
