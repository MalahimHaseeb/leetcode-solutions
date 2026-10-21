class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        if n < 1:
            return True

        visited = [False] * n
        visited[0] = True
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)

        return all(visited)
