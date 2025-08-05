from typing import List

class Solution:

    def twoSum(self, num:List[int], tar:int)-> List[int]:
        for i in range(0, len(num)-1):
            for j in range(i+1, len(num)):
                if(num[i]+num[j]==tar):
                    return [i,j]
    
# creating an object of the class to call the method.
sol= Solution()

arr=[2,4,9,10,11,13,15]
tar=21
# n= len(arr) Total number of elements in an array
result= sol.twoSum(arr, tar)
print(f"The result indices are {result}")