def partOne(filename: str) -> int:
    with open(filename) as f:
        course = map(lambda line: line.strip().split(), f.readlines())

    hor, ver = 0, 0
    for step in course:
        direction, value = step[0], int(step[1])
        if direction == "forward":
            hor += value
        elif direction == "down":
            ver += value
        elif direction == "up":
            ver -= value
    return hor * ver





if __name__ == "__main__":
    inputPath = "./puzzleInput.txt"
    print("---Part One---")
    print(partOne(inputPath))