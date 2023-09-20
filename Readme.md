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

# try/catch in C++
``````
try {
  //block of code to try
}
catch() {
  //block of code to handle errors 
}

``````

# throw statement 

``````
//basic if statement
string CreateCheckingAccount(int age) {
  if(age > 17)
    return "Your account has been created.";
  else
    throw "error";
}

``````
//simple try/catch

```
int main() {
  try {
    CreateCheckingAccount(17);
  }
  catch(...) {
    count << "Does not reach age requirements." << endl; 
  }

}
```
- try/catch  have our throw. any generic throw. as long as (...) if a throw happens within the try block, it will do wahtever the catch block  has inside it. 

- can also use an intger in place of throw 
  - good if you have some kind of error codes in system and based off what the error was, use a particular code to handle it 
``````
  //try/catch with integer instead of ellipses

  try {
    CreateCheckingAccount(17);
  }

  catch(int errorCode){
    cout << "Error: " << errorCode << endl;
    cout << "Age requirement not met." << endl;
  }
  catch(...){
    cout << "Must be 18 or older." <<  endl; 
  }
  
  ``````
  * output Error: 515
  Age requirement not met. 

  # characters 

  the char data type is for a single character

  char letter = 'a';
  string letters = "apple"; 

  # special characters

  - \n - end line characters
  - \t - spaces the text out by a tab
  - \0 - null or no value
  - \' - allows you to put a single quote in a string
  - \" - allows you to put a double quote in a string
  - \\ - allows you to put a backlash in a string 

  # single vs double quotes

  - single quotes for a single characer
  - double quotes for multiple characters 


# upper and lower case

- makes a character to be upper or lower case 

* toupper(): makes the character uppercase
* tolower(): makes the character lowercase 
``````
char letter = 'a'; 
letter = toupper(letter);
cout << letter; 
``````
 # checking for case 

 - determines if a letter is upper or lower case 
 * isupper() checks for an uppercase letter
 * islower() checks for lower case letter

 ```
 char letter = 'a';
 if(islower(letter)) {
  cout << "lowercase";
 }
 ```
 # additional functions

 determines different characteristics about a character
 * isdigit() determines if the character is a number character
 * isalpha() determines if the character is a-z or A-Z
 ispunct() determines if the character is punctuation
``````
 char letter = '!';
 if(ispunct(letter)){
  cout << "punctuation"; 
 }

 ``````

 # what are c strings?

 - an array of characters
 - terminates with a null character

 char name[10] = "Weber";
 W - e - b - e - r \0 (indicates end of string)
 so even though it can be 10 charactetrs long it only displays up to null terminator
but space is still allocated up to 10 spaces for a char


# literal c-strings

- array of characters
- terminates with a null character

char name[] = "Weber"; 

square brackets and no specified size; will create characgter array with enough characters that it needs including the null terminator 

# getting input for c-strings

```
char name [5];
cin >> name: //enter weber 

```
if i enter a word longer than allocated , then it will create an error 

often enter in a value that's bigger so there is extra room in case the user enters something larger

# cout statement 

```
 char name [20];
 cin >> name;
 cout << name; 

 ```

 # c-string functions

 #include <cstring>
must be included in order to use the functions;
- strlen()
- strcpy()
- strcmp()
- strcat()
# length of a c-string
- finds the length of a cstring

```
char cstr[21] = "hello";
int len = strlen(cstr);
cout << len; 

//output: 5 
```
# copy a c-string

* cannot copy using = 

```
char cstr[21] = "hello";
char full[] = cstr;
cout << full; 

```
error: array initilizer must be an initializer list or string literal 
 - character array of size 20
 - it won't let me copy the "hello" because cstr is not a string literal even though it's set = to the same value 

 instead:

 Strcpy: copies a string
 ```
 char cstr[21] = "hello";
 char full[21];
 strcpy(full, cstr);
 cout << full; 

 //output hello 
 ```
- cstr is now stored in my variable full - using strcpy(full, cstr); 


# compare strings

- the strcmp() function alllows you to compare strings

```
char cstr1 [] = "Apple";
char cstr2 [] = "Banana";

if(strcmp(cstr1, cstr2) <= 0) {
  cout << cstr1 << "is less than" << cstr2; 
}

//output "apple is less than banana"
//compare the first letter of each A and B and A is less than B based on ASCII value 

```

# concatenate strings

- the strcat function chains c-strings together

```
char cstr [21] = "hello";
strcat(cstr, "world");
cout << cstr; 

//output Hello World 

```

# concatenate c-strings

- the strcat function chains c-strings together

```
char cstr [21] = "hello";
strcat(cstr, "world");
cout << cstr; 

```

# iterating a c-string

- use the [] to access a position in the c-string

```
char cstr [21] = "hello";
for(int i = 0; i < strlen(cstr); i++) {
  cstr[i] = toupper(cstr[i]);
}
cout << cstr; 

//output HELLO
 
 ```

 # std::strings


- define a string

```
string s1("Man");
string s2 = "Beast";
string s3; 

s3 = s1; 

```

- two strings can be made into one string using the + concatentation operator: 


``````
s3 += " and " + s2; 
``````

# string input 

- cin retrieves to a space  
string name;
cin >> name;

- getline retrieves to a new line (enter)
string name;
getline(cin, name);

# issues with getline

the cin command does not read the endl character

so to fix it: 

string sentence;
cout << "Enter number: ";
cin >> number;
cout << "Enter sentence: ";
cin.ignore();
getline(cin, sentence);

cout << "Values: " << 


*enter number: 5
Ignore: <enter>
Enter sentence: Hello World

so anytime you have a cin statement, ignore the "enter" before you do a getline statement

# Length or Size 

- find the size or length of the string
- both commands do the same thing

```
string str "hello";
cout << str.size();  //5
cout << str.length(); //5


```

# CONCATENATING 

- chaining together strings

