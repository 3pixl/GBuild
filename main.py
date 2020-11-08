from tkinter import *
from tkinter import messagebox
import os  # Used for console
import sys
from tkinter import filedialog as fd, StringVar
from config import *  # Version, author etc.

# Vars init
compilerPath: str = "none"
filePath: str = "none"
outputPath: str = "none"


# Windows
def licenseWindow():
    licenseW = Tk()
    licenseW.title("GBuild v" + version + " | License")
    #about.geometry("")
    text = Label(licenseW, text="""MIT License

Copyright (c) 2020 Mykola Malyovaniy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")
    text.pack(side="left", anchor=N)
    licenseW.mainloop()


def aboutWindow():
    about = Tk()
    about.title("GBuild v" + version + " | About")
    about.geometry("300x100")
    about.resizable(0, 0)
    textFrame = Frame(about)
    textFrame.pack(side="top", anchor=N)
    aboutLabel = Label(textFrame, text="GBuild - GCC GUI to build C/C++ programs. ")
    aboutLabel.pack(side="top", anchor=N)
    aboutButtonsFrame = Frame(about, padx="5", pady="2")
    aboutButtonsFrame.pack(side="bottom", anchor=S)
    licenseButton = Button(aboutButtonsFrame, width=10, text="License", command=licenseWindow)
    licenseButton.pack(side="left", anchor=SW)
    creditLabel = Label(aboutButtonsFrame, text="Copyright (c) 2020 Mykola Malyovaniy")
    creditLabel.pack(side="right", anchor=SE)
    about.mainloop()


# Functions
def chooseCompiler():  # Calls file dialog and saves to ccevar
    global compilerPath
    compilerPath = fd.askopenfilename(filetypes=(("GNU C Compiler", "gcc.exe"),
                                                 ("GNU C++ Compiler", "g++.exe"),
                                                 ("All files (Linux)", "*.*")))


def chooseFile():  # Same as chooseCompiler but saves to cfevar
    global filePath
    filePath = fd.askopenfilename(filetypes=(("C source code", "*.c"),
                                             ("C++ source code", ("*.cpp", "*.cc", "*.C", "*.cxx", "*.c++")),
                                             ("All files", "*.*")))


def chooseOutputFolder():
    global outputPath
    outputPath = fd.askdirectory()


def compileFile():  # Compiles file
    os.system(compilerPath + " " + filePath + " -o " + outputPath + "/app")
    messagebox.showinfo(title="Compilation info", message="Compiled!\nCheck " + outputPath + "/ for your file.")


root = Tk()  # Window create
# Window Initialization
root.title("GBuild v" + version)  # Window title
root.geometry("245x300")  # Window resolution
root.resizable(0, 0)  # Set no resizing window
# Window init end

# Compiler choose frame
compilerChooseFrame = Frame(root)
compilerChooseFrame.pack(side="top", anchor=W, padx="5", pady="2")
chooseCompilerLabel = Label(compilerChooseFrame, text="Path to GCC/G++ compiler:")
chooseCompilerLabel.pack(side="left")
chooseCompilerDialog = Button(compilerChooseFrame, width="10", text="Select", command=chooseCompiler)
chooseCompilerDialog.pack(side="left")
# End compiler choose frame

# File to compile frame
fileChooseFrame = Frame(root)
fileChooseFrame.pack(side="top", anchor=W, padx="5", pady="2")
chooseFileLabel = Label(fileChooseFrame, text="File to compile:")
chooseFileLabel.pack(side="left")
chooseFileDialog = Button(fileChooseFrame, width="10", text="Select", command=chooseFile)
chooseFileDialog.pack(side="left")
# End file to compile frame

# Output folder frame
outputFolderFrame = Frame(root)
outputFolderFrame.pack(side="top", anchor=W, padx="5", pady="2")
outputFolderLabel = Label(outputFolderFrame, text="Output folder: ")
outputFolderLabel.pack(side="left")
chooseFolderDialog = Button(outputFolderFrame, width="10", text="Select", command=chooseOutputFolder)
chooseFolderDialog.pack(side="left")
# End output folder frame

# Arguments frame
argsFrame = Frame(root)
argsFrame.pack(side="top", anchor=W, padx="5", pady="2")
argsLabel = Label(argsFrame, text="Arguments:")
argsLabel.pack(side="left")
argsEntry = Entry(argsFrame, width="27")
argsEntry.pack(side="left")
# End arguments frame

# TODO: Info frame
# infoFrame = Frame(root)
# infoFrame.pack(side="top", anchor=W, padx="5", pady="2")
#
# compilerVar = StringVar()
# compilerPath = Label(infoFrame, textvariable=compilerVar)
# compilerVar.set("Compiler: " + ccevar)
# compilerPath.pack(side="top", anchor=NW)
#
# fileVar = StringVar()
# filePath = Label(infoFrame, textvariable=fileVar)
# fileVar.set("Main source file: " + cfevar)
# filePath.pack(side="bottom", anchor=SW)
# End info frame

# Buttons frame
buttonsFrame = Frame(root)
buttonsFrame.pack(side="bottom", anchor=S, padx="5", pady="2")
compileButton = Button(buttonsFrame, width="7", text="Compile", command=compileFile, pady="1")
compileButton.pack(side="left")
aboutButton = Button(buttonsFrame, width="7", text="About", command=aboutWindow, pady="1")
aboutButton.pack(side="right")
# End buttons frame
root.mainloop()  # Show the window
