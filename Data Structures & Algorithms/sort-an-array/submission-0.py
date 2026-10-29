def merge (left:List[int],right:List[int]) -> List[int]:

    result=[]

    l,r=0,0

    while l<len(left) and r<len(right):

        if (left[l]<=right[r]):
            result.append(left[l])
            l+=1
        else :
            result.append(right[r])
            r+=1
    result.extend(left[l:])
    result.extend(right[r:])

    return result

def sort(nums:List[int]):
        if len(nums)==1:
            return nums
        
        middle=0+len(nums)>>1

        left=sort(nums[0:middle])
        right=sort(nums[middle:])

        return merge(left,right)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sort(nums)