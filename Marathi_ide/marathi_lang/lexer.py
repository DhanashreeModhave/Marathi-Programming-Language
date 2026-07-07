import re
from .tokens import KEYWORDS

token_specification = [

    ("NUMBER", r"\d+(\.\d+)?"),
    ("STRING", r'"[^"]*"'),
    ("ID", r"[A-Za-z_ऀ-ॿ]+"),

    ("OP", r"==|!=|>=|<=|[+\-*/%<>]"),
    ("ASSIGN", r"="),

    ("LBRACKET", r"\["),
    ("RBRACKET", r"\]"),

    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),

    ("COMMA", r","),

    ("SEMI", r";"),

    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),

    ("SKIP", r"[ \t\n]+")
]


tok_regex = "|".join("(?P<%s>%s)" % x for x in token_specification)


def tokenize(code):

    tokens = []

    for match in re.finditer(tok_regex, code):

        kind = match.lastgroup
        value = match.group()

        if kind == "ID" and value in KEYWORDS:
            tokens.append((KEYWORDS[value], value))

        elif kind != "SKIP":
            tokens.append((kind, value))

    return tokens