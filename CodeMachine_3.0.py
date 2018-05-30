from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import Tk
from tkinter import END


# Functions called by button clicks.
def clear_all():
    windows_output_box.delete(1.0, END)
    app_name_box.delete(1.0, END)
    input_box.delete(1.0, END)
    android_output_box.delete(1.0, END)


def save_windows_output():
    foo = ('\n  </Grid>\
    \n</Page>')
    output = windows_output_box.get(1.0, 'end-1c')
    f = open('windows_output.txt', 'w')
    f.write(output + foo)
    f.close()


def save_android_output():
    foo = ('\n  }\
    \n}')
    output = android_output_box.get(1.0, 'end-1c')
    f = open('android_output.txt', 'w')
    f.write(output + foo)
    f.close()


def check_checkbox():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        checkbox_windows_custom()
        checkbox_android_custom()
    else:
        checkbox_windows()
        checkbox_android()


def check_button():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        button_windows_custom()
        button_android_custom()
    else:
        button_windows()
        button_android()


def check_textbox():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        textbox_windows_custom()
        textbox_android_custom()
    else:
        textbox_windows()
        textbox_android()


def check_hello():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        hello_windows_custom()
        hello_android_custom()
    else:
        hello_windows()
        hello_android()


def check_math():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        math_windows_custom()
        math_android_custom()
    else:
        math_windows()
        math_android()


def check_array():
    user_input = input_box.get(1.0, 'end-1c')
    if user_input:
        array_windows_custom()
        array_android_custom()
    else:
        array_windows()
        array_android()


def checkbox_windows():
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    <CheckBox Content="CheckBox" HorizontalAlignment="Left" Margin="258,153,0,0" VerticalAlignment="Top"/>')
    else:
        windows_output_box.delete(1.0, END)
        foo = ('<Page\
    \nx:Class="' + app_name + '"\
    \n  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"\
    \n  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"\
    \n  xmlns:local="using:' + app_name + '"\
    \n  xmlns:d="http://schemas.microsoft.com/expression/blend/2008"\
    \n  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"\
    \n  mc:Ignorable="d">\
    \n\
    \n  <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">\
    \n    <CheckBox Content="CheckBox" HorizontalAlignment="Left" Margin="258,153,0,0" VerticalAlignment="Top"/>')
    windows_output_box.insert(END, foo)


def checkbox_windows_custom():
    user_input = input_box.get(1.0, 'end-1c')
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    <CheckBox Content="' + user_input + '" HorizontalAlignment="Left" Margin="258,153,0,0" VerticalAlignment="Top"/>')
    else:
        windows_output_box.delete(1.0, END)
        foo = ('<Page\
    \nx:Class="' + app_name + '"\
    \n  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"\
    \n  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"\
    \n  xmlns:local="using:' + app_name + '"\
    \n  xmlns:d="http://schemas.microsoft.com/expression/blend/2008"\
    \n  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"\
    \n  mc:Ignorable="d">\
    \n\
    \n  <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">\
    \n    <CheckBox Content="' + user_input + '" HorizontalAlignment="Left" Margin="258,153,0,0" VerticalAlignment="Top"/>')
    windows_output_box.insert(END, foo)


def button_windows():
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    <Button Content="Button" HorizontalAlignment="Left" Margin="234,239,0,0" VerticalAlignment="Top"/>')
    else:
        windows_output_box.delete(1.0, END)
        foo = ('<Page\
    \nx:Class="' + app_name + '"\
    \n  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"\
    \n  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"\
    \n  xmlns:local="using:' + app_name + '"\
    \n  xmlns:d="http://schemas.microsoft.com/expression/blend/2008"\
    \n  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"\
    \n  mc:Ignorable="d">\
    \n\
    \n  <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">\
    \n    <Button Content="Button" HorizontalAlignment="Left" Margin="234,239,0,0" VerticalAlignment="Top"/>')
    windows_output_box.insert(END, foo)


def button_windows_custom():
    user_input = input_box.get(1.0, 'end-1c')
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    <Button Content="' + user_input + '" HorizontalAlignment="Left" Margin="234,239,0,0" VerticalAlignment="Top"/>')
    else:
        windows_output_box.delete(1.0, END)
        foo = ('<Page\
    \nx:Class="' + app_name + '"\
    \n  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"\
    \n  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"\
    \n  xmlns:local="using:' + app_name + '"\
    \n  xmlns:d="http://schemas.microsoft.com/expression/blend/2008"\
    \n  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"\
    \n  mc:Ignorable="d">\
    \n\
    \n  <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">\
    \n    <Button Content="' + user_input + '" HorizontalAlignment="Left" Margin="234,239,0,0" VerticalAlignment="Top"/>')
    windows_output_box.insert(END, foo)


