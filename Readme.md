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
  
double angle; 
int x, y;

cout << “Enter the angle: “;
cin >> angle;

cout << “Enter x and y: “;
cin >> x >> y; 



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
-		Subtract from: - - (does not work in python) or - 

		E.g.   int xPos = 5;
			xPos += 3;  so xPos = 8 

		* same in python
		xPos = 5;
		xPos += 3;  (xPos = 8)

# Division Types

Modulus division %
 - result is the remainder

 int division

 - result dropts the decimal places
 - in python use the // operator 
 - in c++, results when int is divided by an int


 regular division
 - result is the answer

 # integer division

 - an int divided by an int is an int

 # modulus division

 - finds the remainder

 # python division example

 quotient = 13//2
 remainder = 13 % 2

 print("13 divided by 2 is ", quotient, "r", remainder)


 answer: 13 divided by 2 is 6 r 1 

  - same example in c++
  int quotient = 13/2 
  int remainder = 13 % 2
  cout << "13 divided by 2 is" << quotient << "r" << remainder; 

  answer: 13 divided by 2 is 6 r 1

# constant values 

a value that cannot be altered 
- this concept is not used in python

const double PI = 3.14159;
const int MAX_VALUE = 256; 

* all caps when making a constant variable

# enum constant values

- quick way to do multiple constants 
- must be int values 

enum{NORTH, EAST, SOUTH, WEST}; 

defined as 0(North), 1(East), 2(South), 3(West) 

- no real difference between const and enum
- enum cannot be a floating point value while const can 

# library functions

C++:
#include<cmath>

round() round a number to nearest integer
ceil() will round up to next integer
floor() will round down to previous integer
abs() take absolute value of -3.5   is 3.5
sin() cos() tan()
pow()   sqrt()

for python: 
import math

round()  abs()
math.ceil() math.floor()
math.sin()   math.cos()  math.tan()
math.exp()  math.sqrt()


# library functions in python 

import math

PI = 3.14159;
result = math.sqrt(PI);
bigNumber = math.exp(PI, 10);
lisaSays = math.floor(PI); 

print("Square root of PI ", result)
print("PI to the 10th", bigNumber)
print("PI is exactly", lisaSays)

answer:  Square root of PI 1.77245
PI to the 10th 93647.3
PI is exactly 3 

# C++ library functions

#include<cmath>

const double PI = 3.14159;
double result = sqrt(PI);
double bigNumber = pow(PI, 10);
double lisaSays = floor(PI); 

cout <<"Square root of PI "<< result << endl;
cout <<"PI to the 10th" << bigNumber << endl;
cout <<"PI is exactly" << lisaSays << endl; 

answer:  Square root of PI 1.77245
PI to the 10th 93647.3
PI is exactly 3 


# set width: setw()

- use a library: #include <iomanip>
- lets you manipulate the output to display how you want

- sets the field width to be used on the display

cout << setw(5) << "LOL"  right aligned and left aligned


# set precision: setprecision()

- use a library: #include<iomanip>

double num = 123.456;
cout << fixed;
cout << setprecision(4) << num << endl; 

answer: 123.4560

# if statement

- executes when the condition is true 

```
int force;
cout << "Enter the Midichlorian level: ";
cin >> force;
if(force < 10)
{
    cout << "Jedi Hopeful"; 
}

```

```
force = input("Enter the midichlorian level: ")

if force < 10:
  print("Jedi Hopeful")

  ```

  # else 

  - executes when the condition is not true

```
int force;
cout << "Enter the Midichlorian level: ";
cin >> force;
if(force < 10){
    cout << "Jedi Hopeful"; 
}
else{
  cout << "Jedi Knight"; 
}
```

# else if 

- excutes the first true statement

int force;
cout << "Enter the Midchlorian level";
cin >> force;

if(force < 10){
  cout << "Jedi hopeful"'
}
else if(force <25){
  cout <<"Jedi Padawan"'
}
else if(force < 50){
  cout << "jedi Master;
}
else{
  cout << "Jedi Knight"
}

# IFs vs If Else

*If   - executes code for all true statements 

if(die1 == 1){
    cout << "Die 1";
}

if(die2 == 1){
  cout << "Die 2";
  }

*If else  - executes first true statement

if(die1 == 1){
    cout <<"Die 1";
}
else if(die 2 == 1){
  cout << "Die 2";
}

# boolean 

* OR   returns true if one statement is true

* AND returns true if both statements are true 

# Random Numbers

C++:
- used to create a pseudo-random number 
- use the rand() function

int value = rand() % 10; 

random number starting at 0 and goes up to 9. not including 10 

python: 
- use the randrange() function


 import random
 value = random.randrange(0, 10)


```
int r1 = rand() % 99;  //0 to 99
int r2 = rand() % 99 + 1  //1 to 100
int r3 = rand() % 99 + 50 //50 to 149
```
# srand

- 
#include <iostream>
#include <time.h>
using namespace std; 

int main(){
  srand(time(0));
  cout << rand() % 6 + 1 << endl;
  cout << rand() % 6 + 1 << endl;
  cout << rand() % 6 + 1 < < endl;
}

# Loops: Repeate segments of code 

- for loop: iterates a certain number of times
- while loop: iterates while a condition is true 

# for loop in python 
-used when you know the number of iterations

for i in range (2, 12, 3) (start, end, change)
print (i)

output: 2 ,5, 8, 11 then stops cause next iteration would be above 12

for (int i = 2; i <12 ; i += 3) (start, end condition, and increment of 3)
cout << i << endl;

same output as python 

* if have a negative vaule for change, goes down by 1
(start at 5, go down by 1, and end at 1, but not including 1)

for i in range(5, 1, -1)
print (i)

output: 5, 4, 3, 2 ..does not include the 1.
 
 * C++ 
 for (int i = 5; i > 1; i--){
  cout << i << endl; 
 }
# while loop - python

- iterates while a condition is true 

# do/while loop C++ only
- iterates while a condition is true 

- if the condition is false to begin with, it will go through the code once then stop 

- for scenarios where we need to go through loop at least one time. 

