from part01 import countIncreases

def partTwo(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.readlines()))
    return countIncreases(nums, 3)


if __name__ == "__main__":
    inputPath = "./puzzleInput.txt"
    print("---Part Two---")
    print(partTwo(inputPath))