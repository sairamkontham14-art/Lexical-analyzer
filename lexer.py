from pygments import lex
from pygments.lexers import PythonLexer

code = """
print("hello world")
"""

tokens = list(lex(code, PythonLexer()))

count = 0

for token_type, value in tokens:
    print(token_type, "->", value)
    count += 1

print("\nTotal tokens:", count)