def textbox_windows():
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    <TextBox HorizontalAlignment="Left" Margin="249,335,0,0" Text="TextBox" VerticalAlignment="Top"/>')
    else:
        windows_output_box.delete(1.0, END)
        foo = ('<Page\
    \nx:Class="' + app_name + '"\
    \n  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"\
    \n  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"\
    \n  xmlns:local="using:' + app_name + '"\
    \n  xmlns:d="http://schemas.microsoft.com/expression/blend/2008"\
    \n  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"\
    \n  mc:Ignorable="d">\
    \n\
    \n  <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">\
    \n    <TextBox HorizontalAlignment="Left" Margin="249,335,0,0" Text="TextBox" VerticalAlignment="Top"/>')
    windows_output_box.insert(END, foo)


def textbox_windows_custom():
    user_input = input_box.get(1.0, 'end-1c')
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    <TextBox HorizontalAlignment="Left" Margin="249,335,0,0" Text="' + user_input + '"VerticalAlignment="Top"/>')
    else:
        windows_output_box.delete(1.0, END)
        foo = ('<Page\
    \nx:Class="' + app_name + '"\
    \n  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"\
    \n  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"\
    \n  xmlns:local="using:' + app_name + '"\
    \n  xmlns:d="http://schemas.microsoft.com/expression/blend/2008"\
    \n  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"\
    \n  mc:Ignorable="d">\
    \n\
    \n  <Grid Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">\
    \n    <TextBox HorizontalAlignment="Left" Margin="249,335,0,0" Text="' + user_input + '" VerticalAlignment="Top"/>')
    windows_output_box.insert(END, foo)


def checkbox_android():
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    final CheckBox checkBox = (Checkbox) findViewById(R.id.checkbox_id);\
        \n    if (checkBox.isChecked()) {\
        \n        checkBox.setChecked(false); \
        \n    }')
    else:
        android_output_box.delete(1.0, END)
        foo = ('public class ' + app_name + ' {\
    \n  protected void onCreate(Bundle icicle) {\
    \n    super.onCreate(icicle);\
    \n    setContentView(R.layout.activity_hello);\
    \n    final CheckBox checkBox = (CheckBox) findViewById(R.id.checkbox_id);\
    \n    if (checkBox.isChecked()) {\
    \n        checkBox.setChecked(false);\
    \n    }')
    android_output_box.insert(END, foo)


def checkbox_android_custom():
    user_input = input_box.get(1.0, 'end-1c')
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    final CheckBox checkBox = (' + user_input + ') findViewById(R.id.checkbox_id);\
        \n    if (checkBox.isChecked()) {\
        \n        checkBox.setChecked(false); \
        \n    }')
    else:
        android_output_box.delete(1.0, END)
        foo = ('public class ' + app_name + ' {\
    \n  protected void onCreate(Bundle icicle) {\
    \n    super.onCreate(icicle);\
    \n    setContentView(R.layout.' + user_input + ');\
    \n    final CheckBox checkBox = (CheckBox) findViewById(R.id.checkbox_id);\
    \n    if (checkBox.isChecked()) {\
    \n        checkBox.setChecked(false);\
    \n    }')
    android_output_box.insert(END, foo)


def button_android():
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('    findViewById(R.id.button).setOnClickListener(new View.OnClickListener() {\
        \n    public void onClick(View view) {\
        \n   startActivity(new Intent(HelloActivity.this, GoodbyeActivity.class));\
        \n    }\
        \n}')
    else:
        android_output_box.delete(1.0, END)
        foo = ('public class ' + app_name + ' {\
    \n  protected void onCreate(Bundle savedInstanceState) {\
    \n    super.onCreate(savedInstanceState);\
    \n    setContentView(R.layout.activity_hello);\
    \n    findViewById(R.id.button).setOnClickListener(new View.OnClickListener() {\
    \n    public void onClick(View view) {\
    \n   startActivity(new Intent(HelloActivity.this, GoodbyeActivity.class));\
    \n    }\
    \n}\n')
    android_output_box.insert(END, foo)


