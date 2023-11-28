class Info:
    def __init__(self, open, closed, full):
        self.open = open
        self.closed = closed
        self.full = full


class SegmentTree:
    def __init__(self, n):
        self.n = n
        node = Info(0, 0, 0)
        self.seg = [node]*((4*n)+1)

    def merge(self, left, right):
        res = Info(0, 0, 0)
        res.full = left.full + right.full + min(left.open, right.closed)
        res.open = left.open + right.open - min(left.open, right.closed)
        res.closed = left.closed + right.closed - min(left.open, right.closed)
        return res

    def build(self, ind, low, high, s):
        if low == high:
            temp = Info(0,0,0)
            if s[low] == ")":
                temp.closed += 1
            else:
                temp.open += 1
            self.seg[ind] = temp
            return
        mid = (low+high)//2
        left = (2*ind)+1
        right = (2*ind)+2
        self.build(left, low, mid, s)
        self.build(right, mid+1, high, s)
        self.seg[ind] = self.merge(self.seg[left], self.seg[right])

    def query(self, ind, low, high, l, r):
        if r < low or high < l:
            return Info(0, 0, 0)
        elif low >= l and high <= r:
            return self.seg[ind]
        else:
            mid = (low+high)//2
            left = self.query((2*ind)+1, low, mid, l, r)
            right = self.query((2*ind)+2, mid+1, high, l, r)
            return self.merge(left, right)


if __name__ == '__main__':
    s = "())(())(())("
    n = len(s)
    s1 = SegmentTree(n)
    s1.build(0, 0, n-1, s)
    queries = [(1,1),(2 ,3),(1, 2),(1 ,12),(8 ,12),(5 ,11),(2,10)]
    for i in queries:
        l, r = i[0],i[1]
        l -= 1
        r -= 1
        ans = s1.query(0, 0, n-1, l, r)
        print(2*ans.full)
