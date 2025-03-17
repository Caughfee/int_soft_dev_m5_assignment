# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Rogine Mirando

## Assignment
Assignment 01: Classes, Encapsulation and Unit Test Planning
The classes will incorporate the outcomes associated with Module 01.
Encapsulation of private attributes, public accessors and mutators.

Assignment 02: Abstraction, Inheritance and Polymorphism
This assignment will focus on the topics we have learned in Module 2.
Abstraction, Inheritance, and Polymorphism.

Assignment 03: Design Patterns
For this assignment I will use the knowledge of design patterns gained from Module 3.

## Encapsulation
The way I achieved encapsulation in my BankAccount class is how I made the account_number, client_number, and balance.
They're private attributes because their names are added with a double underscore prefix.

## Polymorphism
How I achieved polymorphism is how each bank account type use the same method names, like get_service_charges(), but it has something to add on to the method. An example would be something like appending more text to __str__().

## Strategy Pattern
I used the Strategy Pattern by creating separate strategy classes to handle service charge calculations for different types. ChequingAccount, InvestmentAccount, and the SavingsAccount classes uses the chosen strategy at runtime.

## Observer Pattern
I used the Observer Pattern by having clients subscribe to bank accounts using the attach() method, and when significant events happen, the bank accounts call notify() which triggers each client's update() method to send an email alert. 