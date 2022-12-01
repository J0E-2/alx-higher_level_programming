#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    length = len(sys.argv)
    if len(sys.argv[1:]) == 0:
        print("0 arguments.")
    elif len(sys.argv[1:]) == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv[1:])))

    for w in range(1, length):
        print("{}: {}".format(w, sys.argv[w]))
