nums = [x for x in range(int(input()), int(input()) + 1) if x % 3 == 0]
print(sum(nums) / len(nums))