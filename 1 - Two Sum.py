class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        // 66ms beats 59.42%
        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in numMap:
                return [i, numMap[complement]]
            
            numMap[nums[i]] = i 