use + or += 
```
string str = "hello";
str += " ";
string full = str + "World";
cout << full; 

//output hello World 

```

# concatenating with numbers 

- chaining together strings and numbers 
- gives an error
``````
string str = "life the universe and everything";
int value = 42;
string full = str + value; 
cout << full;
``````
//output error


# comparing

- same as values 

```
string str1 = "Apple";
string str2 = "Banana";
if(str1 < str2) {
  cout << "A is smaller than B";
}

//output A is smaller than B
```

# Comparing Case

- lower case values are bigger than upper case 

```
string str1 = "Apple";
string str2 = "Banana";
if(str1 > str2) {
  cout << "b is larger than A";
}

//output b is larger than A 
```

# find 

- returns the position of the search item 

```
string str = "Mississippi";
int pos = str.find("iss");
cout << pos << endl; 

//output 1 

```

- suppose you wanted to find the next 'iss' in mississippi

``````
string str = "Mississippi";
int pos = str.find("iss");
pos = str.find("iss", pos + 1);
cout << pos << endl; 

//output 5 
``````

start search at 2..and find 'iss' at character 5 

# find 

- no position string::npos
- want to see if something is not found; 

in example, looking for x in mississippi 

```
string str = "Mississippi";
int pos = str.find("x");
if(pos == string::npos){
  cout << "x not found"; 
}

//output x not found
```

# substring

- returns a portion of the string to the end of the string
- allow you to limit the size of your string

```
string str = "Weber state";
int space1 = str.find(" ");
string school = str.substr(space1);
cout << school; 

//output State

```
so gives the portion of the string specified, starting at whatever pos is passed in

- if given 2 positions (0, space) it will give a start and an ending, not inclusive 

# iterating over strings

- iterate over the characters of a string

```
for(int i = 0; i < str.length(); i++) {
  cout << str.at(i)<< endl; 
  cout << str[i] << endl; 
}

```

# iterating: At vs []

- At - preferred if wanting read-only
``````
string str = "abc";
cout << str.at(99);
``````
- will result in an error

VS.

operator[]

```
string str = "abc"; 
cout << str[99]; 


```

- this is allowed but will display random junk; whatever is at the position 

# C-strings vs std::strings

C-string
Pros
* fixed length 
* primitive data type 

Cons
* watch out for out of bounds

 Std:string
 Pros
 * more intuitive to use
 * checks for out of bounds  

 # stringstream

 #include <sstream>

 an object used to ...
 * add strings, objects, and values into a stream
 * parse streams and strings into values 

 # Converting to a string

 - use the << sign to add to the stringstream 

 - .str() function converts the stream to a string 

 ```
 //declared stringstream with sout
 stringstream sout;
 sout << "Add Word "; 
 sout << 42 << " " << 3.1415;
 string mystring = sout.str();

 //output Add Words 42 3.1415
 
 ```


# Parsing using stringstream

- you can use the stringstream to parse a string

```
string str = "one two three four";
stringstream sout(str);

string temp;
while(sout >> temp) {
  cout << temp << endl; 
}

//output one  
          two 
          three 
          four 
//1st loop is one
//next time through loop is two
//because it goes up to the space 

```
can also: 

```
string str = "one two three four"
stringstream sout; 
sout << str;
string temp; 
while(sout >> temp) {
  cout << temp << endl; 
}

```

# File I/O

#include <fstream>

3 classes 
* fstream: input/output
* ifstream: input
* ofstream: output 

# File types 

- can write to Text files 
* open with text editor
* .txt .csv, .cpp, .java, .html, and more

- or can write to Binary  files 
* everything else 
* opened with specialized programs
* .exe, .png, .zip, .mp3

# file access

- random access; 

- sequential access;

- random access file analogy

  - tennis box full of balls; can reach in and grab any ball

  vs.
   - sequential access analogy 
    - 3 tennis balls in tube and to access the one at the bottom, you must remove the balls above it

    # writing to a file 

    - #include<fstream>

    ifstream: reading in from a file

    ofstream: writing out to a file 

    # file output with standard dictionary

    to write to it, you need to open it
    
    - if using namespace std;
    OR
    - using std::ofstream;
      using std::out;  

    ```
    ofstream fout; 
    fout.open("hello.txt", ios::out);
    
    ```

# file output inline 

- if not using namespace std; 
- maybe in a .h file

```
std::ofstream fout;
fout.open("hello.txt", std::ios::out); 

```

- many compilers create the file in the same directory

- CLion, however, creates it in the cmake-build-debug folder so you must go up a directory using 
  *  ../

  ```
  ofstream fout;
  fout.open("../hello.txt", ios::out);

  
  ```

  # file output

  - in CLion using projects with test cases it's even 1 folder deeper so use:
    * ../../hello.txt

    # file output 

    - declare and open file in same line of code
    ```
    ofstream fout("hello.txt", ios::out);
    
    ```

    - writing to the file is just like a cout statement, but we use the name of our stream (fout)

    ```
    ofstream fout;

    //opens the file
    fout.open("../hello.txt", ios::out);
//writes hello world to the file
    fout << "Hello World";
//closes the file 
    fout.close(); 
    
    ```

* the ios::out says to write to the file and overwrite whatever is there; what was previously there will be deleted and replaced 

* this can be changed by ios::app
 - it will add it to the end instead of deleting what is there

 - append a file: just add to the file instead of overwrite it

 # open a file for reading

 - ifstream: reads from a file 

ifstream fin("numbers.txt", ios::in); 

in CLion:

ifstream fin("../numbers.txt", ios::in); 

 if not in main:

 std::ifstream fin("numbers.txt", std::ios::in); 

 # checking that a file opened

 .good() determines if it's a valid stream

 - before we can read from it, need to make sure the file exists

 ```
 ifstream fin("numbers.txt", ios::in);
 if(!fin.good()){
  cout << "could not find the file";
  return 0; 
 }
 
 ```

