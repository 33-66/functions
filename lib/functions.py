#!/usr/bin/env python3

def greet_programmer():
    greet = print("Hello, programmer!")
    return greet
    
greet_programmer()

def greet(name):
    greeting = print(f"Hello, {name}!")
    return greeting
    
greet("simon")    

def greet_with_default(name="programmer"):
    default_greetings = print(f"Hello, {name}!")
    return default_greetings
    
greet_with_default()    

def add(num1, num2):
    return num1 + num2

add(45,55)

def halve(number):
    return number/2

halve(20) 
