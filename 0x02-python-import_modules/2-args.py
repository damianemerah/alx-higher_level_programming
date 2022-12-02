#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('0 arguments.')
    elif len(sys.argv) > 1:
        print('{} argument{}:'.format(len(sys.argv) - 1,
                                      's' if (len(sys.argv) - 1) > 1 else ''))
        for i in range(len(sys.argv) - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
