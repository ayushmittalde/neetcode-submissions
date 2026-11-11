class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats=0
        people.sort()
        l=0
        r=len(people)-1

        while (l<r):
            target=people[l]+people[r]
            if target<=limit:
                boats+=1
                l+=1
                r-=1
            if target>limit:
                boats+=1
                r-=1
        
        if (l==r):
            boats+=1
        
        return boats