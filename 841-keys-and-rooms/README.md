# 841. Keys and Rooms

**Difficulty:** Medium

**LeetCode:** [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)

---

## Problem

There are `n` rooms labeled from `0` to `n - 1` and all the rooms are locked except for room `0`. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array `rooms` where `rooms[i]` is the set of keys that you can obtain if you visited room `i`, return `true` if you can visit all the rooms, or `false` otherwise.

---

## Examples

### Example 1

**Input:**

```text
rooms = [[1],[2],[3],[]]
```

**Output:**

```text
true
```

**Explanation:**

We visit room `0` and pick up key `1`.

We then visit room `1` and pick up key `2`.

We then visit room `2` and pick up key `3`.

We then visit room `3`.

Since we were able to visit every room, we return `true`.

---

### Example 2

**Input:**

```text
rooms = [[1,3],[3,0,1],[2],[0]]
```

**Output:**

```text
false
```

**Explanation:**

We can not enter room number `2` since the only key that unlocks it is in that room.

---

## Constraints

- `n == rooms.length`
- `2 <= n <= 1000`
- `0 <= rooms[i].length <= 1000`
- `1 <= sum(rooms[i].length) <= 3000`
- `0 <= rooms[i][j] < n`
- All the values of `rooms[i]` are unique.

---

## Approach

Treat the rooms as a graph where each key is an edge from the room it is found in to the room it opens, then check whether every node is reachable from room `0`. An iterative DFS with a stack does the job:

- `visited` is a list of booleans, one per room, marking rooms we have already unlocked.
- `stack` holds rooms we have entered but have not yet collected keys from.

Start by marking room `0` as visited and pushing it onto the stack, since it is the only room that begins unlocked.

While the stack is not empty:

1. Pop a `room` off the stack.
2. Go through every `key` found in `rooms[room]`.
3. If `visited[key]` is `False`, that room is newly unlocked. Mark it visited and push it onto the stack so its keys get collected later.

Marking a room as visited at the moment it is pushed, rather than when it is popped, makes sure no room is ever added to the stack twice.

When the stack runs out, every reachable room has been visited. Return `all(visited)`, which is `True` only if no room was left locked.

An empty `rooms` list is treated as trivially `True`.

---

## Example Walkthrough

For:

```text
rooms = [[1,3],[3,0,1],[2],[0]]
```

Start with:

```text
visited = [True, False, False, False]
stack = [0]
```

Pop room `0`. Its keys are `1` and `3`. Both rooms are locked, so unlock and push them:

```text
visited = [True, True, False, True]
stack = [1, 3]
```

Pop room `3`. Its only key is `0`, which is already visited, so nothing changes:

```text
visited = [True, True, False, True]
stack = [1]
```

Pop room `1`. Its keys are `3`, `0` and `1`, all already visited, so nothing changes:

```text
visited = [True, True, False, True]
stack = []
```

The stack is empty. Room `2` is still `False`, because the only key to it sits inside room `2` itself. `all(visited)` is `False`, so the final result is `false`.

---

## Complexity

Let `n` be the number of rooms and `k` be the total number of keys across all rooms.

- **Time Complexity:** `O(n + k)`
- **Space Complexity:** `O(n)`

Each room is pushed onto the stack at most once, and each key is looked at exactly once when its room is popped. The `visited` list and the stack each hold at most `n` entries.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
