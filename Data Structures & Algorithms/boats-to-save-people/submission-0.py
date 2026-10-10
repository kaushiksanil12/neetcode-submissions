class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        left=0
        right=len(people)-1
        people.sort()
        while left<=right :
            if people[right]+people[left]<=limit:
                left+=1
                right-=1
            else :
                right-=1
            count+=1
        return count