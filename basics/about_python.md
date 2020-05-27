# Python MMR (Minimum Memory Requirement)

## About
This document consists of basic python which serves as a minimum memory requirement for writing elementary code in python without use of any other external documentation.

This document is incomplete for now and still being updated. It's hard to keep it short as well as exhaustive. However, for beginners the current version covers many things and might be useful.

## Key Facts:
1. Interpreted language - unlike C++, which is a compiled language.
2. Dynamically typed (Automatic inferring of types).
3. Strongly typed (Stricter typing rules at compile time and variables are bound to specific data types).
4. Object-oriented language.

### Other random facts:
* Variables store references and not objects
* Simultaneous assignemnt possible: `(x, y) = (y, x)`
* literals = values that are written exactly as it's meant to be interpreted
* In Python, everything is an object, literally everything

## Essential Python Libraries:
* Numpy - Numerical Processing
* Pandas - Data Analysis
* Matplotlib - Visualization
* Scikit - Processing ML datasets

## Commonly used Data Types:
1. Numbers 
    * immutable type
    * Eg: `int`, `float`, `complex`
2. String 
    * immutable type
    * Usage: `""` or `''`
3. List
    * mutable type
    * Like arrays
    * Usage: `[]`
    * Eg: `["a", 2]`
4. Tuple
    * immutable type
    * multiple return values are wrapped in a tuple
    * Usage: `()`
    * Like lists but immutable
5. Dictionary
    * mutable type
    * Usage: `{}`
    * key-value pairs - `{k1:v1, k2:v2}`
    * Like maps in C++
    
## Commonly used built-in functions:
1. `type(var)` - get the type
2. `id(var)` - get the reference address
3. `input()` - get console input as a string
4. `ord()` - function returns the ASCII code of the character.
5. `chr()` - function returns character represented by a ASCII number.
6. `len(str)` - returns length of string
7. `in` and `not in` - boolean membership operators
8. `print("text", end="")`
9. `isinstance(object, class_type)` - returns True if object is of type class_type
10. `dir(object)` - find all attributes (i.e all available classes, functions, variables and constants ) of the object.

## Python loops:
1. `for i in iterable_object:`
2. `for i in range(start, end, step_size):`
3. `while condition:`

### Using else block with loops:
Note: Else is only executed when for loop exits gracefully (i.e. not from a break statement)
##### Example:

```python
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break")
```

## List comprehension:

`list_ = [ x for x in range(10) if x%2 == 0 ]`

## Functions:

```python
def empty_func(args):
      pass  #to bypass body
```

### Use Global variables in functions as a local variable:

```python
gvar = 10 # You can also declare global variables directly inside the function using keyword global
def increment() :
    global gvar
    gvar += 1
increment()
print(gvar) # prints 11
```

## File Handling:

```python
f = open(filename, mode)
f.read()
f.read([index])
f.readline() # returns single line
f.readlines() # returns list of lines
f.write('Add this statement\n')
f.close()
```

## Objects and Classes:
### Creating a class

```python
class Person :
    # constructor
    def __init__(self, name): # self represents the instance of the class
        self.name = name
        # When you create new object the self parameter in the __init__  method is automatically set to reference
        # the object you have just created.

    def whoami(self):
        return "You are " + self.name
```

### Creating an object

```python
p1 = Person('tom')
print(p1.whoami())
print(p1.name) # prints 'tom'

# When you call a method you don't need to pass anything to self parameter, python automatically does that for you
# behind the scenes. i.e. self parameter is automatically passed if you haven't explicitly
```

#### Underscore usage in variable names and methods:
1. `_var` or `_methods` aren't imported during wildcard imports. (Indicates the variable is for internal use - Programmer's perspective)
2. `__var` or `__method` names are mangled with and cannot be accessed with the same names. Helps to prevent overriding the child variables or methods.
3. There are no real real private attributes in Python like Java does
4. `_` (Single underscores) are don't cares
5. `__special_methods__` (Double underscores at start and end with special names such as init in between are reserved for magic methods)
6. `var_` (Used to avoid naming conflicts with reserved keywords)


### Pseudo Private fields in a class

```python
class BankAccount :
    # constructor
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money :
            self.__balance -= money
            return money
        else :
            return "Insufficient Funds"

    def checkbalance(self):
        return self.__balance

b1 = BankAccount('Tim', 400)
b1.deposit(500)
print(b1.checkbalance) # prints 900
print(b1.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'
# __balance field is not accessible outside the class.
```

