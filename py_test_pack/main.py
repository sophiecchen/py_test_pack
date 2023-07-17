#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

def alphabet(text):
    regex = "[a-zA-Z]+"
    regex += "at"
    match = re.match(regex, text)
    
    if match:
        return True
    else:
        return False

def numbers(text):
    regex = "[1-9]"
    regex += "[0-9]*"
    regex += "%"
    match = re.match(regex, text)
    
    if match:
        return True
    else:
        return False
