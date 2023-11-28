"""
arr=[1,4,2,1,3,1]
update (2-5)-->+5
lazy propagation will help to reduce Time Complexity
"""


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0] * ((4 * n) + 1)
        self.lazy = [0] * ((4 * n) + 1)

    def build(self, ind, low, high, arr):
        if low == high:
            self.seg[ind] = arr[low]
            return
        mid = (low + high) // 2
        left = (2 * ind) + 1
        right = (2 * ind) + 2
        self.build(left, low, mid, arr)
        self.build(right, mid + 1, high, arr)
        self.seg[ind] = min(self.seg[left], self.seg[right])

    def update(self, ind, low, high, l, r, val):
        """
        update the previous remaining updates and propogate downwards
        """
        left = (2 * ind) + 1
        right = (2 * ind) + 2
        if self.lazy[ind] != 0:
            self.seg[ind] += self.lazy[ind]
            if low != high:
                self.lazy[left] += self.lazy[ind]
                self.lazy[right] += self.lazy[ind]
            self.lazy[ind] = 0

        """
        complete Overlap OF InterVal Lies within the Range

        """
        if high < l or r < low:
            return

        if low >= l and high <= r:
            self.seg[ind] += val
            if low != high:
                self.lazy[left] += val
                self.lazy[right] += val
            return
        mid = (low + high) // 2
        self.update(left, low, mid, l, r, val)
        self.update(right, mid + 1, high, l, r, val)
        self.seg[ind] = min(self.seg[left], self.seg[right])

    def query(self, ind, low, high, l, r):
        left = (2 * ind) + 1
        right = (2 * ind) + 2
        if self.lazy[ind] != 0:
            self.seg[ind] += self.lazy[ind]
            if low != high:
                self.lazy[left] += self.lazy[ind]
                self.lazy[right] += self.lazy[ind]
            self.lazy[ind] = 0

        if high < l or r < low:
            return 99999

        if low >= l and high <= r:
            return self.seg[ind]

        mid = (low + high) // 2
        left_value = self.query(left, low, mid, l, r)
        right_value = self.query(right, mid + 1, high, l, r)
        return min(left_value, right_value)


if __name__ == '__main__':
    n = 5
    arr = [1, 2, 3, 4, 5]
    stree = SegmentTree(5)
    stree.build(0, 0, n - 1, arr)

    queries = [[1, 0, 4], [2, 1, 3, 2], [1, 0, 4]]
    for query in queries:
        type = query[0]
        if type == 1:
            l = query[1]
            r = query[2]
            ans = stree.query(0, 0, n - 1, l, r)
            print("answer", ans)

        else:
            l, r, value = query[1], query[2], query[3]
            stree.update(0, 0, n - 1, l, r, value)
