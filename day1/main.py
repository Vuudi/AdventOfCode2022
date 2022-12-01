if __name__ == '__main__':
    elfCount = 1
    maxElf = 0
    maxCalorieSum = -1
    currentCalorieSum = 0

    with open('input.txt', 'r') as calorieList:
        for line in calorieList:
            line = line.strip()

            if line == '':
                if maxElf == 0 or currentCalorieSum > maxCalorieSum:
                    maxElf = elfCount
                    maxCalorieSum = currentCalorieSum
                elfCount += 1
                currentCalorieSum = 0
                continue

            currentCalorieSum += int(line)

    if maxElf == 0 or currentCalorieSum > maxCalorieSum:
        maxElf = elfCount

    print(maxCalorieSum)