# Reading word from a file 

- read using the >> operator 

- like  a cin statemen (fin)



```
ifstream fin("numbers.txt", ios::in);
if(!fin.good()){
  cout << "could not find file" ; 
  return 0; 
}
string word;

//reads whatever's in the file, then stores it to variable called word
fin >> word; 
 fin.close();


```

# reading line from a file:  <<

- read using the >> operator 

* >> reads up to a space so to read a whole line, we use getline()
``````
ifstream fin("numbers.txt", ios::in);
if(!fin.good()){
  cout << "could not find file" ; 
  return 0; 
}
string line;
getline(fin, line);

fin.close()
``````

# reading until eof()

- eof() finds the end of the file 



```
string word;
//as long as it's not the end of the file
while(!fin.eof()){
  //its gonna read in the word and print it out to the screen 
  fin >> word;
  cout >> word >> endl; 
}

fin.close(); 

```

# Reading line from a file: getline()

- getline returns false if nothing is read 

- eof() finds the end of the file 

```
string line; 
//as long as i'm reading information from the getline(), print it out
while(getline(fin, line)) {
  cout << line << endl; 
}

fin.close(); 

```
# reading: Mac vs PC

* add a specification on what characters you will ignore 
``````
string line;

int number;

while(getline(fin, line)) {
  //on mac, if you find a /r in your ine because ignore character is not reading in /r, then just erase that last character
      if(line.find('\r') != line.npos)
        line.erase(line.size() -1);
      fin >> number; 

  //on pc, ignore 2 characters all the way up to the \n
      fin.ignore(2, '\n');

  cout << line << endl;
  cout << number << endl; 
}

``````

# Arrays 

# static arrays

- why an array?

- collection of items
- same data type
- same name 

string person1;
string person2;
string person3;

# declare an array

```
int oddNumbers [100];
double grades[10];
string tweets[200]; 

```

# initializer list 

- declare an array with values defined 

```
string students[4] = {"Jenny", "Joe", "Paul", "Fred"};

int primes[4] = {2, 3, 5, 7};

//set or change position 0 of primes to 4
primes[0] = 4; 

//allow the user to enter in the value for primes position 2
cin >> primes[1];

```

# iterating over array elements

- use a loop to iterate over the elements of an array 
``````
const int DAYS = 7; 
string days[DAYS] = {"sun", "mon", "tue", "wed", "thu", "fri", "sat"}

for(int i = 0; i < DAYS; i++){
  cout <<"Day: " << days[i] << endl; 
  }
``````


# finding size 

- use sizeof function to find the size of the array

```
string days[] = {"sun", "mon", "tue", "wed", "thu", "fri", "sat"};

int size = sizeof(days) / sizeof(string);
for(int i = 0; i < size; i++) {
  cout << "Day: " << days[i] << endl; 
}

```

# iterating using a range for loop

- use a loop to iterate over the elements of an array 
``````
const in DAYS = 7;
string days[DAYS] = {"sun", "mon", "tue", "wed", "thu", "fri", "sat"};

for(string i: days){
  cout << "Day: " << i << endl; 
}
``````
 - i becomes the string itself.  

- but you cannot modify i. it's just a copy of the value from the list; 

- if we want to modify it... we can use 

```
for(auto &&i: days)
  i = "holiday"; 

```
- && make i the actual address of where the info is stored in the list 

- so above code would change all of sun mon tues wed, etc  to holiday. 

# passing array to functions
- when you pass an array to a function, you're actually passing the memory location of where it is stored

```
#include <iostream>

using namespace std;

//passing an array num to a function change
void change(int num[]){
  num[0] = 42; 
}

int main() {
  cout << "Array Practice!\n";
  int num[] = {1, 2, 3, 4};
  cout << "Position 1 Before change() " num[0] << endl; 
  change(num);
  cout << "position 1 after change() " << num [0] << endl; 
}

```
* it doesn't make a copy. it actually passes the data itself so any change made in a function will be changed back in main, as well. 

* it retains the changes from the function

# Array of objects

- array may contain more than primitive data

- each position in array contains both x and y


```
Point triange[] = {
  Point(1,1),
  Point(5, 1),
  Point(3, 4) 
};



```

* must have default constructor  
- it will assume all th values in triangle are empty until i've specified an amount 

```
Point triangle[3];
triangle[0] = Point[1, 3];

```


```
class Point 
{
  public: 
  Point () : x(0), y(0) {}
  Point(int x, int y) : x(x), y(y) {}
  int GetX() {return x;}
  int GetY() {return y; }

private:
int x, y;


};

```

# access methods

cout << triangle[0].GetX(); 
cout << triangle[1].GetY(); 

# Array of struct

- array may contain more than primitive data
- each position in array contains both x and y 

```
struct Point
{
  int x, y; 
}

Point triangle[]  = {{1,1}, {5, 1}, {3,4}}

```

- has no problem defining an array 

Point triangle[3];
triangle[0] = {1, 3};

# access methods
- easy to use because don't have to spend the time to code entire class
- instead of using Get() can use dot operator

```
cout << triangle[0].x; 
cout << triangle[1].x; 

```

# 2-D array

- a table with rows and columns
usu. row first, column second

# 2d array initialization

int numbers[3][4]= {
  {11, 13, 9, 12}, 
  {3, 5, 21, 10}, 
  {17, 15, 32 ,4}
}; 

# iterating over a 2d array

- need to use 2 loops: 

char tactoe[ROWS][COLS] = {
  {'X', ' ', 'O'},
   {'O', 'O', 'X'},
    {' ', 'X', ' '}
}

for(int r = 0; r < ROWS; r++) {
  for(int c=0; c < COLS; c++) {
    cout << tactoe[r][c] << "|"; 
  }

  cout << endl << " ______________" << endl;
}

# multiple dimensions

- you can have more than 2 dimensions in an array

int cube [3][3][3];

