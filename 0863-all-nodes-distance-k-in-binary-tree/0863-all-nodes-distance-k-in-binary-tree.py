from collections import deque

class Solution:
    def distanceK(self, root, target, k):

    
        parent = {}

        def markParents(node, par=None):
            if not node:
                return

            parent[node] = par
            markParents(node.left, node)
            markParents(node.right, node)

        markParents(root)

        queue = deque([target])
        visited = set([target])

        distance = 0

        while queue:

            if distance == k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                node = queue.popleft()

                # Check left, right, and parent
                for neighbor in [node.left, node.right, parent[node]]:

                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            distance += 1

        return []