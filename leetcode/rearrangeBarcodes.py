class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        ans=[None]*len(barcodes)
        c=Counter(barcodes)
        c=sorted(c.items() ,key=lambda x:x[1],reverse=True)
        c=dict(c)
        k_even=0
        for key ,val in c.items():
            while val>0:
                if k_even>=len(barcodes):
                    k_even=1
                ans[k_even]=key
                k_even+=2
                val-=1
        return ans
