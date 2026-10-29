class Solution:
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        LOG = max(1, (n - 1).bit_length())
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        it = [0] * n
        stack = [0]
        timer = 1
        tin[0] = 1
        while stack:
            u = stack[-1]
            if it[u] < len(g[u]):
                v = g[u][it[u]]
                it[u] += 1
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                timer += 1
                tin[v] = timer
                stack.append(v)
            else:
                tout[u] = timer
                stack.pop()

        up = [parent]
        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[v]] for v in range(n)])

        bit = [0] * (n + 2)

        def add(i, x):
            while i <= n + 1:
                bit[i] ^= x
                i += i & -i

        def get(i):
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            d = depth[u] - depth[v]
            for j in range(LOG):
                if (d >> j) & 1:
                    u = up[j][u]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]
            return up[0][u]

        cs = [ord(c) - 97 for c in s]
        for u in range(n):
            x = 1 << cs[u]
            add(tin[u], x)
            add(tout[u] + 1, x)

        res = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u = int(p[1])
                c = ord(p[2]) - 97
                if cs[u] != c:
                    x = (1 << cs[u]) ^ (1 << c)
                    add(tin[u], x)
                    add(tout[u] + 1, x)
                    cs[u] = c
            else:
                u = int(p[1])
                v = int(p[2])
                l = lca(u, v)
                m = get(tin[u]) ^ get(tin[v]) ^ (1 << cs[l])
                res.append((m & (m - 1)) == 0)
        return res