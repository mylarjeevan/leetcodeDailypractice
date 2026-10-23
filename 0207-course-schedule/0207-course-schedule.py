
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
