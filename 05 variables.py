# ***********Python Variables***************

Here we will discuss about how to create the variables.

Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

#Example:
x = 5
y = "John"

print(x)
print(y)

#Variables do not need to be declared with any particular type and can even change type after they have been set.

#Example:

x = 4 # x is a variable of type int
x = "Sally" # x is now of type str

print(x)

#String variables can be declared either by using single or double quotes:

#Example:

x = "John"
# is the same as
x = 'John'

'''Variable Names:

1. A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
2. A variable name must start with a letter or the underscore character
3. A variable name cannot start with a number
4. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
5. Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

#Example:

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"


'''Remember that variable names in Python are case-sensitive.

Assign Value to Multiple Variables:

Python allows you to assign values to multiple variables in one line:
'''
#Example:

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:

#Example:

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Output Variables:

#The Python print statement is often used to output variables.

#To combine both text and a variable, Python uses the + character:

#Example:

x = "awesome"

print("Python is " + x)


#You can also use the + character to add a variable to another variable:

#Example:

x = "Python is "
y = "awesome"
z =  x + y

print(z)

#For numbers, the + character works as a mathematical operator:
#Example:

x = 5
y = 10
print(x + y)


#If you try to combine a string and a number, Python will give you an error:

#Example:

x = 5
y = "John"
print(x + y)

'''Global Variables:

Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Example:

Create a variable outside of a function, and use it inside the function
'''

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

Example:
  
Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

The global Keyword:
  
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Example:
  
If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
Also, use the global keyword if you want to change a global variable inside a function.

Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
