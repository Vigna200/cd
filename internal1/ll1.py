from collections import defaultdict

grammar={
"E":[["T","E'"]],
"E'":[["+", "T","E'"],["ε"]],
"T":[["F","T'"]],
"T'":[["*","F","T'"],["ε"]],
"F":[["(","E",")"],["id"]]
}

terminals=["id","+","*","(",")","$"]
non_terminals=["E","E'","T","T'","F"]

FIRST=defaultdict(set)
FOLLOW=defaultdict(set)

def compute_first():
    for t in terminals:
        FIRST[t].add(t)

    changed=True

    while changed:
        changed=False

        for head,prods in grammar.items():
            for prod in prods:
                before=len(FIRST[head])

                FIRST[head]|=FIRST[prod[0]]

                if "ε" in FIRST[prod[0]] and len(prod)>1:
                    FIRST[head]|=FIRST[prod[1]]

                if len(FIRST[head])>before:
                    changed=True

def compute_follow():
    FOLLOW["E"].add("$")

    changed=True

    while changed:
        changed=False

        for head,prods in grammar.items():
            for prod in prods:
                for i,sym in enumerate(prod):

                    if sym in non_terminals:

                        before=len(FOLLOW[sym])

                        if i+1<len(prod):
                            FOLLOW[sym]|=FIRST[prod[i+1]]-{"ε"}
                        else:
                            FOLLOW[sym]|=FOLLOW[head]

                        if len(FOLLOW[sym])>before:
                            changed=True

compute_first()
compute_follow()

table={nt:{t:"" for t in terminals} for nt in non_terminals}

for head,prods in grammar.items():
    for prod in prods:

        first_set=FIRST[prod[0]]

        for t in first_set-{"ε"}:
            table[head][t]=head+" -> "+" ".join(prod)

        if "ε" in first_set:
            for t in FOLLOW[head]:
                table[head][t]=head+" -> ε"

print("\nLL(1) Parsing Table:\n")

print("{:<8}".format("NT"),end="")
for t in terminals:
    print("{:<20}".format(t),end="")
print()

for nt in non_terminals:
    print("{:<8}".format(nt),end="")
    for t in terminals:
        print("{:<20}".format(table[nt][t]),end="")
    print()