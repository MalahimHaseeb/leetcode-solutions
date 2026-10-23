class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        if n < 1:
            return 0
        
        visited = [False] * n

        def dfs(city):
            visited[city] = True
            for nb in range(n):
                if isConnected[city][nb] == 1 and not visited[nb]:
                    dfs(nb)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        
        return provinces