cube[0][1][2] = 5;
cout << cube[0][1][2] << endl; 

# Containers

# Standard Template Library

containers: stores a collection of other objects
Algorithms: collection of functions
Integrators and lambdas: allows you to specify the data in your algorithm 
# array

array
Vector
Set
Map
Stack
Queue

different ways of storing data

# std::Array

fixed size list of any value 

Declaration
```

#include<array>

Array<data_type,  array_size> array_name;

```

Example

```

Array<string, 200>names; 



```
# Array: Instantiating

Iterate through and set each item: 

```

Array<int, 5>myList; 

	For(int i = 0; i < 5; I++) {

			MyArray[i] = i; }

```

OR -
//Initializer list
Array<int, 5>myList = {5, 2, 1, 3, 4}

# Array: iterating by index 

Size: size() determines the number of elements 

# Access each element

	* operator[] access each element 

	* .at() function 

```

For(int i = 0; i < myArray.size(); i++){

	Count << myArray.at(i) << “ “; 

}



```

# Array: iterating entire array 

iterates the entire list 
i becomes a copy of each element 


Array<int, 5>myArray = {5, 4, 3, 2, 1};

For(auto i : myArray){



}



i. Cannot be modified. It’s just a copy of the data; but if a double reference is added, then the data can be modified 
	

Array<int, 5>myArray = {5, 4, 3, 2, 1};

For(auto &&i : myArray){

	Cout << i << “ “; 

		i++

}

Values would be 6, 5, 4, 3, 2 

# std::Array iterator

begin() returns the start

end() returns the end

Pointer to accesss location


For (auto it = lst.begin(); it != lst.end(); ++it) {

	Cout << *it << “ “; 

}


lst.begin
Iterate through through until we hit the end


Pointer means i have the address location. The * means shows me the data instead of the address location 

# Vector

Similar to an array; with exception - size

It’s a resizeable array


#include <vector>

Void push_back(toAdd)

Begin() returns a pointer to the start

End() returns a pointer to the end 

Size() returns number of elements

Overloaded [] to access each element 

At() 


# vector: instantiating

Vector<int>myList; don’t have to specify the size 


//initial size of the list is 100

Vector<int>myVector(100); 

# Vector: Adding

adds an item to the end of the list 
Void push_back(item)


For(int i = 0; i < 5; i++) {

	MyVector.push_back(i);

}

Creating a loop that goes from 0 to 4 and pushing the items on the back of list, so list will be 0 1 2 3 4 

List is sized accordingly. 

#Vector: Iterating 

.size() determines the number of elements 

Operator[] access each element

.at() access the element at that position

For(int i = 0; i < myList.size(); i++){

	Cout << myVector.at(i) << “ “; 

}


Above way is iterating by index value


Another way is to iterate the entire array


For(auto &&i : myList){

	Cout << i << “ “; 

}

The ampersands will change the particular value in the list; without them will not change 

# Vector: using auto

Use an iterator. It is a pointer to the value


