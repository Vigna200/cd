import re

# Lexical Analysis
def lexer(expr):
    pattern=r'\d+|[a-zA-Z]+|[+\-*/=()]'
    tokens=[]
    for tok in re.findall(pattern,expr):
        tokens.append(tok)
    return tokens

# Infix to Postfix
def infix_to_postfix(tokens):
    prec={'+':1,'-':1,'*':2,'/':2}
    stack=[]
    postfix=[]

    for tok in tokens:
        if tok.isalnum():
            postfix.append(tok)

        elif tok=='(':
            stack.append(tok)

        elif tok==')':
            while stack and stack[-1]!='(':
                postfix.append(stack.pop())
            stack.pop()

        else:
            while stack and stack[-1]!='(' and prec[stack[-1]]>=prec[tok]:
                postfix.append(stack.pop())
            stack.append(tok)

    while stack:
        postfix.append(stack.pop())

    return postfix


# TAC
t=0
def new_temp():
    global t
    t+=1
    return "t"+str(t)

def generate_tac(postfix,lhs=None):
    stack=[]
    tac=[]

    for tok in postfix:
        if tok.isalnum():
            stack.append(tok)
        else:
            b=stack.pop()
            a=stack.pop()
            temp=new_temp()
            tac.append(f"{temp} = {a} {tok} {b}")
            stack.append(temp)

    result=stack.pop()

    if lhs:
        tac.append(f"{lhs} = {result}")

    return tac


# Optimization
def optimize_tac(tac):
    opt=[]

    for line in tac:
        p=line.split()

        if len(p)==5 and p[2].isdigit() and p[4].isdigit():
            val=eval(p[2]+p[3]+p[4])
            opt.append(f"{p[0]} = {val}")
        else:
            opt.append(line)

    return opt


# Target Code
r=0
def new_reg():
    global r
    r+=1
    return "R"+str(r)

def assembly(tac):
    code=[]

    for line in tac:
        p=line.split()

        if len(p)==3:
            code.append(f"MOV {p[0]}, {p[2]}")

        else:
            reg=new_reg()
            code.append(f"MOV {reg}, {p[2]}")

            if p[3]=='+':
                code.append(f"ADD {reg}, {p[4]}")
            elif p[3]=='-':
                code.append(f"SUB {reg}, {p[4]}")
            elif p[3]=='*':
                code.append(f"MUL {reg}, {p[4]}")
            elif p[3]=='/':
                code.append(f"DIV {reg}, {p[4]}")

            code.append(f"MOV {p[0]}, {reg}")

    return code


# MAIN
expr=input("Enter expression: ")

tokens=lexer(expr)
print("Tokens:",tokens)

if '=' in tokens:
    i=tokens.index('=')
    lhs=tokens[0]
    rhs=tokens[i+1:]
else:
    lhs=None
    rhs=tokens

postfix=infix_to_postfix(rhs)
print("Postfix:",postfix)

tac=generate_tac(postfix,lhs)
print("\nTAC")
for i in tac:
    print(i)

opt=optimize_tac(tac)
print("\nOptimized TAC")
for i in opt:
    print(i)

asm=assembly(opt)
print("\nAssembly")
for i in asm:
    print(i)