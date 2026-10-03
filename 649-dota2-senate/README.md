# 649. Dota2 Senate

**Difficulty:** Medium

**LeetCode:** [649. Dota2 Senate](https://leetcode.com/problems/dota2-senate/)

---

## Problem

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of two rights:

- **Ban one senator's right:** A senator can make another senator lose all his rights in this and all the following rounds.
- **Announce the victory:** If this senator finds that the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string `senate` representing each senator's party, where `'R'` represents the Radiant party and `'D'` represents the Dire party, and the size of the string is `n` senators:

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce victory. The output should be `"Radiant"` or `"Dire"`.

---

## Examples

### Example 1

**Input:**

```text
senate = "RD"
```

**Output:**

```text
"Radiant"
```

**Explanation:**

The first senator comes from Radiant and he can just ban the next senator's right in round 1. The second senator can't exercise any rights anymore since his right has been banned. In round 2, the first senator can just announce the victory since he is the only one in the senate who can still vote.

---

### Example 2

**Input:**

```text
senate = "RDD"
```

**Output:**

```text
"Dire"
```

**Explanation:**

The first senator comes from Radiant and he can just ban the next senator's right in round 1. The second senator can't exercise any rights anymore since his right has been banned. The third senator comes from Dire and he can ban the first senator's right in round 1. In round 2, the third senator can just announce the victory since he is the only one in the senate who can still vote.

---

## Constraints

- `n == senate.length`
- `1 <= n <= 10^4`
- `senate[i]` is either `'R'` or `'D'`.

---

## Approach

Model this as a queue-based simulation using the indices of each party's senators:

- `radient` holds the indices of all `'R'` senators, in voting order.
- `dire` holds the indices of all `'D'` senators, in voting order.

The key idea: whenever an `'R'` senator and a `'D'` senator face off, the one whose turn comes first in the current round should ban the other, since banning early is always at least as good as waiting. So repeatedly compare the front of both queues:

1. Pop the front index from each queue, `r` from `radient` and `d` from `dire`.
2. Whichever index is smaller gets to act first in this round and bans the other. The surviving senator re-enters the voting order for the next round, which is modeled by pushing their index back onto their own queue as `index + n`. Adding `n` preserves relative order across rounds, since it places this senator after every currently-waiting senator from both parties but still before anyone who already got pushed back in an earlier round at an even higher value.
3. If `r < d`, the Radiant senator survives, so push `r + n` onto `radient`.
4. Otherwise, the Dire senator survives, so push `d + n` onto `dire`.

Continue until one queue is completely empty, meaning that party has no voters left. The party with senators remaining in their queue wins.

As a shortcut, if there's only one senator total, that senator's own party wins immediately without needing the simulation.

---

## Example Walkthrough

For:

```text
senate = "RDD"
```

`n = 3`. Build the initial queues from indices:

```text
radient = [0]
dire = [1, 2]
```

Round 1: pop `r = 0` and `d = 1`. `0 < 1`, so Radiant acts first and bans Dire's senator at index `1`. Radiant's senator survives and rejoins at `0 + 3 = 3`:

```text
radient = [3]
dire = [2]
```

Round 2: pop `r = 3` and `d = 2`. `3 > 2`, so Dire acts first and bans Radiant's senator at index `3`. Dire's senator survives and rejoins at `2 + 3 = 5`:

```text
radient = []
dire = [5]
```

`radient` is now empty, so the loop stops. The final result is `"Dire"`.

---

## Complexity

Let `n` be the length of `senate`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

Each senator is pushed back into a queue at most once per round survived, and every senator is eventually banned exactly once, so the total number of queue operations is bounded by `O(n)`.

---

## Solution

The implementation is available in [`solution.py`](./solution.py).
