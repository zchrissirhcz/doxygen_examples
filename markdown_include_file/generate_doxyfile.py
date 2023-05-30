import os

class CodeWriter(object):
    def __init__(self, indent_len):
        self.lines = []
        self.indent_num = 0
        self.indent_len = indent_len

    def write(self, content):
        padding = (self.indent_len * self.indent_num) * ' '
        line = padding + content
        self.lines.append(line)

    def save(self, filename):
        with open(filename, 'w') as fout:
            for line in self.lines:
                fout.write(line + "\n")

    def tab(self):
        self.indent_num += 1

    def backspace(self):
        if (self.indent_num > 0):
            self.indent_num -= 1


def generate_doxyfile():
    w = CodeWriter(8)
    w.write('PROJECT_NAME = "x"')
    w.write('GENERATE_TREEVIEW = YES')
    w.write('GENERATE_HTML = YES')
    w.write('GENERATE_LATEX = NO')
    w.write('')
    w.write('EXTRACT_ALL = YES')
    w.write('EXTRACT_STATIC = YES')
    w.write('')
    w.write('INPUT = hello.h \\')
    w.tab()

    curDir = os.getcwd().replace('\\', '/')
    line = '{:s}/docs/root.md \\'.format(curDir)
    w.write(line)

    line = '{:s}/docs/changelog.md'.format(curDir)
    w.write(line)

    w.backspace()

    w.write('# cpp command, the C Pre Processor, works on Linux/MacOSX, but failed on Windows')
    line = '# FILTER_PATTERNS = {:s}/docs/changelog.md="cpp -P "'.format(curDir)
    w.write(line)

    w.write('# Implement an alternative of cpp with Python wors for Windows, Linux and MacOSX')
    line = 'FILTER_PATTERNS = {:s}/docs/changelog.md="python {:s}/sledcpp.py "'.format(curDir, curDir)
    w.write(line)

    w.save("Doxyfile")


if __name__ == '__main__':
    generate_doxyfile()