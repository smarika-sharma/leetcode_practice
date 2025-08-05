from typing import List

class Solution:
    hash_map={}

    def twoSum(self, num:List[int], tar:int)-> List[int]:
        for i in range(0,len(num)):
            
            res=tar-num[i]
            if res in self.hash_map:
                return [self.hash_map[res], i]
            
            self.hash_map[num[i]]=i

# Creating an object of solution in order to use the funtion
sol= Solution()

arr= [5,4,4,5]
tar=10
result= sol.twoSum(arr, tar)
print(f"The result indices are {result}")