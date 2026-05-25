# ----- DFA Lexical Analyzer -----
KEYWORDS = {"int", "float", "char", "if", "else", "while", "return", "true", "false", "print"}
OPERATORS = {"+", "-", "*", "/", "=", "<", ">"}
SPECIAL_SYMBOLS = {";", ",", "(", ")", "{", "}", ":"}
def tokenize(code):
    tokens = []
    i = 0
    n = len(code)
    while i < n:
        ch = code[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isalpha() or ch == "_":
            start = i
            i += 1
            while i < n and (code[i].isalnum() or code[i] == "_"):
                i += 1
            lexeme = code[start:i]
            if lexeme in KEYWORDS:
                tokens.append((lexeme, "KEYWORD"))
            else:
                tokens.append((lexeme, "IDENTIFIER"))
            continue
        if ch.isdigit():
            start = i
            i += 1
            while i < n and code[i].isdigit():
                i += 1
            tokens.append((code[start:i], "NUMBER"))
            continue
        if ch in OPERATORS:
            tokens.append((ch, "OPERATOR"))
            i += 1
            continue
        if ch in SPECIAL_SYMBOLS:
            tokens.append((ch, "SPECIAL SYMBOL"))
            i += 1
            continue
        i += 1
    return tokens
def display_dfa(lexeme, token_type):
    print(f"\nLexeme: {lexeme}")
    print("Start State: q0")
    current_state = "q0"
    for i, ch in enumerate(lexeme):
        next_state = f"q{i + 1}"
        print(f"{current_state} -- {ch} --> {next_state}")
        current_state = next_state
    print(f"Final State: {current_state} ({token_type})")
def lexical_analyzer(code):
    tokens = tokenize(code)
    print("\nTokens:")
    for lexeme, token_type in tokens:
        print(f"{lexeme}  ->  {token_type}")
    print("\nDFA Representation:")
    for lexeme, token_type in tokens:
        display_dfa(lexeme, token_type)
print("Enter your code (finish input with an empty line):")
lines = []
while True:
    try:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    except EOFError:
        break
source_code = "\n".join(lines)
lexical_analyzer(source_code)