# 735. Asteroid Collision

**Difficulty:** Medium

**LeetCode:** [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

---

## Problem

We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

---

## Examples

### Example 1

**Input:**

```text
asteroids = [5,10,-5]
```

**Output:**

```text
[5,10]
```

**Explanation:**

The `10` and `-5` collide resulting in `10`. The `5` and `10` never collide.

---

### Example 2

**Input:**

```text
asteroids = [8,-8]
```

**Output:**

```text
[]
```

**Explanation:**

The `8` and `-8` collide exploding each other.

---

### Example 3

**Input:**

```text
asteroids = [10,2,-5]
```

**Output:**

```text
[10]
```

**Explanation:**

The `2` and `-5` collide resulting in `-5`. The `10` and `-5` collide resulting in `10`.

---

### Example 4

**Input:**

```text
asteroids = [3,5,-6,2,-1,4]
```

**Output:**

```text
[-6,2,4]
```

**Explanation:**

The asteroid `-6` makes the asteroids `3` and `5` explode, and then continues going left. On the other side, the asteroid `2` destroys `-1`. Since `2` and `4` are both moving right, they never collide.

---

## Constraints

- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

---

## Approach

Use a stack to represent the asteroids that have survived so far, moving left to right through the input:

- A right-moving asteroid (positive) can only ever collide with a left-moving asteroid (negative) that comes after it, so pushing right-movers onto the stack and resolving collisions only when a left-mover shows up handles every case correctly.
- Two asteroids moving in the same direction never collide, so an asteroid never needs to be compared against same-direction neighbors.

For each `val` in `asteroids`, use a flag `should_keep` to track whether `val` survives its collisions:

1. While the stack is non-empty, the top of the stack is moving right (`stack[-1] > 0`), and `val` is moving left (`val < 0`), a collision happens. Compare sizes:
   - If they're equal in size (`top == -val`), both explode. Pop the stack and mark `val` as not kept.
   - If the stack's top is bigger (`top > -val`), the top survives and `val` explodes. Mark `val` as not kept, leave the stack untouched, and stop checking further.
   - Otherwise, the top is smaller, so it explodes. Pop it and keep checking against the next item on the stack, since `val` might also collide with that one.
2. After the loop, if `val` is still marked as kept, push it onto the stack. This covers right-movers (which never enter the collision loop) and left-movers that survived every collision they were in.

At the end, the stack holds the asteroids that remain, in their original left-to-right order.

---

## Example Walkthrough

For:

```text
asteroids = [3,5,-6,2,-1,4]
```

Start with `stack = []`.

Process `3`, moving right, no collision possible. Push it:

```text
stack = [3]
```

Process `5`, moving right. Push it:

```text
stack = [3, 5]
```

Process `-6`, moving left. Top of stack is `5`, moving right, so they collide. `5 < 6`, so `5` explodes. Pop it:

```text
stack = [3]
```

Still colliding: top is `3`, moving right. `3 < 6`, so `3` explodes. Pop it:

```text
stack = []
```

Stack is now empty, so the loop stops. `-6` survives. Push it:

```text
stack = [-6]
```

Process `2`, moving right. Push it:

```text
stack = [-6, 2]
```

Process `-1`, moving left. Top of stack is `2`, moving right, so they collide. `2 > 1`, so `2` survives and `-1` explodes. Stack unchanged:

```text
stack = [-6, 2]
```

Process `4`, moving right. Push it:

```text
stack = [-6, 2, 4]
```

The final result is `[-6, 2, 4]`.

---

## Complexity

Let `n` be the length of `asteroids`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

Each asteroid is pushed onto the stack at most once and popped at most once, so the total work across all collisions is linear, and the stack holds up to `n` asteroids.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
