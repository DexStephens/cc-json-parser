# cc-json-parser

Python JSON parser

The process of parsing

Lexical Analysis: read input character stream into input tokens

Syntactic Analysis: use a set of grammar rules to analyze the sequence of tokens. Build a parse tree or AST, where each node represents a grammatical construct in the program. Check for syntax errors if the token sequence doesn't match the grammar rules.

Tokenization: the process of breaking down a piece of text, into individual tokens. Tokens are defined by the language in which the incoming text is being translated into

Parsing Algorithms

1. Top-Down Parsing(Recursive Descent): start with the start symbol and apply the productions until you arrive at the desired string
2. Bottom-Up Parsing(Shift-reduce): Start with the string and reduce it to the start symbol by applying the productions backwards
3. LALR

Backtracking, how does it work?