For(auto i = myList.begin(); i != myList.end(); i++) {

Cout << *(i) << “ “; 


So this is another way of iterating through except now we have a pointer to the memory address instead of getting just the data; 



The * specifies that we want to view that data at the memory address instead of just the memory address being displayed

# Vector advantages and disadvantages compared to arrays

advantages - 

direct access to data
- memory management is done for you
Disadvantages 

add to end less efficient if always adding values
Extra memory allocated for list items not in list 

# Set 

resizable container 
- must contain unique values
Cannot access individual elements

#include<set>

void insert(toAdd)

begin() returns pointer to the start

end() returns pointer to the end

size() return number of elements 

# set: instantiate


Set<int>myList;

//size of the list is 3

Set<int>myList = {1, 2, 2, 3, 4};

# set: adding 

adds an item to the set
Void insert(item)
Duplicate items will not be added

For(int i = 0; i <5; i++) {

	MyVector.insert(i); 

}



# iterate through a set: for each loop

iterates the entire set 

For(auto i : myList) {

	Cout << i << “ “; 

}

This will iterate from beginning to end and print out each of the items in the list 

# set: using iterator 

use an iterator. It’s a pointer to the value

For(auto i = myList.begin(); i != myList.end(); i++) {

		Cout << *(i) << “ “; 

}

# other containers


# stack 

last in first out (LIFO)
Like a stack of trays 
No access to middle or end values 


stack data structures are useful when the order is important. They ensure that a system does not move onto a new action before completing those before 
Example: undo option 

# stack 

``````
#include<stack>

stack<int>myStack;
std::stack<string> strStack;

``````

- void push(toAdd) adds to the top
- pop() deletes the top
- empty() returns true if the stack is empty
- size() return number of elements
- top() returns the top value 

```
stack<int>myList;
myList.push(10);

```
put '10' onto my stack. will be the item at the top of the stack 

```
myList.push(42);
myList.push(4);

myList.top();
// output: 4

```
result:   (4, 42, 10) each new push is on the top of the stack 

# queue 

First in First Out - waiting in line at disneyland

- no access to middle values 
- every time we add we add to the end of the line; every time we remove we remove from the front of the line

#include <queue>

# queue usage 

when to use a queue?  when the order of actions is important. 

it ensures that actions are performed in order

* example : printer queue

5 people want to print an item; 
whoever prints first gets stored into the queue;
then the next person. when printer is handling jobs, it starts with the first inthe queue


# queue

#include<queue>

queue<int>myQueue;
std::queue<double>dblQueue; 

- void push(toAdd) adds to the back
- npop() deletes from the front
- empty() returns true if the stack is empty
- size() return number of elements 
- front(), back(), returns the front/back value


# Map - data structure


- key/value pairs
- same as dictionary in python
- search for item by the key

#include<map>

- void insert({key, value})
- erase() removes by key
- empty() returns true if the map is empty
- size() return number of elements
[key] :Key returns the value 


example: insert using key value pairs
``````
map<string, int>myMap;
myMap.insert({"Weber State", 21});
myMap.insert({"Utah State", 37});
myMap.insert({"BYU", 14});

``````


# map access by key 
map<string, int>myMap;
myMap.insert({"Weber State", 21});
myMap.insert({"Utah State", 37});
myMap.insert({"BYU", 14});

cout << myMap["Weber State"];  //21
myMap.erase("Utah State"); //takes out utah state from list 


# iterate

- first is the key
- second is the value 
``````
for(auto i : myMap) {
  cout << i.first << " " << i.second << endl;
}
``````
# modify values 

- may modify value
- cannot modify key

```
for(auto &&i : myMap) {
  i.second ++; 
}

```

# what are iterators

- pointers to the container
- used with algorithms 
  - .begin() gives beginnign of list
  - .end() gives end of list

- access the ends of the list 

```

array<int, 4> myArr = {2, 4, 6, 8};

cout << *myArr.begin();
cout << *myArr.end();

```

*   star means it's going to reference the data int he pointer, not that it's accessing the pointer itself

# what are iterators

- can iterate with iterators

array<int, 5> myArr = {5, 2, 1, 7, 9};

for(auto i = myArr.begin(); i != myArr.end(); ++i) {
  cout << *i << " "; 
}

- iterator needs to be ++i, not i++

# used with algorithms 

sort(myArr.begin(), myArr.end());

sort entire array from beginnning to end

# algorithms

- count
- count_if
- find
- find_if
- sort 
- min
- max


# sort 

- used with algorithms

```
array<int, 4> myArr = {5, 4, 2, 9, 1}
sort(myArr.begin(), myArr.end());
1, 2, 4, 5,9

```

# sort descending

sort(myArr.begin(), myArr.end(), greater<>());

9 5 4 2 1 

# count

- finds the number of elements in a list 

array<int, 10> myArr = {2, 2, 2, 2, 4, 6, 8, 10, 6, 2}

int cnt = count(myArr.begin(), myArr.end(), 2); 
cout << cnt << endl; 

//output: 5 

# find 

- finds the position of the item in the list 

- this is a pointer, not the value
- will retrieve a pointer to wherever teh item is in the list

array<int, 10> myArr = {2, 4, 6, 2, 4, 6, 8, 10, 6, 2};
auto it = find{myArr.begin(), myArr.end(), 4};
if(it == myArr.end()){

  cout<< "Item not found"; 
}else
{
  cout << *it << "is found in the list"; 
}

//output: 4 is found in the list 

# Max 

- finds the largest element: max_element()
- finds the smallest element: min_element()

array<int, 10> myArr = {2, 4, 6, 2, 4, 6, 8, 10, 6, 2};
auto mx = max_element(myArr.begin(), myArr.end()); 
cout << *mx << endl;
(it's a pointer to the object, not the object itself so the * is used to get the data )


# Lambda

- variable that acts like a function
- short snippets of code
- not reuseable
- usually used in an algorithm 

# lambda format

- format for a lambda: variables to use in the function

* capture clause: variables that are to be copied inside the lambda function
* parameters: argument to be passed to the lambda at execution time
* definition: defines the lambda function

[ capture variables ] (parameters) {
  Definition
}


auto divisible = [] (int num) { return num % 2 == 0; };

if(divisible(4) ) {
  cout << "True";
}

- suppose we don't care if it's even or odd, we just want to see if it's divisible by a particular value...

int value;
cin >> value; 
auto divisible = [value] (int num) {return num % value == 0;};

if (divisible(4)){
  cout << "True"; 

}

- capture clasues is used to capture variables; 

send the 'value' as the capture clause so it can be used in the definition

it captures the variable and allows us to use it in our defintion

```
array<int, 20> values = { 90, 99, 70, 2, 19, 37, 65, 84, 2, 21}; 

int divisible = 5; 
int cnt = count_if(values.begin(), values.end(), [divisible](int num){return num % divisible == 0;})

- want to see how many of the values in the array are divisible by 5; 
send divisible variable in by capture clause, int num will represent each of the items, one at a time 

will count how many are divisble by 5; 

```

* lambda is a function that's used like a variable.  in the count_if the lambda is used in palce of the variable  

# count_if 

- count of cars from 2020 

```
struct Car {

  string make;
  string model; 
  int year; 
  string vin; 

}

vector<Car> cars = {
  {"Honda", "Accord", 2020, "4YLJ44837838"},
  {"Toyota", "Camry", 2020, "4YLJ44837838"},
  {"Mazda", "Miata", 2016, "4YLJ44837838"};

};

int year = 2020; 
int cnt = count_if(cars.begin(), cars.end(), [year](const Car &c) {return c.year == year;});
cout << cnt << endl; 

```

* year is the variable to send to lambda, put in capture clause 

so as long as c.year is equal to the year we are looking for (2020), then it counts it using count_if 

output: 2

# sort with lambda

```
struct Car {

  string make;
  string model; 
  int year; 
  string vin; 

}

vector<Car> cars = {
  {"Honda", "Accord", 2020, "4YLJ44837838"},
  {"Toyota", "Camry", 2020, "4YLJ44837838"},
  {"Mazda", "Miata", 2016, "4YLJ44837838"};

};

 
sort(cars.begin(), cars.end(), [](const Car &a, const Car &b) {return a.year < b.year;});
cout << cnt << endl; 

```

- sorting the items, need to compare each item to each other

- use 2 instances of the car, a and b.  

- sorting by year .. a.year < b.year ...smallest to largest by year



# Pointers

- what are pointers

- variable that holds the memory address of another variable

- this allows us to have dynamic memory (static memory up until now)


# what is a variable? 

* name 
* address or location in memory (0xfc2001)
* content 

int num = 10;       => num    0xfc2001 |  10 

- the type of data allocates the number of bytes

int is 4 bytes vs dbl. is 8 bytes... etc

# Address-Of Operator (&)

- Address-Of Operator gives the address; shows us where variable is stored

int num = 10
double num2 = 15.7;
cout << &num; 
cout << &num2; 

will be different every time program is ran because won't be stored in same location every time


# Dereference Operator (*)

- Pointers are variables with a value of a memory address
  - isntead of having a value (like 15.8), instead, it has a memory address of where the data is actually stored

- points to first byte

- asterisk defines it as pointer

``````
int num = 10; 
double num2 = 15.7; 

int *iPtr;
double *dPtr; 

iPtr = &num1;
dPtr = &num2; 
-----------------------------
output:   num1 is 10;   num2 is 15.7
iPtr is 0xfc2001;   dPtr is 0xfc2005

``````

- two purposes of * 

* declares a pointer - put a * in front of a variable and it's now a pointer
* dereferences a pointer - 

so a cout statement for the pointer as follows: 

cout << iPtr
cout << dPtr

will gives the addresses for the pointers - 0xfc2001 and 0xfc2005
but if i do: 
cout << *iPtr; 
cout << *dPtr;

it dereferences the pointer and prints out the value of whats' stored at that location

will give - 10 and 15.7

# Variables and Pointers 

* has a
* name
* address or location in memory
* content

int num;        num => 0xfc2001 | (no value given)
int *ptr;      ptr =>   0xfc2015

difference is if i set my num = 123

then:    num =>  0xfc2001 |  123


and with the pointer - if i set ptr = &num; 
set it to have the address of num
 then we get :     ptr => 0xfc2015 |  0xfc2001 (the address of num)


so a pointer points to a memory location, but it also has a memory location of where it exists
 cout << *ptr;  will output   123 (it's dereferenced and gives the value)


 # Memory Management 
 
2 places data gets stored: 

- stack memory - stores temporary data; stores variables; super efficient because of stack structure
- heap - allows you to dynamically allocate data;  the data persists throughout your program; 

# Stack

- stack segment is where memory is allocated for local variables within functions. 
- such memory is claimed back when the function returns
- needs to know exactly the size of the data in order to store it on the stack

# heap

- provides more stable storage of global data;  memory allocated in the heap remains in existence for the duraction of the program or untnil the program releases it  

- disadvantage  doesn't automaticlly deallocate memory like the stack does;  you have to specifically instruct it to do so


pros and cons

- stack pros
* automatica memory management: 
* don't need to worry about memory management and cleaning up after functions, local variables
- stack cons
 * static allocation of memory; need to know ahead of runtime how big your data is, how much memory is needed


- heap variabels  - the 'new' operator is used to request blocks of heap memory

* pros - dynamic allocation of memory:
  - you don't need to know the size of the memory you are requesting before runtime

  * cons - manual memory management: 
  you have to remember to use the delete operator to release memory


  # stack : declare variables

  - declaring variables reserves the space 

  * int = 4 bytes
  * float = 4 bytes 
  * double = 8 bytes
   etc etc
will reserves the size for whatever type is declared


# New Keyword - heap data

- new keyword: creates object and allocates space 

int* x = new int; stored on heap
double* y = new double(8.6); stored on the heap. 

* they are pointers because need a pointer to use 'new' operator

Date* dt = new Date("01/01/2024")

// new specifies that all variables will be stored on the heap 

# nullptr Keyword

- nullptr means that the pointer does not have memory allocated on the queue

- when you use the new keyword, you do not need to re-declare the variable 

- suppose we don't know how much memmory we want to allocate, can specify nullptr which means it has no value, not pointing to any data, just go ahead and allocate some space 

```
int* x = nullptr;
double* y = nullptr; 

Date* dt = nullptr; 

- the above code just declares the variable, initializes it to null, no value; later on, don't have to redclare it. can just call: 

x = new int; 
y = new double(8.6)


dt = new Date ("01/01/2023")
```
- when the new keyword is used, you dont need to re-declare the variable 

# delete keyword

- new keyword: creates object and allocates space 

- call to new requires call to delete

```
int* x = new int; 
double* y = new double(8.6); 

Date* dt = new Date("1/1/2023"); 

delete x; 
delete y;
delete dt; 

x = nullptr
y = nullptr;
dt = nullptr

* setting it equal to nullptr is when you're specifying it has no value anymore


```

- if a pointer does not have memory allocated, you may set it equal to nullptr

- no value for pointer

- just because it is deleted, all that does is deallocate the memory, it doesn't necessarily erase the memory, it's still there. 
- it's not actually deleted

# pointers and arrays

- a fixed size array is a pointer (we know it's a fixed size because it doesn't use the 'new' operator)
``````
int primes[] = {2, 3, 4, 5, 7};
for(int i = 0; i < 4; i++>){
  cout << *(primes + 1)>>  //this is dereferencing a pointer
}

//* primes is a pointer to wherever 2 is stored in memory; can access the next value by using primes[i]; 
//
``````
this is stored on stack, not heap. it's fixed size; no 'new' keyword being used

# pointer array

can do the same as above with a pointer array; but don't have to specify the size when it's instantiated

* dynamic sized pointer
* heap variables: uses 'new' keyword

```
int *primes = new int[user_defined_size]; 
for(int i = 0; i < user_defined_size; i++>){

  primes[i] = i * 10; 

}
 

 delete [] primes; // must call delete or memory is not deallocated
```


# can also reallocate data

* pointer can be reused
* must reallocate data with new keyword
* loses original data
* must call delete again 

```

int *primes = new int[user_defined_size]; 
for(int i = 0; i < user_defined_size; i++>){

  primes[i] = i * 10; 

}
 

 delete [] primes;

 primes = new int[1000];
 ...//do stuff
 delete [] primes; 


```

# Pointers to objects

* dynamic memory for objects; if i want to allocate dynamic memory for the Time struct, 
use:

Time *t = new Time; 
- this will allocate memory on the heap, for all variables we need.
struct Time {
  int hours;
  int minutes;
  int seconds;
}


# dereferencing the values  

- can use the * to dereference the object 

- parenthesis needed to specify the object 

Time *t = new Time; 
(*t).hours = 11;
(*t).minutes = 45;
(*t).seconds = 17;

can also use an arrow operator

# arrow operator

- class member access operator 
- used with a pointer 

Time *t = new Time; 
t->hours = 11;
t->minutes = 45;
t->seconds = 17;


this says, my object 't' that points to wherever the location the data the is stored, what is inside the objects is this hours, minutes, seconds.  so can set these variables using the arrow operator

can't use dot oeprator because t is not a variable, it's a pointer to where the data is stored

so t's hours are 11.  etc 

# delete operator

- new operator allocates on the heap
- delete operator removes from the heap 

Time *t = new Time; 
t->hours = 11;
t->minutes = 45;
t->seconds = 17;
delete t; 

# Pointers to objects 

```
//given the following code: 

class Time {
  public:
    Time(int h, int m, int s) : hours_(h), minutes_(m), second_(s) {}
    int GetHours() {return hours_; }
    friend ostream& operator << (ostream & out, const Time &t); 

    private:
    int hours_;
    int minutes_;
    int second_; 
}; 


```

- can do the same thing with pointers to objects in classes

- call the constructor: 

Time *t = new Time(11.45, 17);
cout << *t;

creates the object in memory, on the heap, and have t point to wherever that object is stored in memory;

if i want to call any of the functions in the class, have to use arrow operator: 

Time *t = new Time(11.45, 17);
cout << *t;
int hours = t->GetHours(); 
 (t is not an object, it's a pointer to an object) 
 delete t; //besure to call delete 

 *  KEY NOTE:  if it's a pointer, use an arrow instead of a dot. 


# array of objects


- each posiition in the array contains space for each variable

gives the class: 

class Point {
  public:
    Point(int x, int y) : x(x), y(y) {}
    int GetX() {return x; }
    int GetY() {return y; }

    private:
    int x, y; 
}

here is a vector of Points;  a point has an x, and y value;  

if i create an array of points, and push_back 4 points; we will have:

position 0 - stores X: 6
                    Y: 2
position 1 - stores X: 3
                    Y: 5
position 2 - stores X: 6
                    Y: 7
position 3 - stores X: 2
                    Y: 7

this is allocated space for an entire 'Point' instead of just an int, dbl, etc


# Array of objects
- each position in the array contains address on stack and dynamically allocated space on the heap
if we create a vector of points: 
vector<Point*> points; 

Point* means:
a list of values that are all stored on the heap

so the address  of that value is stored in that pos in the array and this is smaller than storing the value, it just stores an address to the value; but the objec tis stored in the heap so it can dynamically 

- vector itself is  not a pointer, just storing pointers that point some place on the heap


# List of pointers vs list of objects


* list of pointers:   vector<Point*>points; 
  points.push_back(new Point(6, 2));
  points.push_back(new Point(3, 5));
  points.push_back(new Point(6, 7));

   


  * list of objects: vector<Point> points; 

points.push_back(Point(6, 2))
points.push_back(Point(3, 5))
points.push_back(Point(6, 7))

# if we want to iterate through them:  

* Pointers:  

vector<Point*> points;

for(auto i: points){
  cout << i->GetX()<< " " ; 
}

* list of objects:
vector<Point> points; 

for(auto i : points) {
  cout << i.GetX() << " "; 
}


# deleted list of pointers vs objects


* pointers 

vector<Point*> points;

for(auto i : poitns) {
  delete i; 
  i =  nullptr; 
}

* objects 

vector<Point> points;

don't have to delete


# Destructor

* special member function

* destroys the class variables set by constructor

* called automattically when class goes out of scope 


# Destructor Syntax
* same name as the class

* preceded by a tilde ~ 

# pointers as private variables

* pointers can be private variables in a class

* new operator is used to create the list 

```

class IntVector{
  public:
    IntVector() {
        list = new int[10];
        num_elements_ = 0; 
    }

    //whenever new is used in constructor, be sure to use delete
    ~IntVector() {
      delete [] list_; 
    }

    void Push_Back(int value) {
        list_[num_elements_] = value;
        num_elements_++;
    }

private:

  int *list;
  int num_elements_; 
};

```
* whenever the constructro is called, it uses 'new' keyword
* because new is used, then at some point 'delete' needs to be used - deallocated
* want it in somehting that gets called automatically as soon as object goes out of scope
* this can be done in the destructor

* destructor's purpose: deallocation

# Deep vs Shallow copy

- shallow copy 
  - creates a copy of a pointer with the same memory address

  ``` 
  Point * p1 = new Point (4, 4);

  Point *p2 = p1; 

  //p1 and p2 are pointing to same address in memory
  //cout for p1 and p2 are (4,4)

  //suppose we change our p1

  p1->SetX(5);

  //this will also change p2 because it's pointing to the same memory location
  
  
  ```

  to prevent the above from being problematic, create a deep copy

  # deep copy

  - creates a copy of the values of the pointer in a different memory address

  Point *p1 = =new Point (4, 4)
//setting it equal to a new point with X an Y values that are the same as p1 
  Point *p2 = new Point(p1->GetX(), p1->GetY());
  cout << *p1;
  cout << *p2; >>>>

  //this results in the same values, but pointing to different memory addresses 

  //now if i change x, i'm only changing it for p1 
  p1->SetX(5);
  //p2 has it's own memory location and it's values stay the same 4,4 

  # Copy an object 

  - a copy of an object is a shallow copy 

  SpotItCard one(2);
  SpotItCard two(1);

two = one; 
//this command creates a shallow copy so if change one
variable, the other will change as well because it's a copy

to fix this: to avoid having 2 objects that have the same data

# Copy Constructor

- same name as the class
- one parameter is the object itself
- allows you to create deep copies of class variables
- runs when you create and assign an object 

will run in two scenarios: 
``````

//i've decalred my object
SpotItCard one(2);
//and set it equal to another object
SpotItCard two = one; 

``````

//no return type and same name as the class
example of copy constructor
``````
SpotItCard::SpotItCard(const SpotItCard &c) {
  pictures_ = new int[c.size_]; 
  size_ = c.size_; 

  for(int i = 0; i < size_; i++){
    pictures_[i] = c.pictures_[i]; 
  }
}

``````

# operator = 

similar to copy constructor but only:
- one parameter is the obejct istelf
- allows you to create deep copies of class variables
- runs when you assign an object 

example:
differet from constructor copy. because it's assigning a value after it's been initialized...must do if statement where we delete anything that happens to be there

SpotItCard & SpotItCard::operator=(const SpotItCard &c) {
  if(&c != this){
    delete []pictures_; 
  }
  pictures_ = new int[c.size_]; 
  size_ = c.size_; 

  for(int i = 0; i < size_; i++){
    pictures_[i] = c.pictures_[i]; 
  }
}
return *this; 
}


# smart pointers

- a smart pointer is a wrapper class over a pointer 

- takes care of memory management for the pointer

- #include<memory>

# types of smart pointers

types of pointers

* unique_ptr: only one resource pointing to memory (one pointer pointing to the location in memory, prevents other pointer objects from being set equal to it; prevents shallow copies)
* shared_ptr: keeps track of the number of resources pointing to memory (will keep track of how many things are pointing to it, when it is zero, it automatically deletes)

- differ in how they refer to the resource


# review: syntax raw pointers

Point * ptr = new Point (3, 4);

same but as a unique pointer:

std::unique_ptr<Point> ptr = std::make_unique<Point>(3,4);

-- or --

std::unique_ptr<Point> ptr (new Point(3,4)); 

# syntax shared pointer

std::unique_ptr<Point> ptr = std::make_shared<Point>(3,4);
-- or --

std::shared_ptr<Point> ptr (new Point(3,4));


# smart pointer usage

- usage is like raw pointers

- use the arrow operator
``````

std::shared_ptr<Point> ptr (new Point(3,4));
ptr->SetX(5); 

``````


# unique vs shared 

unique:

* owns the object it manages, ccannot share
* unless you need to share ownership, this is the pointer you should use
* cannot be copied to another pointer


shared:
* allows multiple smart pointers to share object
* keeps a reference count of the object
* increments reference count when new shared pointer is created
* reference count decremented when shared pointer goes out of scope
* deletes the object when the count becomes zero 

# copying smart pointers

- shallow copy->shared_ptr

- creates a copy of a pointer with the same memory address
``````


shared_ptr<Point> p1 (new Point(3, 4));
//shared so i can create a 2nd, 2 pointers referencing same location
shared_ptr<Point>p2 = p1; 

cout << *p1 << endl; 
cout  << *p2 << endl;
``````
- shallow copy->unique_ptr

- cannot create a shallow copy of a unique_ptr 

so, this would throw an error:

unique_ptr<Point> p1 (new Point(3,4));
unique_ptr<Point> p2 = p1; 

# move command

can use the move command to transfer ownership of the pointer 

unique_ptr<Point> p1 (new Point(3,4));
unique_ptr<Point> p2 = move(p1); 

//deallocates the space for pointer 1 and gives ownership to p2 instead.

so can't do a cout for p1; it is no longer allocated

# use_count()

- shared pointers allow multiple pointers to access the same data  

- use_count() returns the number of references 

# pointer arrays 

- create an array on heap using unique pointer


``````
//using auto cause calling make_unique; can specify an 
//array of point, and 3 determines number of elements 

auto pointerArray = make_unique<Point[]>(3);
for(int i = 0; i < 3; i++){
  pointerArray[i].SetX(i);
//dot operator used because each element is not a poitner, just the array itself is a pointer
}

``````

# Array of shared_ptr

- create a vector of pointers
- initialize each one 

 ```
 //thsi creates a vector of points
 vector<std::shared_ptr<Point>>points; 
//to add a point to the list, use push_back and make shared to initialize each of the points
points.push_back(make_shared<Point>(2, 3));
points.push_back(make_shared<Point>(1, 2)); 
//can iterate through, using auto because assigning it values each point at a time, dereference because i is a pointer
for(auto i : points){
  cout << *i << endl; 
}
 
 ```

 to iterate through a unique_ptr, 
 cout << *points[i] << endl; 


 # auto keyword

 - lets you declare a variable and determines the type at runtime

 - auto can only be used when assigned using= 

 auto p = make_unique<Point>(3,4); 

 as soon as program runs, type is determined 

 - no equal sign, cannot use auto 
 std::unique_ptr<Point>p1 (new Point(3, 4)); 

 - equal sign, can use auto 

 std::shared_ptr<Point> p1(new Point(3, 4));
 auto p2=p1;

 # UML and class relationships 

 UML stands for Unified Modeling language

 UML is used to create diagrams that describe the structure of a program by showing the programs: 

 * classes
 * attributes
 * operations(or methods)
 * relationships between objects

 # Class relationships 

 UML assists developers in visualizing and understanding the relationships between classes 

 - class attributes, methods, relationships can be represented in UML 

  # types of class relationships 

  - composition
  - aggregation
  - inheritance 

  # composition

  = "has a" relationship - person 'has a' credit card; 

  - whole/part

  - tightly bound
    - person contains instance of Credit Card

  - represented in UML with a black diamond 


# composition - in code 

- simple class to hold credit card info 

class Credit Card {
  private:
  string number_; 
  string exp_date_;
  
  public: 
  CreditCard(string number, string exp_date) : number_(number), exp_date_(exp_date) {}

  void Pay() {
    cout << "Charging card..." << endl;
  }
}


