import re

# temp variable generator
t = 0
def new_temp():
    global t
    t += 1
    return "t" + str(t)

# precedence
prec = {'+':1, '-':1, '*':2, '/':2}

# input
expr = "e = a + b * (c - d)"

# split LHS and RHS safely
lhs, rhs = expr.split('=')
lhs = lhs.strip()
rhs = rhs.strip()

# tokenize (variables + numbers)
tokens = re.findall(r'[a-zA-Z]+|\d+|[+\-*/()]', rhs)

# INFIX → POSTFIX
stack = []
postfix = []

for tok in tokens:
    if tok.isalnum():   # handles variables + numbers
        postfix.append(tok)

    elif tok == '(':
        stack.append(tok)

    elif tok == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()

    else:  # operator
        while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[tok]:
            postfix.append(stack.pop())
        stack.append(tok)

while stack:
    postfix.append(stack.pop())

# POSTFIX → TAC + QUADRUPLES
stack = []
tac = []
quad = []

for tok in postfix:
    if tok.isalnum():
        stack.append(tok)
    else:
        b = stack.pop()
        a = stack.pop()
        temp = new_temp()

        tac.append(f"{temp} = {a} {tok} {b}")
        quad.append((tok, a, b, temp))

        stack.append(temp)

# final assignment
result = stack.pop()
tac.append(f"{lhs} = {result}")
quad.append(('=', result, '-', lhs))

# TRIPLES
triples = []
temp_map = {}

for i, (op, a1, a2, res) in enumerate(quad):
    a1 = temp_map.get(a1, a1)
    a2 = temp_map.get(a2, a2)

    triples.append((op, a1, a2))
    temp_map[res] = f"({i})"

# INDIRECT TRIPLES
pointer = list(range(len(triples)))

# OUTPUT
print("\n Three Address Code:")
for i in tac:
    print(i)

print("\n Quadruples:")
for i in quad:
    print(i)

print("\n Triples:")
for i, t in enumerate(triples):
    print(i, t)

print("\n Indirect Triples:")
print("Pointer Table:", pointer)
