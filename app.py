#!/usr/bin/python
import sys
import os
import Utils
from initializer import App

app = App(os.getcwd())

def help():
    print("eu usage:")
    print("eu init - to initialize current directory as encrypt upload repository")
    print()

def call(command, other_args):
    getattr(app, command)(other_args)
    sys.exit(0)

def args_decision_maker(argv):
    opts = {}  # Empty dictionary to store key-value pairs.

    if len(argv) <= 1:
        help()
        return

    index = 1
    command = argv[index]
    if command == "init":
        getattr(app, command)()

    else:
        if app.check_if_eu_dir():
            other_args = argv[index + 1:]
            call(command, other_args)
        else:
            sys.stderr.write("not a eu repository")
            sys.exit(1)

if __name__ == '__main__':
    myargs = args_decision_maker(sys.argv)
