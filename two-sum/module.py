class TwoSum:
    def naive(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]

    def proposed(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        first_pass_set = {}
        for idx, num in enumerate(nums):
            first_pass_set[num] = idx
        
        for idx, num in enumerate(nums):
            differentiator = target - num
            if differentiator in first_pass_set:
                original_index = first_pass_set[differentiator]
                if (idx != original_index):
                    return [idx, original_index]