class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        n=len(nums)//2
        for key,value in count.items():
            if value>n:
                return key