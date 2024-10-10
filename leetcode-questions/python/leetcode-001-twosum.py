from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            k = i
            for j in range(len(nums)-1):
                if nums[i] + nums[k+1] == target:
                    print(i, k+1)
                    return [i, k+1]
                
                else:
                    k = j + 1


# optimised solution at O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = {}
        for i in len(nums):
            num_dict[nums[i]] = i

        
        for i in len(nums):

            # get supp

            second_number = target - nums[i]

            if second_number in num_dict and nums[second_number] != i:

                return [i, num_dict[second_number]]
         



