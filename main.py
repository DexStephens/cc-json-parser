import re

def tokenize(json_string):
    token_spec = [
        (r'{', 'LBRACE'),
        (r'}', 'RBRACE'),
        (r'\[', 'LBRACKET'),
        (r'\]', 'RBRACKET'),
        (r':', 'COLON'),
        (r',', 'COMMA'),
        (r'true|false|null', 'LITERAL'),
        (r'-?\d+(\.\d+)?([eE][+-]?\d+)?', 'NUMBER'),
        (r'"(\\.|[^"\\])*"', 'STRING'),
        (r'\s+', None)
    ]
    
    token_re = re.compile('|'.join(f'(?P<{name}>{pattern})' for pattern, name in token_spec))
    
    for match in token_re.finditer(json_string):
        kind = match.lastgroup
        value = match.group()
        if kind:
            yield (kind, value)


def main():
    print("Made it")

def parseObject():
    return

def parseArray():
    return

def parseJSON():
    return

main()

# Build out a recursive descent parser

# Two main paths for lookahead
# Objects
# Arrays