def button_android_custom():
    user_input = input_box.get(1.0, 'end-1c')
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('    findViewById(R.id.button).setOnClickListener(new View.OnClickListener() {\
        \n    public void onClick(View view) { \
        \n   startActivity(new Intent(' + user_input + '));\
        \n}')
    else:
        android_output_box.delete(1.0, END)
        foo = ('public class ' + app_name + ' {\
    \n  protected void onCreate(Bundle savedInstanceState) {\
    \n    super.onCreate(savedInstanceState);\
    \n    setContentView(R.layout.' + user_input + ');\
    \n    findViewById(R.id.button).setOnClickListener(new View.OnClickListener() {\
    \n    public void onClick(View view) {\
    \n   startActivity(new Intent(HelloActivity.this, GoodbyeActivity.class));\
    \n    }\
    \n}\n')
    android_output_box.insert(END, foo)


def textbox_android():
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    final TextView helloTextView = (TextView) findViewById(R.id.text_view_id);\
        \n    helloTextView.setText(R.string.user_greeting);\
        ')
    else:
        android_output_box.delete(1.0, END)
        foo = ('public class ' + app_name + ' {\
    \n  protected void onCreate(Bundle savedInstanceState) {\
    \n    super.onCreate(savedInstanceState);\
    \n    setContentView(R.layout.activity_hello);\
    \n    final TextView helloTextView = (TextView) findViewById(R.id.text_view_id);\
    \n    helloTextView.setText(R.string.user_greeting);')
    android_output_box.insert(END, foo)


def textbox_android_custom():
    user_input = input_box.get(1.0, 'end-1c')
    user_output = android_output_box.get(1.0, 'end-1c')
    app_name = app_name_box.get(1.0, 'end-1c')
    if user_output:
        foo = ('\n    final TextView helloTextView = (TextView) findViewById(R.id.text_view_id);\
        \n    helloTextView.setText(R.string.' + user_input + ');\
        ')
    else:
        android_output_box.delete(1.0, END)
        foo = ('public class ' + app_name + ' {\
    \n  protected void onCreate(Bundle savedInstanceState) {\
    \n    super.onCreate(savedInstanceState);\
    \n    setContentView(R.layout.activity_hello);\
    \n    final TextView helloTextView = (TextView) findViewById(R.id.text_view_id);\
    \n    helloTextView.setText(R.string.' + user_input + ');')
    android_output_box.insert(END, foo)


def hello_windows():
    windows_output_box.delete(1.0, END)
    hello = ("#include <iostream>\
    \n#include <string>\
    \n\nint main() {\
    \n  std::cout << \"Hello World! \";\
    \n}")
    windows_output_box.insert(END, hello)


def hello_windows_custom():
    windows_output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    hello = ("#include <iostream>\
    \n#include <string>\
    \n\nint main() {\
    \n  std::cout << \"" + user_input + " \";\
    \n}")
    windows_output_box.insert(END, hello)


def math_windows():
    windows_output_box.delete(1.0, END)
    math = ("#include <iostream>\
    \n#include <string>\
    \n\nint main() {\
    \n  double foo = 10 * 2;\
    \n  std::cout << \"10 * 2 = \" << foo;\
    \n}")
    windows_output_box.insert(END, math)


def math_windows_custom():
    windows_output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    math = ("#include <iostream>\
    \n#include <string>\
    \n\nint main() {\
    \n  double foo = " + user_input + ";\
    \n  std::cout << \"" + user_input + " = \" << foo;\
    \n}")
    windows_output_box.insert(END, math)


def array_windows():
    windows_output_box.delete(1.0, END)
    array = ("#include <iostream>\
    \nusing namespace std;\n\
    \nvoid printArray(int arr[], int size) {\
    \n  for ( int i = 0; i < size; i++ ) {\
    \n      cout << arr[i] << ' ';\
    \n  }\
    \n  cout << endl;\
    \n}\n\
    \nint main() {\
    \n  int arr[6] = { 3, 2, 3, 1, 2, 4 };\
    \n  cout << \"The array is: \";\
    \n  printArray(arr, 6);\
    \n  return 0;\
    \n}")
    windows_output_box.insert(END, array)


def array_windows_custom():
    windows_output_box.delete(1.0, END)
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
    \nvoid printArray(int arr[], int size) {\
    \n  for ( int i = 0; i < size; i++ ) {\
    \n      cout << arr[i] << ' ';\
    \n  }\
    \n  cout << endl;\
    \n}\n\
    \nint main() {\
    \n  int arr[" + str(len(user_input)) + "] = { " + user_input_string + " };\
    \n  cout << \"The array is: \";\
    \n  printArray(arr, " + str(len(user_input)) + ");\
    \n  return 0;\
    \n}")
    windows_output_box.insert(END, array)


