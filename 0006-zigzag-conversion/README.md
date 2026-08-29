# 6. Zigzag Conversion

**Difficulty:** Medium

**LeetCode:** [6. Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)

---

## Problem

Given a string `s` and an integer `numRows`, arrange the characters of the string in a **zigzag pattern** across the given number of rows.

After arranging the characters, read the rows from top to bottom and return the resulting string.

For example, with:

```text id="x1m2pz"
s = "PAYPALISHIRING"
numRows = 3
```

The characters are arranged as:

```text id="d2r7yk"
P   A   H   N
A P L S I I G
Y   I   R
```

Reading row by row produces:

```text id="m0zq4f"
"PAHNAPLSIIGYIR"
```

---

## Examples

### Example 1

**Input:**

```text id="j0uj1n"
s = "PAYPALISHIRING"
numRows = 3
```

**Output:**

```text id="w2yq5r"
"PAHNAPLSIIGYIR"
```

### Example 2

**Input:**

```text id="v4m7dq"
s = "PAYPALISHIRING"
numRows = 4
```

**Output:**

```text id="p8b4qa"
"PINALSIGYAHRPI"
```

The zigzag pattern is:

```text id="w7u9cv"
P     I    N
A   L S  I G
Y A   H R
P     I
```

### Example 3

**Input:**

```text id="h5j2mz"
s = "A"
numRows = 1
```

**Output:**

```text id="s3n8xe"
"A"
```

---

## Constraints

* `1 <= s.length <= 1000`
* `s` consists of English letters, `','` and `'.'`.
* `1 <= numRows <= 1000`

---

## Approach

This solution simulates the zigzag movement using a list of strings, where each string represents one row.

### Step 1: Handle Special Cases

If there is only one row, there is no zigzag pattern to create.

Similarly, if the number of rows is greater than the length of the string, the string cannot form additional rows.

Therefore, the original string is returned:

```python id="h1j4zx"
if numRows == 1 or numRows > len(s):
    return s
```

### Step 2: Create the Rows

A list of empty strings is created to represent the rows:

```python id="f8m2kc"
rows = [""] * numRows
```

For example, with `numRows = 3`:

```text id="w5y7pv"
rows = ["", "", ""]
```

### Step 3: Track the Current Row

The solution starts from the first row:

```python id="j8p3dx"
curr_row = 0
```

A `direction` variable controls whether the characters are moving **down** or **up**:

```python id="q6v4bs"
direction = 1
```

A value of:

* `1` means move downward.
* `-1` means move upward.

### Step 4: Place Each Character

Each character is added to the current row:

```python id="e3r9km"
rows[curr_row] += ch
```

When the top row is reached, the direction changes downward:

```python id="b5q1ws"
if curr_row == 0:
    direction = 1
```

When the bottom row is reached, the direction changes upward:

```python id="k7n4az"
elif curr_row == numRows - 1:
    direction = -1
```

The current row is then updated:

```python id="c2x8hp"
curr_row += direction
```

This creates the zigzag movement:

```text id="q4y8nt"
0
↓
1
↓
2
↑
1
↑
0
↓
1
↓
2
```

### Step 5: Combine the Rows

After all characters have been placed, the rows are joined together:

```python id="m6r2vc"
return "".join(rows)
```

For example:

```text id="n9w5ks"
rows = [
    "PAHN",
    "APLSIIG",
    "YIR"
]
```

Joining them produces:

```text id="x7c3bd"
"PAHNAPLSIIGYIR"
```

---

## Complexity

Let `n` be the length of the string.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Each character is processed once, and all characters are stored in the row strings before they are joined.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
