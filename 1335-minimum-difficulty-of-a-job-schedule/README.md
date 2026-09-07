# 1335. Minimum Difficulty of a Job Schedule

**Difficulty:** Hard

**LeetCode:** [1335. Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)

---

## Problem

You are given a list of jobs that must be completed in order over `d` days.

Each day must contain at least one job, and the difficulty of a day is the **maximum difficulty** of any job completed that day.

The total schedule difficulty is the sum of the maximum difficulty of each day.

Return the **minimum possible schedule difficulty**.

If it is impossible to schedule all jobs across `d` days, return `-1`.

---

## Examples

### Example 1

**Input:**

```text
jobDifficulty = [6,5,4,3,2,1]
d = 2
```

**Output:**

```text
7
```

One optimal schedule is:

```text
Day 1: [6,5,4,3,2] → difficulty = 6
Day 2: [1]          → difficulty = 1
```

Total:

```text
6 + 1 = 7
```

### Example 2

**Input:**

```text
jobDifficulty = [9,9,9]
d = 4
```

**Output:**

```text
-1
```

There are only 3 jobs but 4 days, so it is impossible to complete at least one job every day.

### Example 3

**Input:**

```text
jobDifficulty = [1,1,1]
d = 3
```

**Output:**

```text
3
```

Each day contains one job:

```text
Day 1: [1]
Day 2: [1]
Day 3: [1]
```

Total:

```text
1 + 1 + 1 = 3
```

---

## Constraints

* `1 <= jobDifficulty.length <= 300`
* `0 <= jobDifficulty[i] <= 1000`
* `1 <= d <= 10`

---

## Approach

This solution uses **Dynamic Programming with Memoization**.

At each position, we decide how many jobs should be completed on the current day.

The state is:

```text
dp(i, days)
```

where:

* `i` is the index of the next job we need to schedule.
* `days` is the number of days remaining.

For the current day, we try different ending positions for the jobs.

While extending the current day's jobs, we keep track of the maximum difficulty:

```text
mx = max(mx, jobDifficulty[j])
```

Then we calculate:

```text
current day's difficulty + minimum difficulty of remaining jobs
```

We take the minimum among all possible divisions.

When only one day remains, all remaining jobs must be completed that day, so the answer is simply:

```python
max(jobDifficulty[i:])
```

`@lru_cache(None)` stores previously calculated states so that the same state does not need to be solved again.

---

## Complexity

Let `n` be the number of jobs.

* **Time Complexity:** `O(n² × d)`
* **Space Complexity:** `O(n × d)`

The memoization stores at most `n × d` states, and each state may examine up to `n` possible job divisions.

---

## Solution

The complete implementation is available in [`solution.py`](./solution.py).
