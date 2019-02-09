import pytest
import module

def test_naive():
    nums = [2, 7, 11, 15]
    ans = module.TwoSum().naive(nums, 9)
    assert ans == [0, 1]

def test_naive2():
    nums = [3,2,4]
    ans = module.TwoSum().naive(nums, 6)
    assert ans == [1, 2]

def test_proposed():
    nums = [2, 7, 11, 15]
    ans = module.TwoSum().proposed(nums, 9)
    assert ans == [0, 1]

def test_proposed2():
    nums = [3,2,4]
    ans = module.TwoSum().proposed(nums, 6)
    assert ans == [1, 2]