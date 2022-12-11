def sum_dir(filesystem, directory_name):
    directory = filesystem[directory_name]
    size = 0
    for name in directory:
        if directory[name] == 'dir':
            size += sum_dir(filesystem, name)
        else:
            size += int(directory[name])
    return size


if __name__ == '__main__':
    filesystem = {}
    with open('input.txt', 'r') as terminalOutput:
        currentDir = ''
        ls = False
        for line in terminalOutput:
            line = line.strip()

            if line == '$ cd ..':
                currentDir = currentDir[:currentDir.rfind('/')]
                continue

            if line.startswith('$ cd '):
                ls = False
                if line[5] == '/':
                    currentDir = line[5:]
                else:
                    currentDir += '/' + line[5:]
                filesystem[currentDir] = {}
                continue

            if line == '$ ls':
                ls = True
                continue

            if ls:
                parts = line.split(' ')
                filesystem[currentDir][currentDir + '/' + parts[1]] = parts[0]

    # part 1
    # totalSize = 0
    # for directoryName in filesystem:
    #     size = sum_dir(filesystem, directoryName)
    #     if size <= 100000:
    #         totalSize += size
    #
    # print(totalSize)

    directorySizes = {}
    for directoryName in filesystem:
        size = sum_dir(filesystem, directoryName)
        directorySizes[directoryName] = size

    freeSpace = 70000000 - directorySizes['/']
    neededSpace = 30000000 - freeSpace

    sortedDirectories = sorted(directorySizes.items(), key=lambda item: item[1])
    for directoryName, size in sortedDirectories:
        if size > neededSpace:
            print(size)
            break
