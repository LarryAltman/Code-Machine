from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import Tk
from tkinter import END


# Functions called by button clicks.
def print_output():
    output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    output_box.insert(END, user_input)


def clear_input_box():
    input_box.delete(1.0, END)


def clear_output_box():
    output_box.delete(1.0, END)


def check_hello():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        hello_windows_custom()
    else:
        hello_windows()


def check_math():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        math_windows_custom()
    else:
        math_windows()


def check_array():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        array_windows_custom()
    else:
        array_windows()


def hello_windows():
    output_box.delete(1.0, END)
    hello = ("#include <iostream>\
    \n#include <string>\
    \n\nint main()\
    \n{\
    \n  std::cout << \"Hello World! \";\
    \n}")
    output_box.insert(END, hello)


def hello_windows_custom():
    output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    hello = ("#include <iostream>\
    \n#include <string>\
    \n\nint main()\
    \n{\
    \n  std::cout << \"" + user_input + " \";\
    \n}")
    output_box.insert(END, hello)


def math_windows():
    output_box.delete(1.0, END)
    math = ("#include <iostream>\
    \n#include <string>\
    \n\nint main()\
    \n{\
    \n  int foo = 10 * 2;\
    \n  std::cout << \"10 * 2 = \" << foo;\
    \n}")
    output_box.insert(END, math)


def math_windows_custom():
    output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    math = ("#include <iostream>\
    \n#include <string>\
    \n\nint main()\
    \n{\
    \n  int foo = " + user_input + ";\
    \n  std::cout << \"" + user_input + " = \" << foo;\
    \n}")
    output_box.insert(END, math)


def array_windows():
    output_box.delete(1.0, END)
    array = ("#include <iostream>\
    \nusing namespace std;\n\
    \nvoid printArray(int arr[], int size)\
    \n{\
    \n  for ( int i = 0; i < size; i++ )\
    \n  {\
    \n      cout << arr[i] << ' ';\
    \n  }\
    \n  cout << endl;\
    \n}\n\
    \nint main()\
    \n{\
    \n  int arr[6] = { 3, 2, 3, 1, 2, 4 };\
    \n  cout << \"The array is: \";\
    \n  printArray(arr, 6);\
    \n  return 0;\
    \n}")
    output_box.insert(END, array)


def array_windows_custom():
    output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    user_input_list = []
    user_input_string = ""

    for i in user_input:
        user_input_list.append(i)

    for i in user_input_list[:-1]:
        user_input_string += str(i) + ", "
    user_input_string += str(user_input_list[-1])

    array = ("#include <iostream>\
    \nusing namespace std;\n\
    \nvoid printArray(int arr[], int size)\
    \n{\
    \n  for ( int i = 0; i < size; i++ )\
    \n  {\
    \n      cout << arr[i] << ' ';\
    \n  }\
    \n  cout << endl;\
    \n}\n\
    \nint main()\
    \n{\
    \n  int arr[" + str(len(user_input)) + "] = { " + user_input_string + " };\
    \n  cout << \"The array is: \";\
    \n  printArray(arr, " + str(len(user_input)) + ");\
    \n  return 0;\
    \n}")
    output_box.insert(END, array)


root = Tk()
root.geometry("1300x600+0+0")
root.title("CodeMachine")

# Insert text box
input_box_label = Label(root, text="Enter values for button functions (default \
used if empty):")
input_box_label.place(x=100, y=100)

input_box = Text(root)
input_box.place(x=100, y=125, height=400, width=400)

# Output text box
output_label = Label(root, text="Output:")
output_label.place(x=750, y=100)

output_box = Text(root, fg="white", bg="grey")
output_box.place(x=750, y=125, width=400, height=400)

# Text labels
android_label = Label(root, text="Android:")
android_label.place(x=575, y=350)

windows_label = Label(root, text="Windows:")
windows_label.place(x=575, y=150)

# Buttons
output_button = Button(root, text="Output", command=print_output)
output_button.place(x=250, y=550)

clear_input_button = Button(root, text="Clear", command=clear_input_box)
clear_input_button.place(x=310, y=550)

clear_output_button = Button(root, text="Clear", command=clear_output_box)
clear_output_button.place(x=900, y=550)

hello_button = Button(root, text="Hello", command=check_hello)
hello_button.place(x=575, y=180)

math_button = Button(root, text="Math", command=check_math)
math_button.place(x=575, y=220)

array_button = Button(root, text="Array", command=check_array)
array_button.place(x=575, y=260)

root.mainloop()
