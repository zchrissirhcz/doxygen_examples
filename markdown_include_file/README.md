## Purpose
Demonstrate including a markdown file in another markdown file, via the C preprocessor.

Actually it works on Linux, but failed on Windows, gives warning when executing doxygen:
```
C:/Users/zz/dbg/a/docs/changelog.md:5: warning: explicit link request to 'include' could not be resolved
```

I think the problem is, how to correctly call Visual Studio's cl.exe for preprocessing markdown file's `#include xxx`.

## Run
```batch
python generate_doxyfile.py
doxygen
cd html
python -m http.server 7080
```