def hello_android():
    android_output_box.delete(1.0, END)
    hello = ("public class HelloWorld {\n\
    \n  public static void main(String[] args) {\
    \n    System.out.println(\"Hello, World\");\
    \n  }\
    \n}")
    android_output_box.insert(END, hello)


def hello_android_custom():
    android_output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    hello = ("public class HelloWorld {\n\
    \n  public static void main(String[] args) {\
    \n    System.out.println(\"" + user_input + "\");\
    \n  }\
    \n}")
    android_output_box.insert(END, hello)


def math_android():
    android_output_box.delete(1.0, END)
    math = ("public class MyClass {\n\
    \n  public static void main(String[] args) {\
    \n    double foo = 5 + 12;\
    \n    System.out.println(\"5 + 12 = \"  + foo);\
    \n  }\
    \n}")
    android_output_box.insert(END, math)


def math_android_custom():
    android_output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    math = ("public class MyClass {\n\
    \n  public static void main(String[] args) {\
    \n    double foo = " + user_input + ";\
    \n    System.out.println(\"" + user_input + " = \" + foo);\
    \n  }\
    \n}")
    android_output_box.insert(END, math)


def array_android():
    android_output_box.delete(1.0, END)
    array = ("public class TestArray {\n\
    \n  public static void main(String[] args) {\
    \n    double[] myList = {1.9, 2.9, 3.4, 3.5};\n\
    \n      for (int i = 0; i < myList.length; i++) {\
    \n        System.out.println(myList[i] + " ");\
    \n      }\
    \n  }\
    \n}")
    android_output_box.insert(END, array)


def array_android_custom():
    android_output_box.delete(1.0, END)
    user_input = input_box.get(1.0, 'end-1c')
    user_input_list = []
    user_input_string = ""

    for i in user_input:
        user_input_list.append(i)

    for i in user_input_list[:-1]:
        user_input_string += str(i) + ", "
    user_input_string += str(user_input_list[-1])

    array = ("public class TestArray {\n\
    \n  public static void main(String[] args) {\
    \n    double[] myList = {" + user_input_string + "};\n\
    \n      for (int i = 0; i < myList.length; i++) {\
    \n        System.out.println(myList[i] + " ");\
    \n      }\
    \n  }\
    \n}")
    android_output_box.insert(END, array)


root = Tk()
root.geometry("1300x620+0+0")
root.title("Code Machine")

# Title
title_textbox = Label(root, text="Code Machine")
title_textbox.place(x=500, y=30)
title_textbox.config(font=("Century Gothic", 25))

# Text boxes
input_box = Text(root)
input_box.place(x=560, y=320, height=90, width=130)
windows_output_box = Text(root, fg="lawn green", bg="gray10")
windows_output_box.place(x=100, y=125, height=400, width=400)
app_name_box = Text(root)
app_name_box.place(x=560, y=460, height=30, width=130)
android_output_box = Text(root, fg="lawn green", bg="gray10")
android_output_box.place(x=750, y=125, width=400, height=400)

# Text labels
input_box_label = Label(root, text="C++")
input_box_label.place(x=280, y=100)
insert_text_label = Label(root, text="Insert custom text:")
insert_text_label.place(x=570, y=290)
app_name_label = Label(root, text="App name:")
app_name_label.place(x=590, y=430)
output_label = Label(root, text="Java")
output_label.place(x=930, y=100)
windows_label = Label(root, text="Functions")
windows_label.place(x=595, y=140)


# Buttons
output_button = Button(root, text="Save", command=save_windows_output)
output_button.place(x=270, y=560)
clear_input_button = Button(root, text="Clear", command=clear_all)
clear_input_button.place(x=600, y=560)
clear_output_button = Button(root, text="Save", command=save_android_output)
clear_output_button.place(x=920, y=560)


# Function buttons
hello_button = Button(root, text="Hello", command=check_hello)
hello_button.place(x=550, y=180)
hello_button = Button(root, text="Check Box", command=check_checkbox)
hello_button.place(x=523, y=230)
math_button = Button(root, text="Math", command=check_math)
math_button.place(x=605, y=180)
math_button = Button(root, text="Button", command=check_button)
math_button.place(x=600, y=230)
array_button = Button(root, text="Array", command=check_array)
array_button.place(x=660, y=180)
array_button = Button(root, text="Text Box", command=check_textbox)
array_button.place(x=660, y=230)


root.mainloop()

# Created by Harrison Brown, Larry Altman, and Syldon Harding to please Dr. Nguyen.
# Computer Science Capstone COM-497
# Saint Leo University
# April 13, 2018
