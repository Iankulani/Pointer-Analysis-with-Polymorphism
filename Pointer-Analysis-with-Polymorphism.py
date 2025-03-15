# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 3:41:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Pointer Analysis Tool")
print(Fore.GREEN+font)

import re

def prompt_for_input():
    print("Please enter your C/C++ program code below (press Enter twice to finish):")
    code = []
    while True:
        try:
            line = input()
            if line == "":
                break
            code.append(line)
        except EOFError:
            break
    return "\n".join(code)

def analyze_pointers_and_polymorphism(code):
    # Regex patterns for pointer analysis
    pointer_pattern = r'\w+\s*\*\s*\w+'  # Matches pointer declarations
    virtual_function_pattern = r'virtual\s+\w+\s+\w+\s*\(.*\)\s*;'  # Matches virtual functions in C++

    # Analyze pointer declarations
    print("\nPointer Analysis:")
    pointers = re.findall(pointer_pattern, code)
    if pointers:
        print("Pointers found:")
        for pointer in pointers:
            print(f"- {pointer}")
    else:
        print("No pointers found.")
    
    # Analyze polymorphism (virtual function declarations)
    print("\nPolymorphism Analysis (virtual functions):")
    virtual_functions = re.findall(virtual_function_pattern, code)
    if virtual_functions:
        print("Virtual functions found:")
        for func in virtual_functions:
            print(f"- {func}")
    else:
        print("No virtual functions found.")
    
    # Optional: Additional polymorphism analysis could be added here
    
def main():
    # Step 1: Prompt user to enter code
    code = prompt_for_input()

    # Step 2: Perform pointer and polymorphism analysis
    analyze_pointers_and_polymorphism(code)

if __name__ == "__main__":
    main()
