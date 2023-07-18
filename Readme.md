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

# What is a function? 

- a way to modularize code and make it reusable

functions help us to:
* manage
* reuse
* organize

our code

# Functions in C++ 

```
void GetEmailAddress() {
  string firstName;
  string lastName;
  string emailAddress;

  cout << "Please enter your first name: ";
  cin >> firstName;
  cout << "Please enter your last name: ";
  cin >> lastName;

  emailAddress = firstName + lastName + "@gmail.com";

  cout << emailAddress << endl; 
}

int main(){
  GetEmailAddress()
  GetEmailAddress()
  GetEmailAddress()
}
```

# Functions in C++

Every C++ function should include: 
* return type
* name
* parameters
* {}

- functions in C++ need to be told which type of data to return to the user 

Common return types include:
* void - returns nothing; when using a void return type, 'return' keyword is not required in function body, but with every other return type it is required.
* int
* double
* float
* char
* classes
* memory addressses

- e.g.
int AddFive(int a){
  return a + 5;
}

* where do we keep our functions in C++? 
* do they always go before the main function? 

- if we arent defining our function above main, then a 'function prototype' is required 

a function prototype consists of:
* return type 
* name
* parameter(s)
* semicolon

e.g.  void GetEmailAddress(); 
it declares the function to the compiler

* can be placed above main
* can be placed in a header file

e.g.  #include "my_function.h"

# Header files 

- allows us to link our program to library code 
- system files - use <>
  - #include <...>
- Programmer defined files - use quotation marks instead of <>
  - #include "..."
  - .h extension

  # header files (.h)
  must have:
e.g.
  #ifndef MY_FUNCTIONS_H (if not defined) 
  #define MY_FUNCTIONS_H 

  void GetEmailAddress();

  #endif 

# Source Code Files (.cpp)

- function defintions and other code can be stored in the source file 
  - .cpp file 

  # Parameter Passing

  - pass by value
  - pass by reference

# pass by value 

  - pass by value - also known as "pass by copy'
  - modifies a copy of the variable 
  - notice b variable remains the same 
```
int AddFive(int a){
  return a = a + 5
}

int main() {
  int b = 5; 
  AddFive(b);
  cout << b << endl; 
}

//output is 5
```

  - doesn't modify the vairable, just modifies a copy of it within the function


# pass by reference

- modifies the actual variable being passed in 
- notice nothing is being returned 
- the value of b has changed

```
void AddFive(int& a){
  a = a + 5;
}

int main(){
  int b = 5;
  AddFive(b);
  cout << b << endl; 
}

//output is 10
```

- take the variable we just passed in and modify it; (not modifying a copy)  modifies the specific variable 

# default paramters 
- functions can have a default parameter
- these must be defined in the prototype

# Function Overloading

