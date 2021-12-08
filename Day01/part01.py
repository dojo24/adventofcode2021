def partOne(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.readlines()))
    return countIncreases(nums, 1)


def countIncreases(nums: list[int], size: int) -> int:
    count = 0
    for i in range(len(nums) - size):
        if nums[i + size] > nums[i]:
            count += 1
    return count


if __name__ == "__main__":
    inputPath = "./puzzleInput.txt"
    print("---Part One---")
    print(partOne(inputPath))
