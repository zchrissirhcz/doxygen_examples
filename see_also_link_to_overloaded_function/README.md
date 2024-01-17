`@sa` 是 see also 的缩写，后面跟着一个函数名字。

如果跟着的函数名字有重载版本， 默认链接到第一个版本。

通过指明参数列表，可以获得正确的链接。

```c
void hello(const char* name);
void hello(const char* name, int n);

//
// @sa hello(const char*)
void world();

//
// @sa hello(const char*, int n)
void world2();
```