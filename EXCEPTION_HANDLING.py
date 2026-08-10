"""
DEFINITION / CONCEPT:
Exception Handling in Python (Try-Except Block)

This program demonstrates input validation using Exception Handling in Python. 
When a user enters non-integer text instead of a numeric PIN, Python raises a 
'ValueError'. The 'try-except' block catches this error to prevent the program 
from crashing and prompts the user to re-enter a valid input.
"""


try:
    # User se PIN enter karne ko bol rahe hain aur use integer me convert kar rahe hain
    a = int(input("enter ur pin: "))
    print(a)
except:
    # Agar user integer ki jagah string/text enter kare toh ye block chalega
    print("entered value is not in integer form, please reenter")
    
    # User se dobara input le rahe hain
    a = input("enter ur number")
    
    # Check kar rahe hain ki kya naya input integer type ka hai
    if type(int(a)) == type(10):
        print("ur pin is", a)
    else:
        print("invalid input")




'''
=================== EXPECTED OUTPUT ===================

Case 1: Jab user pehle hi numeric PIN daal de
---------------------------------------------
enter ur pin: 1122
1122

Case 2: Jab user text daale, aur re-entry me number daale
--------------------------------------------------------
enter ur pin: one thousand twenty two
entered value is not in integer form, please reenter
enter ur number 1122
ur pin is 1122

=======================================================
'''


"""
DEFINITION / CONCEPT:
Variable Initialization and NameError Handling

This program demonstrates variable initialization and Exception Handling in Python.
It checks whether a variable ('b') exists and can be printed. If the variable is 
not initialized beforehand, Python raises a 'NameError', which is caught by the 
'except' block to prompt the user to input its value manually.
"""

# Variable 'b' ko initial value assign kar rahe hain
b = 1000

try:
    # Variable 'b' ki value print karne ki koshish kar rahe hain
    print(b)
except:
    # Agar 'b' initialized nahi hota (NameError aata), toh ye block chalta
    print("b is not yet initialised, please enter b:")
    
    # User se 'b' ki value input le rahe hain
    b = input("please enter b's value: ")
    
    # Entered value ko print kar rahe hain
    print("this is the value of b:", b)


'''
=================== EXPECTED OUTPUT ===================

Case 1: Jab 'b = 1000' pehle se Defined Hai (Aapki Image Ka Output)
------------------------------------------------------------------
1000

Case 2: Agar 'b = 1000' wali line na ho (b Initialized Na Ho)
------------------------------------------------------------
b is not yet initialised, please enter b:
please enter b's value: 500
this is the value of b: 500

=======================================================
'''


"""
DEFINITION / CONCEPT:
Division by Zero Exception Handling (ZeroDivisionError)

This program demonstrates how to handle division by zero errors in Python. 
When a user attempts to divide a number by zero, Python raises a 'ZeroDivisionError'. 
The 'try-except' block catches this exception to prevent program crash and prompts 
the user to enter a valid, non-zero denominator.
"""

try:
    # User se numerator (a) input le rahe hain
    a = int(input("enter numerator:"))
    
    # User se denominator (b) input le rahe hain
    b = int(input("enter denominator:"))
    
    # Division perform kar rahe hain aur result print kar rahe hain
    print("the division of a/b is=", a/b)
    
except:
    # Agar denominator 0 enter kiya (ZeroDivisionError aaya), toh ye block chalta hai
    print("you cannot enter denominator as 0")
    
    # User se dobara denominator input le rahe hain
    b = int(input("enter denominator:"))
    
    # Check kar rahe hain ki kya naya denominator 0 ke barabar toh nahi hai
    if b != 0:
        print("the division of a/b is=", a/b)
    else:
        print("invalid input re run code")


'''
=================== EXPECTED OUTPUT ===================

Case 1: Jab valid numbers enter kiye jayein
---------------------------------------------
enter numerator:10
enter denominator:2
the division of a/b is= 5.0

Case 2: Jab denominator 0 enter kiya jaye, aur re-entry me non-zero daala jaye
----------------------------------------------------------------------------
enter numerator:10
enter denominator:0
you cannot enter denominator as 0
enter denominator:2
the division of a/b is= 5.0

Case 3: Jab dobara bhi 0 hi enter kiya jaye
--------------------------------------------
enter numerator:10
enter denominator:0
you cannot enter denominator as 0
enter denominator:0
invalid input re run code

=======================================================
'''



try:
    # User se numerator (a) input le rahe hain
    a = int(input("enter numerator:"))
    
    # User se denominator (b) input le rahe hain
    b = int(input("enter denominator:"))
    
    # Division perform kar rahe hain aur result print kar rahe hain
    print("the division of a/b is=", a/b)

except:
    # Agar denominator 0 enter kiya (ZeroDivisionError aaya), toh ye block chalta hai
    print("you cannot enter denominator as 0")
    
    # User se dobara denominator input le rahe hain
    b = int(input("enter denominator:"))
    
    # Check kar rahe hain ki kya naya denominator 0 ke barabar toh nahi hai
    if b != 0:
        print("the division of a/b is=", a/b)
    else:
        # Agar dobara 0 enter kiya toh infinity wala message print hoga
        print("the answer goes to infinity, try again later")


'''
=================== EXPECTED OUTPUT ===================

Case 1: Jab valid numbers enter kiye jayein
---------------------------------------------
enter numerator:10
enter denominator:2
the division of a/b is= 5.0

Case 2: Jab denominator 0 enter kiya jaye, aur re-entry me non-zero daala jaye
----------------------------------------------------------------------------
enter numerator:10
enter denominator:0
you cannot enter denominator as 0
enter denominator:5
the division of a/b is= 2.0

Case 3: Jab dobara bhi denominator 0 hi enter kiya jaye
-------------------------------------------------------
enter numerator:10
enter denominator:0
you cannot enter denominator as 0
enter denominator:0
the answer goes to infinity, try again later

=======================================================
'''



"""
DEFINITION / CONCEPT:
Try-Except-Else-Finally Block in Exception Handling

This program demonstrates the complete Exception Handling structure in Python:
1. try: Code that might raise an exception.
2. except: Code that executes if an exception occurs.
3. else: Code that executes ONLY if no exception occurs in the try block.
4. finally: Code that ALWAYS executes, regardless of whether an exception occurred or not.
"""

# Variable 'c' ko initial value assign kar rahe hain
c = 1000

try:
    # Variable 'c' ki value print karne ki koshish kar rahe hain
    print(c)
except:
    # Agar 'c' defined nahi hota (NameError aata), toh ye block chalta
    print("c in not yet initialised, please enter c:")
    
    # User se 'c' ki value input le rahe hain
    c = input("please enter c's value: ")
    
    # Inputted value ko print kar rahe hain
    print("this is the value of c:", c)
else:
    # Ye block sirf tabhi chalega jab 'try' block me koi error na aaye
    print("this is else block")
finally:
    # Ye block HAMESHA chalega, error aaye ya na aaye
    print("this is finally block: execution completed!")


'''
=================== EXPECTED OUTPUT ===================

Case 1: Jab 'c = 1000' Defined Hai (No Error)
---------------------------------------------
1000
this is else block
this is finally block: execution completed!

Case 2: Agar 'c = 1000' Defined Na Ho (Error Occurred)
------------------------------------------------------
c in not yet initialised, please enter c:
please enter c's value: 500
this is the value of c: 500
this is finally block: execution completed!

(Note: Case 2 me 'else' skip ho jayega, lekin 'finally' fir bhi chalega)
=======================================================
'''
