# 2. Add Two Numbers

**Difficulty:** Medium

**LeetCode:** [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

---

## Problem

You are given two **non-empty** linked lists representing two non-negative integers.

The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume that the numbers do not contain leading zeros, except for the number `0` itself.

---

## Examples

### Example 1

**Input:**

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output:**

```text
[7,0,8]
```

**Explanation:**

The linked lists represent:

```text
342 + 465 = 807
```

Because the digits are stored in reverse order:

```text
[2,4,3] → 342
[5,6,4] → 465
```

The result is:

```text
[7,0,8]
```

which represents `807`.

### Example 2

**Input:**

```text
l1 = [0]
l2 = [0]
```

**Output:**

```text
[0]
```

### Example 3

**Input:**

```text
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```

**Output:**

```text
[8,9,9,9,0,0,0,1]
```

---

## Constraints

* The linked lists are non-empty.
* Each node contains a single digit.
* The digits are stored in reverse order.
* The two numbers do not contain leading zeros, except for `0` itself.

---

## Approach

This solution adds the two linked lists **digit by digit**, just like normal addition.

A `carry` variable is used whenever the sum of two digits is `10` or greater.

The solution uses a **dummy node** to simplify construction of the result linked list.

### Step 1: Create the Result List

A dummy node is created:

```python
dummy = ListNode(0)
curr = dummy
```

The dummy node acts as the starting point of the result list.

The `curr` pointer is used to append new nodes.

The initial carry is:

```python
carry = 0
```

### Step 2: Process Both Lists

The loop continues while there is still a node in either list or there is a remaining carry:

```python
while l1 or l2 or carry:
```

This also handles cases where one linked list is shorter than the other.

### Step 3: Get the Current Digits

If a list has already reached its end, its value is treated as `0`:

```python
value1 = l1.val if l1 else 0
value2 = l2.val if l2 else 0
```

This allows lists of different lengths to be added without special handling.

### Step 4: Calculate the Sum

The current digits and the previous carry are added:

```python
total = value1 + value2 + carry
```

The new carry is calculated using integer division:

```python
carry = total // 10
```

The digit that belongs in the current result node is obtained using modulo:

```python
total % 10
```

A new node is then created:

```python
curr.next = ListNode(total % 10)
curr = curr.next
```

### Step 5: Move to the Next Nodes

After processing the current digits, the pointers are moved forward:

```python
if l1:
    l1 = l1.next

if l2:
    l2 = l2.next
```

If one list is shorter, its pointer simply stops while the other list continues.

---

## Example Walkthrough

For:

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

The calculation is:

```text
2 + 5 = 7
4 + 6 = 10 → digit = 0, carry = 1
3 + 4 + 1 = 8
```

So the result becomes:

```text
[7,0,8]
```

The linked list represents:

```text
807
```

which is the result of:

```text
342 + 465 = 807
```

---

## Handling Carry

The `carry` variable is important when a digit sum exceeds `9`.

For example:

```text
9 + 9 = 18
```

The result digit is:

```text
18 % 10 = 8
```

and the carry becomes:

```text
18 // 10 = 1
```

That carry is added to the next pair of digits.

---

## Why a Dummy Node?

The dummy node makes it easier to build the result list.

Instead of handling the first node separately, every result digit can be appended using:

```python
curr.next = ListNode(...)
curr = curr.next
```

At the end, the actual result starts at:

```python
dummy.next
```

Therefore, the solution returns:

```python
return dummy.next
```

---

## Complexity

Let `n` be the length of the longer linked list.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Each node is processed once, and the result linked list requires `O(n)` additional space.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
