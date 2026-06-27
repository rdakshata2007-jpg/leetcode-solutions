class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        max=n/2
        for x in c:
            if c[x]>max:
                return(x)
                break
