class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) == 1:
            return True

        if stones[1] - stones[0] != 1:
            return False

        stone_set = set(stones)
        target = stones[-1]
        memo = {}

        def canReach(position, lastJump):
            if position == target:
                return True

            if (position, lastJump) in memo:
                return memo[(position, lastJump)]

            for jump in (lastJump - 1, lastJump, lastJump + 1):
                if jump <= 0:
                    continue
                nextPos = position + jump
                if nextPos in stone_set:
                    if canReach(nextPos, jump):
                        memo[(position, lastJump)] = True
                        return True

            memo[(position, lastJump)] = False
            return False

        return canReach(stones[1], 1)
