class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        result=[]
        heap=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for key,value in count.items():
            heapq.heappush(heap,(-value,key))
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        return result

