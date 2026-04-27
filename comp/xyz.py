from collections import defaultdict, deque
G={
"S":[["E"]],
"E":[["E","+","T"],["T"]],
"T":[["T","*","F"],["F"]],
"F":[["(","E",")"],["id"]]
}
NT=list(G.keys())
T=["id","+","*","(",")","$"]
FIRST=defaultdict(set); FOLLOW=defaultdict(set)
for t in T: FIRST[t].add(t)
changed=True
while changed:
    changed=False
    for A in G:
        for p in G[A]:
            old=len(FIRST[A])
            FIRST[A] |= FIRST[p[0]]
            changed |= len(FIRST[A])>old
FOLLOW["S"].add("$")
changed=True
while changed:
    changed=False
    for A in G:
        for p in G[A]:
            for i,x in enumerate(p):
                if x in NT:
                    old=len(FOLLOW[x])
                    if i+1<len(p): FOLLOW[x] |= FIRST[p[i+1]]
                    else: FOLLOW[x] |= FOLLOW[A]
                    changed |= len(FOLLOW[x])>old
def closure(I):
    I=set(I)
    while True:
        old=len(I)
        for A,p,d in list(I):
            if d<len(p) and p[d] in G:
                for q in G[p[d]]:
                    I.add((p[d],tuple(q),0))
        if len(I)==old: return frozenset(I)
def goto(I,x):
    J=[(A,p,d+1) for A,p,d in I if d<len(p) and p[d]==x]
    return closure(J) if J else None
C=[closure([("S",tuple(G["S"][0]),0)])]
trans={}
q=deque(C)
while q:
    I=q.popleft()
    i=C.index(I)
    for x in T[:-1]+NT:
        J=goto(I,x)
        if J:
            if J not in C:
                C.append(J); q.append(J)
            trans[(i,x)]=C.index(J)
ACTION=defaultdict(dict); GOTO=defaultdict(dict)
for i,I in enumerate(C):
    for A,p,d in I:
        if d<len(p) and p[d] in T:
            ACTION[i][p[d]]="s"+str(trans[(i,p[d])])
        elif d==len(p):
            if A=="S": ACTION[i]["$"]="acc"
            else:
                for a in FOLLOW[A]:
                    ACTION[i][a]="r("+A+"->"+" ".join(p)+")"
    for A in NT[1:]:
        if (i,A) in trans:
            GOTO[i][A]=trans[(i,A)]
print("\nFIRST SETS")
for A in NT:
    print(A,":",FIRST[A])
print("\nFOLLOW SETS")
for A in NT:
    print(A,":",FOLLOW[A])
cols=T+NT[1:]
print("\nSLR PARSING TABLE\n")
print("{:<6}".format("State"),end="")
for c in cols:
    print("{:<15}".format(c),end="")
print()
for i in range(len(C)):
    print("{:<6}".format(i),end="")
    for c in T:
        print("{:<15}".format(ACTION[i].get(c,"")),end="")
    for c in NT[1:]:
        print("{:<15}".format(GOTO[i].get(c,"")),end="")
    print()
def parse(expr):
    toks=[]
    for ch in expr:
        if ch.isalpha(): toks.append("id")
        elif ch in "+*()": toks.append(ch)
    toks.append("$")
    st=[0]; i=0
    while True:
        act=ACTION[st[-1]].get(toks[i])
        if not act: return False
        if act=="acc": return True
        if act[0]=="s":
            st += [toks[i],int(act[1:])]
            i+=1
        else:
            rule=act[2:-1]
            A,b=rule.split("->")
            b=b.split()
            st=st[:-2*len(b)]
            st += [A,GOTO[st[-1]][A]]
s=input("\nEnter expression: ")
print("\nValid Expression" if parse(s) else "\nInvalid Expression")
