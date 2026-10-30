from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        original = set()
        graph = defaultdict(list)

        for a,b in connections:
            original.add((a,b))
            graph[a].append(b)
            graph[b].append(a)

        
        stack = [(0,-1)]
        changes = 0

        while stack:
            city, parent  = stack.pop()

            for neighbor in graph[city]:
                if neighbor != parent:
                    if (city, neighbor) in original:
                        changes +=1
                    stack.append((neighbor, city))
            
        
        return changes
