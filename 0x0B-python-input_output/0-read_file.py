#!/usr/bin/python3
"""defining function to read text file"""
def read_file(filename=""):
    """function reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
