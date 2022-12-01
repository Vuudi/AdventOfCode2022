if __name__ == '__main__':
    elves = []
    i = 0
    currentSum = 0
    with open('input.txt', 'r') as calorieList:
        for line in calorieList:
            line = line.strip()

            if line == '':
                elves.append(currentSum)
                i += 1
                currentSum = 0
                continue

            currentSum += int(line)

    elves.append(currentSum)
    elves.sort()

    # part 1
    # print(sum(elves[-1:]))
    print(sum(elves[-3:]))
