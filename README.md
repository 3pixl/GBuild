# GBuild
GBuild is a GUI application to build C/C++ apps with GCC easily without command-line trash.
## Benefits of GBuild
GBuild is made for non-experienced C/C++ programmers, so they can build their first apps with ease. Of course, they can
just install an IDE like Visual Studio or CodeBlocks, but IDEs are very heavy and big, while GBuild is small and
non-complex.

Okay, the benefits are:
- Easy-to-use
- Lightweight (source: 4,38 KB, built app: 10,5 MB (when building with PyInstaller))
- Open-source - this project is licensed with an MIT license, so you can edit source code how you want.

## How to use GBuild
Very easy, I answer you.<br>
To use this app, you first need a GNU compiler (GCC/G++). You can get it by using MinGW (the only environment I used).
Use MinGW docs to learn, how to install it.

After you installed compiler(s) you can use GBuild.
1. Run app.
2. Set a compiler path.
3. Set a path to the file you want to compile.
4. Set the output path.
5. Press _Compile_.

After file compiles, you'll get a message about compilation. I didn't make the message say "Compiled successfully" because I
don't know how to get state from other apps. But I'll learn it and I'll make sure the message will say "Success" or "Failure".
## Building
To build GBuild, you need **Python 3.9** and **PyInstaller** (`python -m pip install pyinstaller`).

After that, run this in folder with code:<br>
`pyinstaller -F -n GBuild --noconsole main.py`<br>
`-F` to bundle the app in one file;<br>
`-n GBuild` to name output file "GBuild";<br>
`--noconsole` to make app launch without console pop-up.

Congrats! You've built GBuild.
## Read this!
If you'll use my code for your app, then please credit me :)
