#!/usr/bin/env python3.8

"""
This contains all of the keywords used in this language
"""

from cactus.Lexer import Lexer

with open("grammar", "r") as fp:
    content  = fp.readlines()

token_map = {
  # builtin functions
  "EXIT": r'.*exit.*',
  "EXPORT": r'.*export.*',
  "LEN": r'.*len.*',
  "LIST": r'.*list.*',
  "LOAD": r'.*load.*',
  "PRINT": r'.*print.*',
  "UNLOAD": r'.*unload.*',

  # syntax
  "OPEN_PAREN": r'\(',
  "CLOSE_PAREN": r'\)',
  "OPEN_CURLY": r'\{',
  "CLOSE_CURLY": r'\}',
  "SEMI_COLON": r'\;',
  "COMMENT": r'^\#.*[a-zA-Z0-9]',

  # variable assignmet
  "ASSIGNMENT": r'.*let.*[a-zA-Z0-9].*\:\=[ \t]+.*[a-zA-Z0-9]',

  # operations
  "SUM": r'\+',
  "SUB": r'\-',

  # type definitions 
  "NUMBER": r'\d+',
  "URL": r'https:\/\/open\.spotify\.com\/(playlist|user)\/[a-zA-Z0-9]{22}\?si\=[a-zA-Z0-9]{22}$'

}

"""
Testing the lexer
"""

lexer = Lexer(token_map).get_lexer()
for line in content:
    for token in lexer.lex(line):
      print(token)
