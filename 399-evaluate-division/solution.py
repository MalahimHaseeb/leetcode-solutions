class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]

            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}

            graph[a][b] = value
            graph[b][a] = 1 / value

        def find(current, target, visited):
            if current == target:
                return 1.0

            visited.add(current)

            for neighbour in graph[current]:
                if neighbour not in visited:
                    result = find(neighbour, target, visited)
                    if result != -1.0:
                        return result * graph[current][neighbour]

            return -1.0

        answers = []

        for c, d in queries:
            if c not in graph or d not in graph:
                answers.append(-1.0)
            else:
                answers.append(find(c, d, set()))

        return answers
        
