def partTwo(filename: str) -> int:
    with open(filename) as f:
        course = map(lambda line: line.strip().split(), f.readlines())

    hor, ver, aim = 0, 0, 0
    for step in course:
        direction, value = step[0], int(step[1])
        if direction == "forward":
            hor += value
            ver += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    return hor * ver


if __name__ == "__main__":
    inputPath = "./puzzleInput.txt"
    print("---Part Two---")
    print(partTwo(inputPath))
