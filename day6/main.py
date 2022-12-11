if __name__ == '__main__':
    # part 1
    # n = 4
    n = 14
    with open('input.txt', 'r') as dataStream:
        buffer = dataStream.read()
        for i in range(n, len(buffer)):
            window = buffer[i - n:i]
            x = list(set(window))
            y = list(window)
            x.sort()
            y.sort()
            if x == y:
                print(i)
                break

