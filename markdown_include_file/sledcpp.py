# sledcpp:  a naive C Pre-Processor implementation
# Author:   Zhuo Zhang <imzhuo#foxmail.com>
#
# Currently only support expanding `#include` directive once
# Used in generating doxygen webpages from markdown files which include another file
#
# Created:  2023-05-30 10:38:29
# Modified: 2023-05-30 10:38:48

import sys
import os

def getLinesOfTextFile(filepath):
    lines = []
    with open(filepath, encoding='utf-8') as fin:
        for line in fin.readlines():
            lines.append(line.strip())
    return lines


def expand_file_once(filepath):
    fileDir = os.path.dirname(filepath)
    with open(filepath) as fin:
        for line in fin.readlines():
            line = line.strip()
            if line.startswith('#include'):
                startPos = len('#include')
                depfile = line[startPos:].strip().split('"')[1]
                deppath = os.path.join(fileDir, depfile)
                deplines = getLinesOfTextFile(deppath)
                for item in deplines:
                    print(item)
            else:
                print(line)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python {:s} filepath'.format(sys.argv[0]))
        exit(1)
    
    filepath = sys.argv[1]
    expand_file_once(filepath)
