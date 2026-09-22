from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int,
                    queries: List[List[int]]) -> List[int]:

        n = len(nums)

        # tree[node] = [product % k, count of prefix products]
        tree = [[0] * (k + 1) for _ in range(4 * n)]

        def merge(left, right):
            # Product of whole segment
            prod = (left[0] * right[0]) % k

            # Count prefix products
            cnt = [0] * k

            # Prefixes completely inside left segment
            for r in range(k):
                cnt[r] += left[r + 1]

            # Prefixes that start in left and continue into right
            for r in range(k):
                new_rem = (left[0] * r) % k
                cnt[new_rem] += right[r + 1]

            return [prod] + cnt

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                tree[node][0] = rem
                tree[node][rem + 1] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, val):
            if l == r:
                rem = val % k

                tree[node] = [0] * (k + 1)
                tree[node][0] = rem
                tree[node][rem + 1] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Permanent update
            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            res = query(1, 0, n - 1, start, n - 1)

            # res[x + 1] = number of prefixes having remainder x
            ans.append(res[x + 1])

        return ans