class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        if len(senate) < 2:
            return 'Dire' if senate[0] == 'D' else 'Radiant'

        n = len(senate)
        radient = deque()
        dire = deque()

        for i, char in enumerate(senate):
            if char == 'R':
                radient.append(i)
            else:
                dire.append(i)

        while radient and dire:
            r = radient.popleft()
            d = dire.popleft()

            if r < d:
                radient.append(r+n)
            else:
                dire.append(d+n)
        
        return 'Radiant' if radient else 'Dire'
