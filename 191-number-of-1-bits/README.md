# 191. Number of 1 Bits

**Difficulty:** Easy

**LeetCode:** [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

---

## Problem

Given a positive integer `n`, return the number of **set bits** (`1`s) in its binary representation.

This is also known as the **Hamming weight**.

---

## Examples

### Example 1

**Input:**

```text
n = 11
```

**Output:**

```text
3
```

The binary representation of `11` is:

```text
1011
```

There are three `1`s.

### Example 2

**Input:**

```text
n = 128
```

**Output:**

```text
1
```

The binary representation is:

```text
10000000
```

There is one `1`.

### Example 3

**Input:**

```text
n = 2147483645
```

**Output:**

```text
30
```

The binary representation contains thirty `1`s.

---

## Constraints

* `1 <= n <= 2^31 - 1`

---

## Approach

This solution checks the binary representation of `n` one bit at a time.

The bitwise operation:

```python
n & 1
```

checks the **last bit** of `n`.

* If the last bit is `1`, it adds `1` to the count.
* If the last bit is `0`, it adds `0`.

Then:

```python
n >>= 1
```

shifts all bits one position to the right.

For example, with:

```text
n = 11
```

Binary:

```text
1011
```

The process is:

```text
1011 → last bit 1 → count = 1
0101 → last bit 1 → count = 2
0010 → last bit 0 → count = 2
0001 → last bit 1 → count = 3
0000 → stop
```

The final answer is:

```text
3
```

---

## Complexity

Let `b` be the number of bits in `n`.

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

The algorithm processes each binary bit once and uses only a counter.

---

## Solution

The complete implementation is available in [`solution.py`](./solution.py).
