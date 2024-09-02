class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            m = nums[i]
 
            perms = nums[:i] + nums[i+1:]
 
            for p in self.permute(perms):
                result.append([m] + p)

        return result
    
