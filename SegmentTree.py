class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0]*((4*self.n)+1)

    def build(self, ind, low, high, arr):
        if low == high:
            self.seg[ind] = arr[low]
            return

        mid = (low+high)//2
        left = (2*ind)+1
        right = (2*ind)+2
        self.build(left, low, mid, arr)
        self.build(right, mid+1, high,  arr)
        self.seg[ind] = min(self.seg[left], self.seg[right])

    def query(self, ind, low, high, l, r):
        # No OverLap  -->[low,high]  [l,r] or [l,r] [low,high]
        if high < l or r < low:
            return 99999

        elif low >= l and high <= r:
            return self.seg[ind]
        else:
            mid = (low+high)//2
            left = self.query((2*ind)+1, low, mid, l, r)
            right = self.query((2*ind)+2, mid+1, high, l, r)
            return min(left, right)

    def update(self, ind, low, high, i, val):
        if low == high:
            self.seg[ind] = val
            return
        mid = (low+high)//2
        left = (2 * ind) + 1
        right = (2 * ind) + 2
        if i <= mid:
            self.update(left, low, mid, i, val)
        else:
            self.update(right, mid+1, high, i, val)
        self.seg[ind] = min(self.seg[left], self.seg[right])


if __name__ == '__main__':
    n1 = 6
    arr1 = [2, 1, 0, 4, 3, 7]
    sg1 = SegmentTree(n1)
    sg1.build(0, 0, n1-1, arr1)

    n2 = 5
    arr2 = [3, 12, 2, 0, 3]
    sg2 = SegmentTree(n2)
    sg2.build(0, 0, n2 - 1, arr2)

    query = int(input())
    res = []
    for _ in range(query):
        query_type = int(input())
        if query_type == 1:
            l1, r1, l2, r2 = map(int, input().split())
            mini1 = sg1.query(0, 0, n1 - 1, l1, r1)
            mini2 = sg2.query(0, 0, n2 - 1, l2, r2)
            res.append(min(mini1, mini2))
        else:
            arrNo, i, val = map(int, input().split())
            if arrNo == 1:
                sg1.update(0, 0, n1-1, i, val)
                arr1[i] = val
            else:
                sg2.update(0, 0, n2-1, i, val)
                arr2[i] = val
