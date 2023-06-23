# C++ Basics

# About C++

- Compiled language
- Came from the C language
- Object oriented language

# C++ is compiled 

- Take code and run it through a compiler
- Compiler creates object code 
- with that object code you create the executable program
- When ready to use your program, you use the executable to send out and this produces your output

- Python, on the other hand, is an interpreted language
- Take the source code. 
- Put it through an interpreter
- get your output

# output 

Code: 

```
int num = 10;					
cout << “Just Text”; 		
cout << “Text Line” << endl; 	
cout << num << endl; 			
```

Output:

Just TextText Line
10
Text: 10 

# Literals 

# Fixed values: 
- no quotes

cout << 42;

# Character literals
- use single quotes
cout << ‘B’;

# String Literals 
- use double quotes

cout << “moo”; 

# escape characters

- \n End Line
- \t Tab
- \’ display single quote
- \” display double quote 
```
cout << “She said\t\”LOL”\””; 
```
She said “LOL” 

# endl vs \n

- endl not used in quotes

cout << “End the line” << endl; 

- \n is used in quotes
cout << “End the line\n”; 

# C ++ Variables


# Typed Languages
Type matters when performing operations on a variable

- Statically typed: must specify the type of variable
C ++ and Java

-Dynamically typed: type of variable is determined during runtime
Python 

# python is  a non-typed language

numStudents = 42;
Letter = “W”; 
Percentage = .95;


# Primitive data types like C++ and Java

- int      				whole numbers
- float     			decimal numbers 32 bit
- double      			decimal numbers 64 bit
- bool 				true/false
- char 				single character 

# rules for naming a variable

- Only alphabet character numbers and underscore_
Should begin with a letter, cannot begin with a number

- Preferred practice is to being with a lowercase letter

- Cannot be a keyword

# Preferences for naming a variable

- Upper Camel Case: Classes and function

class PigPlayer()
void Go()()

- Upper Snake Case: Classes and functions

Class Pig_Player ()
Void Go()()

* programmer preference for which of these 2 they prefer; just be consistent

- Lower CamelCase: Variables 
string firstName;
int primeValue;  

- Lower Snake Case: Variables 

string first_Name;
int prime_Value; 

- Upper Case: Constants
const int MAX_VALUE = 256;

# Variable Names 

- Preferred Variable Names

string firstName = “Bob”;
string firstName_ = “Bob”; 


- Valid Variable Names
```
string first_Name = “Bob”;
string _firstName = “Bob”;
```
- Invalid Variable Names

```
string First Name = “Bob”;
string 1Name = “Bob”;
int if = 21; 
 
 ```
# C ++ Declare a variable

- Name and type together

- C++
```
int numStudents = 42;
char letter = ‘W’;
double percentage = .95;
```
* python
```
numStudents = 42;
letter = “W”;
percentage = .95; 
```
# User input

- Get input from user (:cin statement)

	
* C++
  ```
double angle; 
int x, y;

cout << “Enter the angle: “;
cin >> angle;

cout << “Enter x and y: “;
cin >> x >> y; 
```


* python
angle = int(input(“Enter an angle: “))
x, y = int(input(“Enter x and y: “)).split()
print(x,y)

# Arithmetic Operators 

- (+) Addition 
- 	(-) subtraction
-		(*)	multiplication
-		/ 	division
-		% 	modulus (remainder)
-		Add to:   ++  (does not work in python) or +=
-		Subtract from: - - (does not work in python) or -= 

		E.g.   int xPos = 5;
			xPos += 3;  so xPos = 8 

		* same in python
		xPos = 5;
		xPos
