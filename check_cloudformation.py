import argparse
import re
import sys


def check_cloudformation(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Yaml filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        contents = open(filename).read()
        if re.search('Fn::Join', contents) or re.search('!Join', contents):
            print("Found usage of Join in '{}', please use !Sub instead.".format(filename))
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(check_cloudformation())