#### Python Operator Overloading:

```python
class Circle :

    def __init__(self, radius):
        self.__radius = radius

    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius)

c1, c2 = Circle(4), Circle(5)
c3 = c1 + c2 # has radius 9
```

### Python inheritance and polymorphism:
* Inheritance allows programmer to create a general class first then later extend it to more specialized class.
* It also allows programmer to write better code and avoids rewriting of code froms scratch.

##### Notes:
1. class X extends class Y, then
   Y is called super class or base class
   X is called sub class or derived class

2. Only data fields and methods that are not private are accessible by child classes.

3. Public, Protected and Private data members or methods:
   `var` is public
   `_var` is protected
   `__var` is private

   `method` is public
   `_method` is protected
   `__method` is private
   
4. `super()` function is used to call method of the base class.

##### Example:

```python
class Vehicle:

    def __init__(self, name, color):
        self.__name = name      # __name is private to Vehicle class
        self.__color = color

    def getColor(self):         # getColor() function is public and hence accessible to class Car and outside
        return self.__color

    def setColor(self, color):  # setColor is accessible outside the class
        self.__color = color

    def getName(self):          # getName() is accessible outside the class
        return self.__name

class Car(Vehicle):

    def __init__(self, name, color, model):
        # call parent constructor to set name and color
        super().__init__(name, color)
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"

# in method getDescrition we are able to call getName(), getColor() because they are
# accessible to child class through inheritance

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName()) # car has no method getName() but it is accessible through class Vehicle
```


### Multiple inheritance

##### Notes:
1. You can inherit from multiple classes at the same time (unlike java).

##### Example:

```python
class MySuperClass1():

    def method_super1(self):
        print("method_super1 method called")

class MySuperClass2():

    def method_super2(self):
        print("method_super2 method called")

class ChildClass(MySuperClass1, MySuperClass2):

    def child_method(self):
        print("child method")

c = ChildClass()
c.method_super1()
c.method_super2()
```

### Overriding methods

##### Notes:
1. To override a method in the base class, sub class needs to define a method of same signature.

##### Example:

```python
class A():

    def __init__(self):
        self.__x = 1

    def m1(self):
        print("m1 from A")


class B(A):

    def __init__(self):
        self.__y = 1

    def m1(self):
        print("m1 from B")

c = B()
c.m1() # prints "m1 from B"
```

## Python Exception Handling

##### Notes:
1. try, except blocks along with optional else and finally blocks.
2. except block gets executed only if the exception type matches the exception name.
3. The except clause is similar to elif. In last except clause ExceptionType is omitted.
4. If exception does not match any exception type before the last except clause, then the handler for last except clause is executed.
5. Statements under the else clause run only when no exception is raised.
6. Statements in the finally clause will run every time no matter exception occurs or not.

##### Example:

```python
try:
    <body>
except <ExceptionType1>:
    <handler1>
except <ExceptionTypeN>:
    <handlerN>
except:
    <handlerExcept>
else:
    <process_else>
finally:
    <process_finally>
```

### Raising Exceptions:

##### Notes:
1. Syntax: raise ExceptionClass("Your argument")

##### Example:

```python
def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    num = int(input("Enter your age: "))
    enterage(num)

except ValueError:
    print("Only positive integers are allowed")
except:
    print("something is wrong")
```

#### Using Exception Objects

##### Example:

```python
try:
    # this code is expected to throw exception
except ExceptionType as ex:
    # code to handle exception
    print("Exception:", ex)
```

#### Creating custom exception class :

##### Example:

```python
# file NegativeAgeException.py
class NegativeAgeException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age

# usage in code
def enterage(age):
    if age < 0:
        raise NegativeAgeException("Only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    num = int(input("Enter your age: "))
    enterage(num)
except NegativeAgeException:
    print("Only positive integers are allowed")
except:
    print("something is wrong")
```

## Python *args and **kwargs:
1. `*args` allows us to pass variable number of arguments to the function.
2. `**kwargs` allows us to pass variable number of keyword arguments.
3. You can use *args and **kwargs to pass elements and items respectively in an iterable variable to a function.

##### Example:

```python
    # *args
def sum(*myargs):
    s = 0
    for i in myargs:
        s += i
    print("sum is", s)
```

```python
# **kwargs
def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i, j)

my_func(name='tim', sport='football', roll=19)
```

