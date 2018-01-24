#!venv/bin/python
import sys
import os

def help():
    print("eu usage:")
    print("eu init - to initialize current directory as encrypt upload repository")
    print()

def initializer():
    os.makedirs(".eu")

def check_if_eu_dir():
    return os._exists(".eu")

def args_decision_maker(argv):
    opts = {}  # Empty dictionary to store key-value pairs.

    if len(argv) <= 1:
        help()
        return

    index = 1
    if argv[index] == "init":
        initializer()
    else:
        if check_if_eu_dir():
            pass
        else:
            sys.stderr.write("not a eu repository")
            sys.exit(1)


if __name__ == '__main__':
    myargs = args_decision_maker(sys.argv)
