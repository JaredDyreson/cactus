from rply import ParserGenerator
from ast import *
from tuffix_lex import token_map
from Lexer import Lexer

class Parser():
    def __init__(self, tokens: dict):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            list(tokens.keys())
        )

    def parse(self):
        @self.pg.production('expression : TARGET')
        def epxression_target(p):
            return Target(str(p[0].getstr()))

        @self.pg.production('expression : ADD')
        def install(p):
            target = str(p[0].getstr()).split()[1]
            return Install(target)

        @self.pg.production('expression : REMOVE')
        def remove(p):
            target = str(p[0].getstr()).split()[1]
            return Remove(target)

        @self.pg.production('expression : DESCRIBE_TARGET')
        def describe(p):
            target = str(p[0].getstr()).split()[1]
            return Describe(target)

        @self.pg.production('expression : COMMENT')
        def ignore_comment(p):
            return Ignore(p)

        @self.pg.error
        def error_handle(token):
            raise Exception(token)

    def get_parser(self):
        return self.pg.build()

"""
Reading a file, simulating the instructions given to the interpreter
"""

current_line = None
lexer = Lexer(token_map).get_lexer()
with open("grammar", "r") as fp: content = fp.readlines()
pg = Parser(token_map)
pg.parse()
parser = pg.get_parser()

try:
    for line in content:
      current_line = line
      parser.parse(lexer.lex(line)).eval()
except Exception as error:
    print("[-] Invalid selection of {}, stop".format(current_line.strip()))