```python
# Usage of *args to pass elements to a function
def my_three(a, b, c):
    print(a, b, c)

a = [1,2,3]
my_three(*a) # here list is broken into three elements
```

```python
# Usage of **kwargs to pass items into a function
def my_three(a, b, c):
    print(a, b, c)

a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a)
```

## Python Generators

#### Notes:
1. Generators are defined similar to functions, but instead we use yield instead of return statement
2. Also, in practice yeild is run inside a loop and values are returned continuously until exit condition

##### Example:

```python
def my_range(start, stop, step = 1):
    if stop <= start:
        raise RuntimeError("start must be smaller than stop")
    i = start
    while i < stop:
        yield i
        i += step

try:
    for k in my_range(10, 50, 3):
        print(k)
except RuntimeError as ex:
    print(ex)
except:
    print("Unknown error occurred")
```

## Python recursive functions:
1. Python has a default recursive limit of 1000. Change it by setting -

```python
sys.setrecursionlimit(desired_limit)
```

## What is `__name__ == "__main__"` ?
1. Every module in Python has a special attribute called `__name__`
2. The value of `__name__`  attribute is set to `'__main__'`  when module run as main program.
3. Otherwise, the value of `__name__`  is set to contain the name of the module.

#### Note:
1. So, when you import a module, the whole script in the module runs, and thus, since it's being imported, the block below won't get executed
   `if __name__ == "__main__":`

## Importing modules:
1. `import numpy as np` - keyword `np` used to access all member variables and methods.
2. `from numpy import array` - only array method gets imported.
3. `from numpy import *` - Should be avoided. In this case, to use properties of a module, you need not dereference and can use directly.

## Python Lambda Function:
1. Python allows to create anonymous function using a facility called lambda.
2. Lambda functions can have arguments just like a normal function, but their execution is assumed small, usually not more than a line.
3. Result of the expression is when the lambda is applied to an argument. There is no neeed for any return statement.

##### Example:

```python
# Multiplication of two numbers
r = lambda x, y: x*y
r(1,2) # called the lambda function

# Signature
ret_value = lambda arg1, arg2, ... : some_operations_on_args_which is_returned
val1 = ret_value(arg1, arg2, ...)

# Need not assign a lambda function to a variable
(lambda x, y: x*y)(2,3) # will return 6
# More generally
(lambda *args : operation_to_be_returned)(*args)
```

## `"__init__.py"` use cases
#### File structure:
```
your_package/
  __init__.py
  file1.py
  file2.py
    ...
  fileN.py
  sub_package/
    __init__.py
    sub_file1.py
```

Considering a package with multiple modules (and possibly sub-packages), there seems to be 3 different approaches:

1. Leave the `__init__.py` blank.
This enforces explicit imports and thus clear namespaces.
The cons are, the user of the package has to import seperate modules and call them with the dot notation.

2. Import all modules in `__init__.py`.
The user doesn't have to do multiple imports.
The cons are explicit vs implicit, and also put it as (paraphrased), "if that's how your package works, maybe it should all go in a single module anyway".

3. Import key functions from various modules directly into the package namespace.
If you restructure modules, you still have the option to keep the same API for end users.
Cons, it dirties the namespace, and very implicit / hacky.
[Mostly used among all 3]

## Difference between Python Modules and Packages:
1. A module is a file containing Python code. A package, however, is like a directory that holds sub-packages and modules.
2. A package must hold the file `__init__.py` (Not needed since Python 3.3). This does not apply to modules.
3. To import everything from a module, we use the wildcard `*`. But this does not work with packages.
`import pkg` will not import all the modules, instead will execute `__init__.py`

## NamedTuple

1. Just like dictionary with additional functionalities and are ordered. Hence, can be accessed by index.
2. Access by keyname.
3. Access by using `getattr(<named_tuple>, <key_value>)`
 
##### Example:

```python
import collections

# namedtuple(<typename>, <fieldnames>)

# Declaring namedtuple()
Student = collections.namedtuple('student_typename',['name','age','DOB'])
# OR
Student = collections.namedtuple('student_typename','name, age, DOB')
# OR
Student = collections.namedtuple('student_typename','name age DOB')

# Adding values
S = Student('Shruti','19','26091996')
# OR
S = Student(name="Shruti", age="19", DOB="26091996")

# Access using index
print(S[1]) # Prints 19

# Access using key
print(S.name) # Prints Shruti

# Access using getattr()
print(getattr(S,'DOB')) # prints 26091996
```

