import re

# register generator
r = 0
def new_reg():
    global r
    r += 1
    return "R" + str(r)

# precedence
prec = {'+':1, '-':1, '*':2, '/':2}

# input
expr = "a + b * (c - d)"

# tokenize
tokens = re.findall(r'[a-zA-Z]+|\d+|[+\-*/()]', expr)

# INFIX → POSTFIX
stack = []
postfix = []

for tok in tokens:
    if tok.isalnum():
        postfix.append(tok)

    elif tok == '(':
        stack.append(tok)

    elif tok == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()

    else:
        while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[tok]:
            postfix.append(stack.pop())
        stack.append(tok)

while stack:
    postfix.append(stack.pop())

# POSTFIX → ASSEMBLY
stack = []
code = []

for tok in postfix:
    if tok.isalnum():
        reg = new_reg()
        code.append(f"MOV {reg}, {tok}")
        stack.append(reg)

    else:
        r2 = stack.pop()
        r1 = stack.pop()

        if tok == '+':
            code.append(f"ADD {r1}, {r2}")
        elif tok == '-':
            code.append(f"SUB {r1}, {r2}")
        elif tok == '*':
            code.append(f"MUL {r1}, {r2}")
        elif tok == '/':
            code.append(f"DIV {r1}, {r2}")

        stack.append(r1)

# output
print("Assembly Code:")
for line in code:
    print(line)

print(f"; Final result in {stack[-1]}")
