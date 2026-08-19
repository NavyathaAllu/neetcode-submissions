class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=0
        nums.sort()
        for i in range(int(len(nums)-1)):
            if nums[i]==nums[i+1]:
                return True
        return False       
    

        