#!/usr/bin/env python3
import skilstak.colors as c
"""This is my hello world program."""
def print_colors(message):
def print_plain(message):
    """This is my color function"""
    print(message)
def print_forever(message):
    while True:
          print(c.rc() + message)
if __name__== '__main__':
    import sys
    
    who = "world"
    
    if len(sys.argv) == 2:
        print_plain("hello " + who + "!")
    print_plain("Hello world")
    print_forever("Hello People Of The World!!!!!!!!!!!!!!!!!!" )
  

