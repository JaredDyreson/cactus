#!/usr/bin/env python3.8

"""
This contains all of the keywords used in this language
"""

from Lexer import Lexer

cpsc_regex = r'CPSC\-(?P<course>[0-9]{3})'

token_map = {
  # builtin functions
  "INIT": r'.*init.*',
  "ADD": r'.*add.*|{}'.format(cpsc_regex),
  "REMOVE": r'.*remove.*|{}'.format(cpsc_regex),
  "LIST_INSTALLED": r'.*installed.*',
  "LIST_AVAILABLE": r'.*available.*',
  "DESCRIBE_TARGET": r'.*describe.*|{}'.format(cpsc_regex),
  "REKEY": r'.*rekey.*',
  "STATUS": r'.*status.*',
  "TARGET": cpsc_regex,

  # syntax
  "COMMENT": r'^\#.*[a-zA-Z0-9]',
}

