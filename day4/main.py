if __name__ == '__main__':
    totalOverlappingPairs = 0
    with open('input.txt', 'r') as assignments:
        for assignment in assignments:
            assignment = assignment.strip()
            pairs = assignment.split(',')
            sectionsOne = pairs[0].split('-')
            sectionsTwo = pairs[1].split('-')

            # part 1
            #
            # if ((int(sectionsOne[0]) <= int(sectionsTwo[0]) and int(sectionsOne[1]) >= int(sectionsTwo[1])) or
            #         (int(sectionsOne[0]) >= int(sectionsTwo[0]) and int(sectionsOne[1]) <= int(sectionsTwo[1]))):
            #     totalContainingPairs += 1

            start = int(sectionsOne[0]) if int(sectionsOne[0]) > int(sectionsTwo[0]) else int(sectionsTwo[0])
            end = int(sectionsOne[1]) if int(sectionsOne[1]) < int(sectionsTwo[1]) else int(sectionsTwo[1])

            totalOverlappingPairs += 1 if end - start >= 0 else 0

    print(totalOverlappingPairs)