- functions can have the same name but must have different: (doesn't need to be all of these)
  - parameter data types
  - parameter count
  - return type 

e.g 
```
int AddFive(int a) {
  return 5 + a; 
}

double AddFive(double a ){
  return 5 + a; 
}
```

# scope

several types:
- global - can be accessed from anywhere in the program
- local - "block scope" anything between 2 curly braces; 
- function - same as block scope but in context of a function
- namespace - defined in a namespace; 
  - namespaces are used to contain libraries of code
  - can include into any scope by including the 'using' statement (using namespace std.)

# recursion

when a function calls itself

- requires
  - a base case that allows us to exit the function
  - a call to itself within the function
- great for problems that are too complex for the typical iterative approach 


e.g.

```
int factorial(int n){ 
  
  if(n<= 1)  //this is the base case to exit the function
    return 1;
  
  return n * factorial(n - 1)
}

```

# Objects in C++ 

C++ and other object oriented programming languages support creating user defined data types: 
  - called objects
  - a way to encapsulate and manage data
  - each object represents a noun (person, place, thing)

  # classes in C++
  the class is like a cookie cutter for our object 
   - we describe our object using a class

   notice here the class has a name and attributes: attributes are describing the student

   ```

   class Student {
    private: 
      int id:
      string name_;
      string email_; 
   }

   int main() {
    //primitive data types 
    int x;
    double y;

    //object
    Student s1; (Student is data type)
   }

   ```

- Declared in C++ using:
  * Class keyword
  * Name
  * Curly braces 
  * ;

  * can be declared in a .h file or above the main function; typically create our class in its own .h file and name the .h file the same as the class

  ```
  class Student {

  }; 

  ```

- classes have members defined within them
  - member variables
  - member functions 

  * called members because they're a member of the class

  ```
  class Student {
    int id_;
    string name_;
    string email_;

    void SetId(int id);
    void SetName(string name);
    void SetEmail(string email)
  }

//thesse are function prototypes defined in the class; this is typical to put prototypes and not definitions in our classes

```
```

- attributes and methods have visibility declarations specifications: 
* private
* public
* protected

* class visibility defaults to private if not specified  by user

```
class Student {
  private: 
    int id_;
    string name_;
    string email_;

  public: 
    void SetId(int id);
    void SetName(string name);
    void SetEmail(string email);
};
```

* every member should be designated as private or public;  (protected has to do with inheritance, we aren't working with this yet)

* these tell us who has access to the attribute or function
  - private  means only the class has access to it; if we tried to access the variable int id outside of the class, it wouldn't allow it
  
for example: in main, we've created a student object  (Student.s1 - student data type and then name (s1)); then we use the dot operator to try and 
access any of the members of the class; the member variable id is set to private, so wecan't access it in main. when working on the object outside of the class itelf, it's not gonna let us access the member variable because it's designated as private, but it would allow accewss to function SetId because it's designated as public.
```
  int main(){
    Student s1; 
    s1.id;
    s1.SetId(1357642);
  }
  ```
* typical to designate member variables as private, and member functions as public  
  * member variable id_ is inaccessible outside of the class specification while set to private 

- to access these variables and methods outside of the class we use th dot operator
  - Student s1;
  s1.SetName("Frodo"); 

  * dot connects variable name and method defined in class;  



* encapsulation - 
  - attributes are only modified by methods within their own class; 
  - this protects member variables by being accessed by outside users;
  - gives access to public methods so user can have access to private methods but in a controlled environment so they can't make changes that don't make sense

  # Constructors

  - a class constructor is a special member function of a clsss that is executed whenever we create new objects of that class
  * it is a function and it creates objects - it creates an object of that class
  * named after the class iself
  * gives our member variables value 

  main purpose is to create the object but to give our attributes or member variables values

  * notice the public method named Student has no return type

  class Student {
    private: 
      int id_;
      string name_;
      string email_; 

    public:
      Student(); // this is the constructor, a public function because we want users of our class to be able to create studen objects 
      //no return type  - every constructor will only return one thing. an object of the class that its constructing  (a student contructor would return a newly constructed student object)

      * prototype shown in the class

      class Student {
        private: 
          string name_;
          string email_;
          int id_;

        public:  //this is the prototype 
          Student();
      }

      * used in main function
      int main () {
        Student s1; // this calls the above prototype, calls the constructor, creates a new object (put class name and then name of variable)  
      }

  }

- several kinds of constructors can be defined.  
  2 we are talking about: 
    - default
    - general 

    # default constructor 

    - creates an empty object 
      - sets numeric values to 0 
      - sets character/string values to blank 
      - sets objects to empty 

      * notice constructor is written outside of class

      e.g. of a default constructor written outside of the class; 

      Student::Student() {
        id_ = 0;
        name_ = "";
        email_ = ""; 
      }


* default constructor creates an empty object
      - can be written inline using initializer list (inline means we can keep it in our class) 
      - very common way to make a default constructor; just creating an empty object
      - makes it so we don't need to define it in 2 places
      - should only be defined in one place  
      - a little bit different than a prototype 

      * notice {} at the end of the list in example 

      class Student {
        private:
          int id_; 
          std::string name_;
          std::string email_;

        public: 
          Student() : id_(0), name_(""), email_(""){}  
          //initializer list;
          //this is defining the method; 
          //the curly braces represent the body of the function;
          //instead of using the = sign assignment operator, we put the values in parentheses.   
      }

      # General Constructor 

      - creates an object with user chosen values given to the member variables; 
      * notice the constructor has parameters

* a common way to identify member variables is by putting an underscore after the name
* good way to differentiate from other variables that might have the same name
* member variable will always have the underscore; 

* defined outside of the class; scoping it back to student class
    Student::Student(int id, std::string name, std::string email) {
      id_ = id; (id_ = our passed in id)
      name_ = name; (name_ = our passed in name)
      email_ = email; etc. 
    }

    * gives our object values that the user has decided on

    * can also be written inline using initializer list 
    * should only be defined in one place 

    * notice parameters used in () for each variable at the end of the list  

    public:
      Student(int id, std::string name, std::string email) : id_(id), name_(name), email_(email) {}

      * can use an inline initializer as long as you don't care what the values are; (like example above. )

      # Using Constructors  

      * default does not need ()
      * to call general add() and values 

      int main () {
        //default - making an empty object
        Student s1;

        //general - giving our object some values
        Student s2(135246, "John Smith", "johnsmith@gmail.com")
      }

# initializer lists 

- constructors can be written inline as an initializer list
- can set values using () rather than =
empty {}

public: 

  Student(int id, std::string name, std::string email) : id_(id), name_(name), email_(email) {}
* giving attributes values 
* cannot be in the .cpp file must be in the class specification file  

# defining class member functions

- class declarations only hold function prototypes; the actual definition is placed somewhere else

- good programming practice says that our function definitions will need to be written outside of the class

* considered OK to keep very small functions in the class declaration

class Student {
  private: 
    int id_;
    string name_; 
    string email_; 

  public:
    void SetId(int id);
    void SetName(string name);
    void SetEmail(string email);
};

- commonly, the class definition is kept within the header (.h) file 

- the class methods are kept in the source code (.cpp) file
    - class member functions are kept within this file
    - name it the same as the class



observe the following .cpp file for our Student class

//links us back to the class specification; 
#include "Student.h"


//scoping this function back to the class; this function belongs to the Student class; and then we 
are adding our definition
void Student::SetName(std::string name){
    name_ = name;
}

void Student::SetId(int id) {
  id_ = id; 
}

void Student::SetEmail(std::string email) {
  email_ = email;
}

# defining a class in a header file 

- header file requires header guards 

- these are ususally generated by the IDE 

- need to include the string class to use string  objects in class

e.g.

#ifndef STUDENT_H
#define STUDENT_H 

#include<string>

class Student {
  private: 
    int id_;
    std::string name_;
    std::string email_;

  public: 
    void SetId(int id);
    void SetName(std::string name);
    void SetEmail(std::string email);
};
#endif

# Member functions 

- should have the following functions in each class 
* constructors
* destructor 
* setters
* getters 

class Student {

  private: 
    int id_;
    std::string name;
    std::string email;

  public:
    //constructors
    Student() : id_(0), name_(""), email_("") {}
    Student(int id, std::string name, std::string email) : id_(id), name_(name), email_(email) {}

    //setters -set all our attribute values
    void SetId(int id);
    void SetName(std::string name);
    void SetEmail(std::string email);    

    //Getters - get the values in order to display them to user
    int GetId() const {return id_;}
    std::string GetName() const { return name_; }
    std::string GetEmail() const {return email_;}
};

# Constructors

- give the user a way to create an object of that type of class

* can be written inline using initialize tests
* can be written outside of class 

- Student() : id_(0), name_(""), email_("") {}
    
- Student(int id, std::string name, std::string email) : id_(id), name_(name), email_(email) {}

# Setters 

- a way to control how values are set and protect member variables  

//Setters 

    void SetId(int id);
    void SetName(std::string name);
    void SetEmail(std::string email);  

some examples of setters: 
  - makes sure the user cannot enter an address without the @ character

  void Student::SetEmail (std::string email) {
    if(email.find('@')!= std::string::npos)
      email_ = email;
    else
      std::cerr << "Invalid email address" << std::endl;  }

  # Getters 

  - a way for the user of the class to see the values without having direct access to them

      - can usually be written in class specification
      - written as const since these functions are written only view the values, not to modify them 

  example: 

  //Getters - sometimes they don't want to modify it, they just want to view it. in this case, use a getter 

  int GetId() const { return _id; }
  std::string GetName() const { return name_ };
  std::string GetEmail() const { return email_ }; 

# Destructors 

- special member functions in C++ that are meant to destroy objects when they go out of scope 

//destructor 
whenever we create an object, we also want to destroy it. important in the process of managing memory

~Student() {}

- has the same name as class name preceded by a ~ symbol
- not possible to define more than one
- does not require arguments
- does not return any value
- automatically called when object goes out of scope 

* they release memory space occupied by teh objects created by constructor 

# structs

- structures are a way to group several related variables into one place

- can be used almost exactly the same way as a class

struct Assignment {
  string name_;
  int points_; 
};

- class has default visibility setting as: private 
- struct has default visibility setting as : public 

 - can have methods just like a c ++ class

 struct Assignment {
  string name_;
  int points_;

  Assignment() : name_(""), points_(0) {}
 }; 

 in main...
 notice we have access to the member variables 
 - structs have default visibility of public 

 Assignment a1:
  a1.name_ = "Learning Activity: classes & objects";
  a1.points_ = 10;
  cout << a1.name_ << endl; 
  cout << a1.points_ << endl; 

  - structs are a way to group several related variables into one place

  - can be used almost exactly the same way as a class

  struct declaration:
  struct
  {
      string name_;
      int points_;
  } assignment1;

  used in main: 
  assignment1.name_ = "Learning Activity";
  assignment1.points_ = 10; 

  # OVERLOADED OPERATORS 

  overloaded function - a function that has the same name as another function 

  - different parameters 
    - different number of parameters 
    - different data types
    - etc 
```
    void Print(){
      cout << "My name is Sam!" << endl; 

    }

    void Print(string name){
      cout << "My name is " << name << "!" << endl; 
    }

    int main() {
      Print();
      Print("Joe")
    }
```
* loading the same function name with different meanings 

# Overloaded Operators 

- in C++, we can redefine operators to work for our classes 

- we can change what it means when we use these symbols in our code 

- operators are naturally used with primitive data types 

why redefine any operators? 
we cannot use operators in our code for objects until they are defined  

Box a;
Box b;
Box c = a + b

* overloading an operator is simply writing a function with specialized syntax

- different kinds of operators will use different syntax

* binary 
  - a + b  (2 operands L and R)
  - a - b 
  - a && b
  - a != b 

  * unary 
  - a++
  - ++a
  - -a 

  ```
  //binary
  Box a(1, 1, 2);
  Box b(1, 1, 2);
  Box c = a + b;

//unary
Box f(4, 4, 4);
-f 
  

  - 2 strategies for overloading operators

  - written as member functions, as members of our class
    - as a member of a class
    

    - written as friend functions
      - as a friend of a class

  - member functions
    - binary 
    - unary

  - friend functions
    -binary
    - unary

# Member functions - Binary

- syntax for overloading binary operators as class member functions
- binary meaning 2 operands 

//binary
Box a(1, 1, 2);
Box b(1, 1, 2);
Box c = a + b; 


 * Example Box class

 Manages member variables
    - length_
    - width_
    - height_

    class Box {
      private:
        double length_;
        double width_;
        double height_;

      public:
        //default and general constructor
        Box():length_(0), width_(0), height(0) {}

        Box(double length, double width, double height) : length_(length), width_(width), height_(height) {}

        //Setters
        void SetLength(double);
        void SetWidth(double);
        void SetHeight(double);

        //Getters
        double GetLenght() const { return length_;}
        double GetWidth() const { return width_;}
        double GetHeight() const {return height_;}
        double GetVolume() const{
          return length_ * width_ * height_; 
        }    };

         * need to be able to add up all the boxes in order to calculate the total volume 
          * 1. specify prototype in class
          * 2. use operator keyword
          * 3. and + sign 

      * notice the function and parameter has been set to "read only" by using const 

      //overloaded operators
      //below is the prototype
      // we are returning a 'Box' object
      // we are using a reference to a Box object as our parameter
      //set to const because it's read only. we aren't going to modify any of the variables 

      Box operator+(Box const &rhs) const; 
-  the overloaded operator above would be defined in our source file
- scope the operator+ back to class
- add up calling object and parameter's member variables 

* notice we have access to two object's member variables. the calling object and the rhs parameter
``````
Box Box::operator+(Box const &rhs) const {
  Box temp;

  temp.length_ = length + rhs.length_;
  temp.height_ = height_ + rhs.height_;
  temp.width_ = width_ + rhs.width_;

  return temp; 
}

 Person p;
 p.Print("Joe");
 p.Print where p is implicit
 and ("Joe") is an explicit argument; 
``````
 - implicit argument is on the left-hand side; the implicit is the one calling the operator

 - explicit argument is on the right hand side; the explicit argument is what we are passing in as a parameter to our function
``````
 Box x; 
 Box y;
 Box z = x + y; 
 //could be written 
 z = x.operator+(y)

 //overloaded operators
 Box operator+(Box const &rhs) const; 

``````
# Unary

- syntax for an overloaded unary operator
- only the implicit argument is required here 

.h file -> Box operator-(); 

.cpp file ->   
Box Box::operator-(){
  return Box(-length_, -width_, -height_);
}

main -> 
//unary
Box f(4,4, 4);
-f; 

# friend functions - binary 
- not members of the class
- but still given access to the private member variables

* use keyword friend in prototype
* no special syntax in definition
* no implicit argument
* binary uses two parameters
* unary use one parameter

* like a good friend that you give a key t your home 

//friend functions
friend Box operator+(Box const &lhs, Box const &rhs);
``````
Box operator+(Box const &lhs, Box const &rhs){
  double length = lhs.length_ + rhs.length_;
  double width = lhs.width_ + rhs.width_;
  double height = lhs.height_ + rhs.height;

  return Box(lenght, width, height); 
}

``````
* no keyword friend and not scoped back to class because it's not a member variable

why use a friend function?
- what ifi want to use the left operand for the integer and the right for the box object?  
Box a(1, 1, 2);
Box c = 5 + a; 
5.operator+(a) is not legal; 
won't compile 

so a friend fucntion will help us do this:
friend Box operator+(double number, Box const &rhs); 
//friend keyword, 
//returning a box object,
// operator keyword and plus sign, 
//Left hand parameter we are passing in a number, 
//right hand parameter we are passing in a box, 

# Overloaded insertion operator << 

- we may want to use the iostream class to print our objects 
``````
//common
int d = 5;
cout << d << endl; 
``````
//must overload the << operator because it won't automatically work with user-defined classes

``````
//we do this by overloading the insertion opeerator
Box a(1, 1, 2)
cout << a << endl; 
``````
- overloeading the inserter operator has special syntax for the function header

* must be a friend
* must return a reference to an ostream object
* must pass in a reference to an ostream object
* must pass in a reference to the class

* friend std::ostream& operator<<(std::ostream& os, Box &box)
 binary - has an operand on the L which is the cout object and and an operand on the R, whatever object we want to put into our ostream object (in the case above, we are overloading it for our box class);

 * can customize how the member variables are printed 

 - must use <<  to stream in output to ostream object 
 - must return the ostream object


``````
std::ostream& operator<<(std::ostream &os, Box &box){
  os << "Length: " << box.length_ << "Width: " << box.width_ << "Height: " << box.height_ << std::endl; 

  return os; //returning a reference to an ostream object
}

``````
# overloaded extraction operator >>

- similiar to insertion operator
- uses istream class 



