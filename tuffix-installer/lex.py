#!/usr/bin/env python3.8

"""
This contains all of the keywords used in this language
"""

from Lexer import Lexer

with open("grammar", "r") as fp:
    content  = fp.readlines()

token_map = {
  # builtin functions
  "INIT": r'.*init.*',
  "ADD": r'.*add.*[a-zA-Z]{4}.*[0-9]{3}',
  "REMOVE": r'.*remove.*[a-zA-Z]{4}.*[0-9]{3}',
  "LIST_INSTALLED": r'.*installed.*',
  "LIST_AVAILABLE": r'.*available.*',
  "DESCRIBE_TARGET": r'.*describe.*[a-zA-Z]{4}.*[0-9]{3}',
  "REKEY": r'.*rekey.*',
  "STATUS": r'.*status.*',
  "TARGET": r'CPSC.*[0-9]',

  # syntax
  "COMMENT": r'^\#.*[a-zA-Z0-9]',

  # type definitions 
  "NUMBER": r'\d+'

}

"""
Testing the lexer
"""

# current_line = None
# try:
  # lexer = Lexer(token_map).get_lexer()
  # for line in content:
      # current_line = line
      # for token in lexer.lex(line):
        # print(token.gettokentype())
# except Exception as error:
    # print("[-] Invalid selection of {}, stop".format(current_line.strip()))
