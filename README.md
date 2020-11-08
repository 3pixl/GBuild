# GBuild
GBuild is a GUI application to build C/C++ apps with GCC easily without command-line trash.

Note: arguments are not working now, in further commits they will work.
## Benefits of GBuild
GBuild is made for non-experienced C/C++ programmers, so they can build their first apps with ease. Of course, they can
just install an IDE like Visual Studio or CodeBlocks, but IDEs are very heavy and big, while GBuild is small and
non-complex

Okay, the benefits are:
- Easy-to-use
- Lightweight (source: 4,38 KB, built app: 10,5 MB (when building with PyInstaller))
- Open-source - this project licensed with MIT license, so you can edit source code how you want.

## How to use GBuild
Very easy, I answer you.<br>
To use this app, you first need a GNU compiler (gcc/g++). You can get it by using MinGW (the only environment I used).
Use MinGW docs to learn, how to install it.

After you installed compiler(s) you can use GBuild.
1. Run app.
2. Set compiler path.
3. Set path to file you want to compile.
4. Set the output path.
5. Press _Compile_.

After file compiles, you'll get message about compilation. I didn't made message say "Compiled succesfully", because I
don't really know how to get state of other app. But I'll learn it and in third (or maybe second) commit I'll make sure
message will say "Success" or "Failure".
## Building
To build GBuild, you need **Python 3.9** and **PyInstaller** (`python -m pip install pyinstaller`).

After that, run this in folder with code:<br>
`pyinstaller -F -n GBuild --noconsole main.py`<br>
`-F` to bundle the app in one file;
`-n GBuild` to name output file "GBuild"
`--noconsole` to make app launch without console pop-up

Congrats! you've built GBuild.
## Read this!
If you'll use my code for your own app, then please credit me :)