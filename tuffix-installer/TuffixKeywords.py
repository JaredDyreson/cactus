#!/usr/bin/env python3.8

"""
This contains all of the keywords used in this language
"""

from Lexer import Lexer

cpsc_regex = r'CPSC\-(?P<course>[0-9]{3})'

TuffixTokenMap = {

  # builtin functions
  "INIT": r'.*init.*',
  "ADD": r'.*add.*CPSC\-(?P<course>[0-9]{3})',
  "REMOVE": r'.*remove.*CPSC\-(?P<course>[0-9]{3})',
  "LIST_INSTALLED": r'.*installed.*',
  "LIST_AVAILABLE": r'.*available.*',
  "DESCRIBE_TARGET": r'.*describe.*|CPSC\-(?P<course>[0-9]{3})',
  "REKEY": r'.*rekey.*',
  "STATUS": r'.*status.*',
  "TARGET": cpsc_regex,

  # syntax
  "COMMENT": r'^\#.*[a-zA-Z0-9]',

}

