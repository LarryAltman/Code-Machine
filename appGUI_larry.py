from tkinter import *

root = Tk()
root.geometry("1300x600+0+0")
root.title("Code Converter")

def printOutput():
    labelActualCodeOutput.delete(1.0, END)
    labelOutput = entryCodeInsert.get(1.0, 'end-1c')
    labelActualCodeOutput.insert(END, labelOutput)

def clearOutputBox():
    labelActualCodeOutput.delete(1.0, END)

def checkHello():
    labelOutput = entryCodeInsert.get(1.0, 'end-1c')
    if labelOutput:
        printHelloWorldCustom()
    else:
        printHelloWorld()

def checkMath():
    labelOutput = entryCodeInsert.get(1.0, 'end-1c')
    if labelOutput:
        printWindowsMathCustom()
    else:
        printWindowsMath()

def checkArray():
    labelOutput = entryCodeInsert.get(1.0, 'end-1c')
    if labelOutput:
        printWindowsArrayCustom()
    else:
        printWindowsArray()

def printHelloWorld():
    labelActualCodeOutput.delete(1.0, END)
    windowsHello = ("#include <iostream>\
    \n#include <string>\
    \n\nint main()\n\
{\
      \n  std::string name;\
      \n  std::cout << 'Hello World! ';\
    \n}")
    labelActualCodeOutput.insert(END, windowsHello)

def printHelloWorldCustom():
    labelActualCodeOutput.delete(1.0, END)
    labelOutput = entryCodeInsert.get(1.0, 'end-1c')
    windowsHello = ("#include <iostream>\
    \n#include <string>\
    \n\nint main()\n\
{\
      \n  std::string name;\
      \n  std::cout << '" + labelOutput + "';\
    \n}")
    labelActualCodeOutput.insert(END, windowsHello)


def printWindowsMath():
    labelActualCodeOutput.delete(1.0, END)
    windowsMath = ("#include <iostream>\
    \n#include <string>\
    \n\nint main()\n\
{\
    \n  int datMath = 10 * 2;\
    \n  std::cout << \"10 * 2 = \" << datMath;\
    \n}")
    labelActualCodeOutput.insert(END, windowsMath)

def printWindowsMathCustom():
    labelActualCodeOutput.delete(1.0, END)
    labelOutput = entryCodeInsert.get(1.0, 'end-1c')
    windowsMath = ("#include <iostream>\
    \n#include <string>\
    \n\nint main()\n\
{\
    \n  int datMath = " + labelOutput + ";\
    \n  std::cout << \"" + labelOutput + " = \" << datMath;\
    \n}")
    labelActualCodeOutput.insert(END, windowsMath)


def printWindowsArray():
    labelActualCodeOutput.delete(1.0, END)
    windowsArray = ("#include <iostream>\
    \n#using namespace std\
    \n\nvoid printArray(int arr[], int size)\n{\
        \n  for ( int i = 0; i < size; i++ )\n{\
            \n  cout << arr[i] << ' ';\
        \n}\
        \n  cout << endl;\
    \n}\
    \n\
    \nint main() \
    \n{\
        \n  int arr[4] = { 6, 2, 5, 1 };\
        \n  cout << \"The array is: \";\
        \n  printArray(arr, 4);\
     \
        \n  return 0;\
    \n}")
    labelActualCodeOutput.insert(END, windowsArray)

def printWindowsArrayCustom():
    labelActualCodeOutput.delete(1.0, END)
    labelOutput = entryCodeInsert.get(1.0, 'end-1c')
    windowsArray = ("#include <iostream>\
    \n#using namespace std\
    \n\nvoid printArray(int arr[], int size)\n{\
        \n  for ( int i = 0; i < size; i++ )\n{\
            \n  cout << arr[i] << ' ';\
        \n}\
        \n  cout << endl;\
    \n}\
    \n\
    \nint main() \
    \n{\
        \n  int arr[4] = { 6, 2, 5, 1 };\
        \n  cout << \"The array is: \";\
        \n  printArray(arr, 4);\
     \
        \n  return 0;\
    \n}")
    labelActualCodeOutput.insert(END, windowsArray)


# Insert
labelCodeInsert = Label(root, text="Insert custom string, equation, or list here:")
entryCodeInsert = Text(root)
labelCodeInsert.place(x=100, y=100)
entryCodeInsert.place(x=100, y=125, height=400, width=400)

# Output
labelCodeOutput = Label(root, text="Output:")
labelActualCodeOutput = Text(root, fg="white", bg="grey")
labelCodeOutput.place(x=750, y=100)
labelActualCodeOutput.place(x=750, y=125, width=400, height=400)

# Android
labelAndroid = Label(root, text="Android:")
labelAndroid.place(x=575, y=350)

# Windows
labelWindwows = Label(root, text="Windows:")
labelWindwows.place(x=575, y=150)

# Buttons
buttonOutput = Button(root, text="Click for output", command=printOutput)
buttonOutput.place(x=250, y=550)

buttonClearOutputBox = Button(root, text="Clear output", command=clearOutputBox)
buttonClearOutputBox.place(x=900, y=550)

buttonHelloWorldOutput = Button(root, text="Hello", command=checkHello)
buttonHelloWorldOutput.place(x=575, y=180)

buttonHelloWorldOutput = Button(root, text="Math", command=checkMath)
buttonHelloWorldOutput.place(x=575, y=220)

buttonHelloWorldOutput = Button(root, text="Array", command=printWindowsArray)
buttonHelloWorldOutput.place(x=575, y=260)

root.mainloop()
