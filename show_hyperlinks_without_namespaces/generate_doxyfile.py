import os
from code_writer import CodeWriter

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
    w.write('changelog.h')

    w.backspace()

    w.save("Doxyfile")


if __name__ == '__main__':
    generate_doxyfile()