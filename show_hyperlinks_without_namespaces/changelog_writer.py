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

if __name__ == '__main__':
    w = CodeWriter(4)

    # write header
    w.write('namespace xx')
    w.write('{')
    w.write('')
    w.write('/** @page changelog Changelog')

    fin = open('CHANGELOG.md')
    for line in fin.readlines():
        w.write(line)
    fin.close()

    # write footer
    w.write('*/')
    w.write('')
    w.write('}')

    w.save('changelog.h')
