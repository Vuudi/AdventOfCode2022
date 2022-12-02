if __name__ == '__main__':
    totalScore = 0
    with open('input.txt', 'r') as strategyGuide:
        for line in strategyGuide:
            opponent = ord(line[0]) - 64
            you = ord(line[2]) - 87

            outcome = (you - opponent) % 3

            if outcome == 2:
                outcome = 0
            elif outcome == 1:
                outcome = 6
            else:
                outcome = 3

            totalScore += you + outcome

    print(totalScore)
