# Title: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Date: 2025-07-29

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i

# Optional: Test the function
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(sol.twoSum([3, 3], 6))          # Output: [0, 1]

