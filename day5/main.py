if __name__ == '__main__':
    stacks = []
    with open('input.txt', 'r') as rearrangementProcedure:
        moves = False
        for line in rearrangementProcedure:
            line = line.rstrip()
            if line == '':
                for i in range(len(stacks)):
                    stacks[i].reverse()
                continue

            if not moves and any(char.isdigit() for char in line):
                moves = True
                continue

            if not moves:
                crates = []
                for i in range(1, len(line), 4):
                    crates.append(line[i])

                while len(crates) > len(stacks):
                    stacks.append([])

                for i in range(len(crates)):
                    if crates[i] != ' ':
                        stacks[i].append(crates[i])

                continue

            move = line.split(' ')
            stacks[int(move[5]) - 1].extend(stacks[int(move[3]) - 1][-int(move[1]):])
            del(stacks[int(move[3]) - 1][-int(move[1]):])
            # part 1
            #
            # while int(move[1]) > 0:
            #     stacks[int(move[5]) - 1].append(stacks[int(move[3]) - 1].pop())
            #     move[1] = str(int(move[1]) - 1)

    for stack in stacks:
        print(stack.pop(), end='')
