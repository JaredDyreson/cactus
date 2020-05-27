# Tuffix Lang

This is a simple mnemonic language developed in my spare time to teach myself how lexer, parsers and compilers work.

There are four components to this build:

- Lexer
- AST
- Parser
- Grammar

# Lexer

This takes in a "token map", which is just a dictionary that has a string associated with a regular expression.

Here is the one we are using in this project:

```python
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
```
And we are ignoring spaces by default.

# AST

AST stands for "abstract syntax tree" and this is where the grammar, functions and tokens all meet.
Each class must contain a `eval` function as this is what the parser uses to associate an action for a set of grammar parameters (I think that's how you explain it?).

# Parser

Here is where the grammar is defined and is processed.
An example grammar rule is:

```python
@self.pg.production('expression : TARGET')
```

`expression` is a filler word that is not associated with a token directly.

This can be seen in this grammar rule:

```python
@self.pg.production('expression : expression MUL expression')
```

When going through the parsing process, an example function can be used:

```python
def multiply(p):
  left = p[0]
  right = p[2]
  return Multiply(left, right)
```
Where the `Multiply` function would be defined in the `AST`.
For this to work as well, you would need to define what a number is, which can be defined in the lexer token map.
