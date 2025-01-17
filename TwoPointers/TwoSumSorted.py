class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            product = numbers[left] + numbers[right]

            if product == target:
                return [left + 1, right + 1]
            elif product > target:
                right -= 1
            else:
                left += 1
        