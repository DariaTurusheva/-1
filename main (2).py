def solution(nums_list):
    len_counts = len(nums_list) + 1
    counts = [0] * len_counts
    for num in nums_list:
        counts[num] += 1
    mis_nums = []
    for i in range(1, len_counts):
        if counts[i] == 0:
            mis_nums.append(i)
    return mis_nums


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    result = solution(nums)
    print(result)
