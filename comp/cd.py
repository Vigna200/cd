from collections import defaultdict

grammar = {
    "S": [["E"]],
    "E": [["E","+","T"],["T"]],
    "T": [["T","*","F"],["F"]],
    "F": [["(","E",")"],["id"]]
}

NT = ["S","E","T","F"]
T = ["id","+","*","(",")","$"]
FIRST, FOLLOW = defaultdict(set), defaultdict(set)

def first():
    for t in T: FIRST[t].add(t)
    ch=True
    while ch:
        ch=False
        for h,prods in grammar.items():
            for p in prods:
                b=len(FIRST[h])
                FIRST[h] |= FIRST[p[0]]
                if len(FIRST[h]) > b: ch=True

def follow():
    FOLLOW["S"].add("$")
    ch=True
    while ch:
        ch=False
        for h,prods in grammar.items():
            for p in prods:
                for i,s in enumerate(p):
                    if s in NT:
                        b=len(FOLLOW[s])
                        if i+1 < len(p): FOLLOW[s] |= FIRST[p[i+1]]
                        else: FOLLOW[s] |= FOLLOW[h]
                        if len(FOLLOW[s]) > b: ch=True

def closure(I):
    I=set(I)
    ch=True
    while ch:
        ch=False
        for h,b,d in list(I):
            if d<len(b) and b[d] in grammar:
                for p in grammar[b[d]]:
                    item=(b[d],tuple(p),0)
                    if item not in I:
                        I.add(item); ch=True
    return frozenset(I)

def goto(I,x):
    J=[(h,b,d+1) for h,b,d in I if d<len(b) and b[d]==x]
    return closure(J) if J else None

def states():
    s=closure([("S",tuple(grammar["S"][0]),0)])
    C,trans=[s],{}
    for I in C:
        for x in T+NT:
            g=goto(I,x)
            if g:
                if g not in C: C.append(g)
                trans[(C.index(I),x)] = C.index(g)
    return C,trans

def table(C,trans):
    ACT,G={},{}
    for i,I in enumerate(C):
        for h,b,d in I:
            if d<len(b) and b[d] in T:
                ACT[(i,b[d])] = "s"+str(trans[(i,b[d])])
            elif d==len(b):
                if h=="S": ACT[(i,"$")] = "acc"
                else:
                    for a in FOLLOW[h]:
                        ACT[(i,a)] = "r"+h+"->"+" ".join(b)
        for nt in NT:
            if (i,nt) in trans: G[(i,nt)] = trans[(i,nt)]
    return ACT,G

def parse(s,ACT,G):
    tok=s.replace("+"," + ").replace("*"," * ").replace("("," ( ").replace(")"," ) ").split()
    tok=["id" if x.isalnum() else x for x in tok]+["$"]
    st,i=[0],0

    while True:
        a=ACT.get((st[-1],tok[i]))
        if not a: return "Invalid"
        if a=="acc": return "Valid"
        if a[0]=="s":
            st += [tok[i],int(a[1:])]
            i+=1
        else:
            h,b=a[1:].split("->")
            b=b.split()
            st=st[:-2*len(b)]
            st += [h,G[(st[-1],h)]]

first()
follow()
C,trans=states()
ACT,G=table(C,trans)

s=input("Enter expr: ")
print(parse(s,ACT,G))