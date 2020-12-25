def solution(nums, target):
    length = len(nums)
    if target < nums[0]:
        return 0
    if target > nums[length-1]:
        return length
    for i in range(1, length):
        if target == nums[i-1]:
            return i-1
        if target == nums[i] or nums[i - 1] < target < nums[i]:
            return i


if __name__ == "__main__":
    nums_list = [int(x) for x in input().split()]
    target_num = int(input())
    result = solution(nums_list, target_num)
    print(result)
