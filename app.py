#!venv/bin/python
import sys
import os
from encrypter import encrypt_file as ef

def help():
    print("eu usage:")
    print("eu init - to initialize current directory as encrypt upload repository")
    print()

def call(arg, cb, key=False):
    index = 1
    if sys.argv[index] == arg :
        if key == True:
            print(sys.argv)
            key_val = input("Enter the key")
            cb(key_val, ",".join(sys.argv[index + 1: ]))
        else:
            cb(sys.argv[index + 1:])
        sys.exit(0)


def initializer():
    os.makedirs(".eu")

def check_if_eu_dir():
    return os.path.exists(".eu")

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

            call("encrypt", ef, key=True)

        else:
            sys.stderr.write("not a eu repository")
            sys.exit(1)


if __name__ == '__main__':
    myargs = args_decision_maker(sys.argv)
