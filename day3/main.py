if __name__ == '__main__':
    prioritySum = 0
    with open('input.txt', 'r') as rucksacks:
        # part 1
        # for rucksack in rucksacks:
        #     rucksack = rucksack.strip()
        #     firstCompartment = rucksack[0:len(rucksack) // 2]
        #     secondCompartment = rucksack[len(rucksack) // 2:len(rucksack)]
        #     for item in firstCompartment:
        #         if item in secondCompartment:
        #             priority = ord(item) - 64
        #
        #             if priority < 27:
        #                 priority += 26
        #             else:
        #                 priority -= 32
        #
        #             prioritySum += priority
        #             break

        i = 0
        commonItems = ''
        for rucksack in rucksacks:
            if i == 3:
                priority = ord(commonItems) - 64
                if priority < 27:
                    priority += 26
                else:
                    priority -= 32

                prioritySum += priority
                commonItems = ''
                i = 0

            rucksack = rucksack.strip()
            if commonItems == '':
                commonItems = ''.join(set(rucksack))
                i += 1
                continue

            for item in commonItems:
                if item not in rucksack:
                    commonItems = commonItems.replace(item, '')

            i += 1

        priority = ord(commonItems) - 64
        if priority < 27:
            priority += 26
        else:
            priority -= 32

        prioritySum += priority

        print(prioritySum)
