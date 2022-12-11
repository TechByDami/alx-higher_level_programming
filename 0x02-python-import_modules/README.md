## 0x02. Python - import & modules

![](https://alx-intranet.hbtn.io/images/challenge2022/get-started.jpg)

**What you should learn from this project**

At the end of this project you are expected to be able to explain to anyone, without the help of Google:

Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
How to import functions from another file
How to use imported functions
How to create a module
How to use the built-in function dir()
How to prevent code in your script from being executed when imported
How to use command line arguments with your Python programs

**Exercises**

**0. Import a simple function from a simple file**

     Write a program that imports the function def add(a, b): from the file add_0.py and prints the result 
     of the addition 1 + 2 = 3

* You have to use print function with string format to display integers
* You have to assign:
  * the value 1 to a variable called a
  * the value 2 to a variable called b
  * and use those two variables as arguments when calling the functions add and print
  * a and b must be define in 2 different lines: a = 1 and another b = 2
* You can only use the word add_0 once in your code
* You are not allowed to use '*' for importing or __import__
* Your code should not be executed when imported


**1. My first toolbox!**

     Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

* Do not use the function print (with string format to display integers) more than 4 times
* You have to define:
     * the value 10 to a variable a
     * the value 5 to a variable b
     * and use those two variables only, as arguments when calling functions (included print)
     * a and b must be define in 2 different lines: a = 10 and another b = 5
* Your program should call each of the imported functions. See example bellow for format
     the word calculator_1 should be used only once in your file
* You are not allowed to use * for importing or '__import__'
* Your code should not be executed when imported

**2. How to make a script dynamic!**

	Write a program that prints the number of and the list of its arguments.

The output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no argument where passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
* Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (preferred in a near Future), if you know them you can use them.

**3. Infinite addition**

	Write a program that prints the result of the addition of all arguments

The output should be the result of the addition of all arguments, followed by a new line
You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
* Your code should not be executed when imported

**4. Who are you?**

	Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

* You should print one name per line, in alpha order
* You should print only names that do not start with __
* Your code should not be executed when imported

**5. Everything can be imported**
	
	Write a program that imports the variable a from the file variable_load_5.py and prints its value.

* You are not allowed to use * for importing or __import__
* Your code should not be executed when imported

**6. Build my own calculator!**

	Write a program that imports all functions from the file calculator_1.py and handles basic operations.

* You are not allowed to use * for importing or __import__
* Your code should not be executed when imported

**7. Easy print**

	Write a program that prints #pythoniscool, followed by a new line, in the standard output.

* Your program should be maximum 2 lines long
* You are not allowed to use print or eval or open or import sys in your file 101-easy_print.py

**8. ByteCode -> Python #3**

	Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

**9. Fast alphabet**

	Write a program that prints the alphabet in uppercase, followed by a new line.

* Your program should be maximum 3 lines long
* You are not allowed to use:
        any loops
        any conditional statements
        str.join()
        any string literal
        any system calls

