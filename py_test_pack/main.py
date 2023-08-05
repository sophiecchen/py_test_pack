#!/usr/bin/python
# -*- coding: utf-8 -*-

from re import match

def alphabet(text):
    regex = "[a-zA-Z]+"
    regex += "at"
    matcher = match(regex, text)
    
    if matcher:
        return True
    else:
        return False

def numbers(text):
    regex = "[1-9]"
    regex += "[0-9]*"
    regex += "%"
    matcher = match(regex, text)
    
    if matcher:
        return True
    else:
        return False
