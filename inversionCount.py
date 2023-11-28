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
        self.seg[ind] = self.seg[left]+ self.seg[right]

    def query(self, ind, low, high, l, r):
        # No OverLap  -->[low,high]  [l,r] or [l,r] [low,high]
        if high < l or r < low:
            return 0

        elif low >= l and high <= r:
            return self.seg[ind]
        else:
            mid = (low+high)//2
            left = self.query((2*ind)+1, low, mid, l, r)
            right = self.query((2*ind)+2, mid+1, high, l, r)
            return left+ right

    def update(self, ind, low, high, i, val):
        if low == high:
            self.seg[ind] += val
            return
        mid = (low+high)//2
        left = (2 * ind) + 1
        right = (2 * ind) + 2
        if i <= mid:
            self.update(left, low, mid, i, val)
        else:
            self.update(right, mid+1, high, i, val)
        self.seg[ind] = self.seg[left]+self.seg[right]

if __name__ == '__main__':
    n=5
    arr=[2,3,8,6,1]
    maxi=-1
    for i in arr:
        maxi=max(maxi,i)
    maxi+=1
    freq=[0]*maxi
    for i in arr:
        freq[i]+=1
    st=SegmentTree(maxi)
    st.build(0,0,maxi-1,freq)
    cnt=0
    for i in range(n):
        freq[arr[i]]-=1
        st.update(0,0,maxi-1,arr[i],-1)
        cnt+=st.query(0,0,maxi-1,1,arr[i]-1)
    print(cnt)
