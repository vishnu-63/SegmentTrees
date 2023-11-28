class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0]*((4*self.n)+1)

    def build(self, ind, low, high, arr, orr):
        if low == high:
            self.seg[ind] = arr[low]
            return

        mid = (low+high)//2
        left = (2*ind)+1
        right = (2*ind)+2
        self.build(left, low, mid, arr, not orr)
        self.build(right, mid+1, high,  arr, not orr)
        if orr:
            self.seg[ind] = self.seg[left] | self.seg[right]
        else:
            self.seg[ind] = self.seg[left] ^ self.seg[right]

    def update(self, ind, low, high, i, val, orr):
        if low == high:
            self.seg[ind] = val
            return
        mid = (low+high)//2
        left = (2 * ind) + 1
        right = (2 * ind) + 2
        if i <= mid:
            self.update(left, low, mid, i, val, not orr)
        else:
            self.update(right, mid+1, high, i, val, not orr)
        if orr:
            self.seg[ind] = self.seg[left] | self.seg[right]
        else:
            self.seg[ind] = self.seg[left] ^ self.seg[right]


if __name__ == '__main__':
    n, q = map(int, input().split())
    ele = 2**n
    arr = list(map(int, input().split()))

    s1 = SegmentTree(ele)
    if n % 2 == 0:
        s1.build(0, 0, ele-1, arr, False)
    else:
        s1.build(0, 0, ele - 1, arr, True)
    for _ in range(q):
        i, val = map(int, input().split())
        i -= 1
        if n % 2 == 0:
            s1.update(0, 0, ele - 1, i, val, False)
        else:
            s1.update(0, 0, ele - 1, i, val, True)

        print("Result", s1.seg[0])
