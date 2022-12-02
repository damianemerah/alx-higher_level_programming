if __name__ == '__main__':
    import sys

    length = len(sys.argv) - 1
    arg_sum = 0

    for i in range(length):
        arg_sum = arg_sum + int(sys.argv[i + 1])
    print(arg_sum)
