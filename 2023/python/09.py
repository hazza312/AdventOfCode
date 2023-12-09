import sys


def differences(nums):
    return [b - a for a, b in zip(nums, nums[1:])]


def all_zero(nums):
    return all(n == 0 for n in nums)


def predict_after(nums):
    return 0 if all_zero(nums) else nums[-1] + predict_after(differences(nums))


def predict_before(nums):
    return 0 if all_zero(nums) else nums[0] - predict_before(differences(nums))


if __name__ == '__main__':
    after_sum = 0
    before_sum = 0

    for line in sys.stdin:
        nums = [int(n) for n in line.split()]
        after_sum += predict_after(nums)
        before_sum += predict_before(nums)

    print(after_sum)
    print(before_sum)
