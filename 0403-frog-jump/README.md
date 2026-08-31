# 403. Frog Jump

**Difficulty:** Hard

**LeetCode:** [403. Frog Jump](https://leetcode.com/problems/frog-jump/)

---

## Problem

A frog is crossing a river. The river is divided into units, and some units contain stones.

The frog can only land on stones and must avoid the water.

Given a list of `stones` positions in ascending order, determine whether the frog can reach the last stone.

The frog starts on the first stone, and its first jump must be exactly `1` unit.

If the previous jump was `k` units, the next jump can be:

* `k - 1` units
* `k` units
* `k + 1` units

The frog can only jump forward.

---

## Examples

### Example 1

**Input:**

```text
stones = [0,1,3,5,6,8,12,17]
```

**Output:**

```text
true
```

**Explanation:**

The frog can cross the river using jumps:

```text
1 → 2 → 2 → 3 → 4 → 5
```

It eventually reaches the last stone.

### Example 2

**Input:**

```text
stones = [0,1,2,3,4,8,9,11]
```

**Output:**

```text
false
```

**Explanation:**

The frog cannot cross the gap between the stones at `4` and `8`.

---

## Constraints

* `2 <= stones.length <= 2000`
* `0 <= stones[i] <= 2^31 - 1`
* `stones[0] == 0`
* `stones` is sorted in strictly increasing order.

---

## Approach

This solution uses **Depth-First Search (DFS) with Memoization**.

The important part of the problem is that the frog's possible next jumps depend on the size of its previous jump.

Therefore, the state of the frog is represented by:

```text
(position, lastJump)
```

For example:

```text
(position = 8, lastJump = 3)
```

means that the frog is currently at position `8` and its previous jump was `3` units.

From this state, the frog can try:

```text
2, 3, 4
```

units.

---

## Step 1: Check the First Jump

The first jump must be exactly `1` unit.

```python
if stones[1] - stones[0] != 1:
    return False
```

If the second stone is not exactly one unit away, the frog can never make its required first jump.

---

## Step 2: Store Stones in a Set

The solution creates a set:

```python
stone_set = set(stones)
```

This allows the solution to quickly check whether a position contains a stone.

For example:

```python
if nextPos in stone_set:
```

This lookup takes approximately `O(1)` average time.

---

## Step 3: DFS State

The recursive function is:

```python
def canReach(position, lastJump):
```

It receives:

* `position` → the frog's current position
* `lastJump` → the distance of the previous jump

If the frog reaches the final stone:

```python
if position == target:
    return True
```

the crossing is successful.

---

## Step 4: Try the Three Possible Jumps

If the previous jump was `k`, the next jump can be:

```python
k - 1
k
k + 1
```

The solution checks all three:

```python
for jump in (lastJump - 1, lastJump, lastJump + 1):
```

Jumps of zero or less are ignored:

```python
if jump <= 0:
    continue
```

The next position is calculated as:

```python
nextPos = position + jump
```

If a stone exists at that position, DFS continues from there:

```python
if nextPos in stone_set:
    if canReach(nextPos, jump):
        ...
```

---

## Step 5: Memoization

Without memoization, the same `(position, lastJump)` state could be explored repeatedly.

The solution stores previously calculated states in:

```python
memo = {}
```

Before exploring a state:

```python
if (position, lastJump) in memo:
    return memo[(position, lastJump)]
```

If a state has already been calculated, its result is returned immediately.

When a successful path is found:

```python
memo[(position, lastJump)] = True
```

If no possible jump works:

```python
memo[(position, lastJump)] = False
```

This avoids repeatedly solving the same state.

---

## Example Walkthrough

For:

```text
stones = [0,1,3,5,6,8,12,17]
```

The first jump is:

```text
0 → 1
```

with a jump length of `1`.

From position `1`, the frog can try:

```text
0, 1, 2
```

The zero-length jump is ignored.

A valid path can continue:

```text
0 → 1 → 3 → 5 → 8 → 12 → 17
```

with jump lengths:

```text
1 → 2 → 2 → 3 → 4 → 5
```

The frog reaches the target, so the result is:

```text
true
```

---

## Why Memoization?

Consider a state such as:

```text
(position, lastJump)
```

There may be multiple paths that reach the same state.

Instead of exploring that state again, the solution remembers its result.

This changes the problem from repeatedly exploring the same paths into solving each reachable state once.

---

## Complexity

Let `n` be the number of stones.

There can be up to `O(n²)` possible `(position, lastJump)` states in the worst case.

Each state checks at most three possible jumps.

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n²)`

The `stone_set` provides constant-average-time stone lookups, while `memo` prevents repeated exploration of the same states.

---

## Solution

The implementation is available in [`solution.py`](solution.py).
