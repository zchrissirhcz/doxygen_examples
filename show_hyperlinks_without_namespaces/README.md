生成 changelog 的 html 网页， 并让符号生成超链接， 符号（例如函数）刻意省略 namespace。

这个例子是不需要修改 doxygen 的源代码的解决方案。

思路是用 python 生成 changelog.h 这个 C++ 的头文件， 内容是把 changelog.md 内容作为 doxygen 注释。

https://github.com/doxygen/doxygen/issues/10102