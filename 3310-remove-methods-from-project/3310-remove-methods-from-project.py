class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)
            rev[v].append(u)

        suspicious = [False] * n

        # Mark all methods reachable from k
        def dfs(node):
            suspicious[node] = True
            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        # If a non-suspicious method calls a suspicious one,
        # then we cannot remove any suspicious methods.
        for v in range(n):
            if suspicious[v]:
                for u in rev[v]:
                    if not suspicious[u]:
                        return list(range(n))

        # Otherwise remove all suspicious methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans