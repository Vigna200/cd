from collections import defaultdict,deque
# ---------- GRAMMAR ----------
G = {
"E'":[["E"]],   # augmented grammar
"E":[["E","+","T"], ["T"]],     # 1, 2
"T":[["T","*","F"], ["F"]],     # 3, 4
"F":[["(","E",")"], ["id"]]     # 5, 6
}
NT = list(G.keys())
T = ["id","+","*","(",")","$","ε"]
FIRST = defaultdict(set)
FOLLOW= defaultdict(set)
# ---------- FIRST ----------
def compute_first():
    # FIRST of terminals
    for t in T:
        FIRST[t].add(t)
    changed = True
    while changed:
        changed = False
        for A in G:                 # for each non-terminal
            for p in G[A]:          # for each production A → p
                before = len(FIRST[A])
                # go through symbols in production
                for symbol in p:
                    # add FIRST(symbol) except epsilon
                    FIRST[A] |= (FIRST[symbol] - {"ε"})
                    # if epsilon not in FIRST(symbol), stop
                    if "ε" not in FIRST[symbol]:
                        break
                else:
                    # if all symbols had epsilon
                    FIRST[A].add("ε")
                if len(FIRST[A]) > before:
                    changed = True
compute_first()
# ---------- FOLLOW ----------
# Start symbol
FOLLOW["E'"].add("$")
def compute_follow():
    changed = True
    while changed:
        changed = False
        for A in G:                  # for each production A → p
            for p in G[A]:
                for i, B in enumerate(p):
                    if B in NT:      # only for non-terminals
                        old = len(FOLLOW[B])
                        # Case 1: something after B
                        if i + 1 < len(p):
                            next_symbol = p[i+1]
                            # add FIRST(next) except epsilon
                            FOLLOW[B] |= (FIRST[next_symbol] - {"ε"})
                            # if epsilon in FIRST(next)
                            if "ε" in FIRST[next_symbol]:
                                FOLLOW[B] |= FOLLOW[A]
                        # Case 2: B is last
                        else:
                            FOLLOW[B] |= FOLLOW[A]
                        if len(FOLLOW[B]) > old:
                            changed = True
compute_follow()
# ---------- CLOSURE ----------
def closure(items):
    items = set(items)
    while True:
        new = set(items)
        for A, body, dot in items:
            if dot < len(body):
                B = body[dot]
                if B in G:
                    for p in G[B]:
                        new.add((B, tuple(p), 0))
        if new == items:
            return items
        items = new
# ---------- GOTO ----------
def goto(I, X):
    move = set()
    for A, body, dot in I:
        if dot < len(body) and body[dot] == X:
            move.add((A, body, dot + 1))
    return closure(move) if move else set()
# ---------- STATES ----------
start = closure([("E'", tuple(G["E'"][0]), 0)])
states = [start]
q = deque([start])
trans = {}
symbols = ["E","T","F","id","+","*","(",")"]
while q:
    I = q.popleft()
    i = states.index(I)
    for X in symbols:
        g = goto(I, X)
        if g:
            if g not in states:
                states.append(g)
                q.append(g)
            trans[(i,X)] = states.index(g)
# ---------- PARSING TABLE ----------
ACTION = defaultdict(dict)
GOTO = defaultdict(dict)
for i,I in enumerate(states):
    for A,body,dot in I:
        # SHIFT
        if dot < len(body):
            a = body[dot]
            if a in T and (i,a) in trans:
                ACTION[i][a] = "s" + str(trans[(i,a)])
        # REDUCE / ACCEPT
        else:
            if A == "E'":
                ACTION[i]["$"] = "acc"
            else:
                for a in FOLLOW[A]:
                    ACTION[i][a] = "r(" + A + "→" + " ".join(body) + ")"
    # GOTO
    for A in NT:
        if (i,A) in trans:
            GOTO[i][A] = trans[(i,A)]
# ---------- PRINT TABLE ----------
print("\nSLR Parsing Table")
print("State | " + " | ".join(T + NT[1:]))
for i in range(len(states)):
    row = [str(i)]
    for t in T:
        row.append(ACTION[i].get(t," "))
    for nt in NT[1:]:
        row.append(str(GOTO[i].get(nt," ")))
    print(" | ".join(row))
# ---------- VALIDATION ----------
def valid(expr):
    tokens = []
    for c in expr:
        if c.isalpha():
            tokens.append("id")
        elif c in "+*()":
            tokens.append(c)
    tokens.append("$")
    stack = [0]
    i = 0
    print("\nParsing Steps:\n")
    while True:
        state = stack[-1]
        cur = tokens[i]
        act = ACTION[state].get(cur)
        # ✅ PRINT STEP
        print("Stack:", stack, " Input:", tokens[i:], " Action:", act)
        if not act:
            return False
        if act == "acc":
            return True
        # SHIFT
        if act[0] == "s":
            stack.append(cur)
            stack.append(int(act[1:]))
            i += 1
        # REDUCE
        else:
            rule = act[2:-1]
            A,body = rule.split("→")
            body = body.split()
            stack = stack[:-2*len(body)]
            state = stack[-1]
            stack.append(A)
            stack.append(GOTO[state][A])
# ---------- INPUT ----------
while True:
    s = input("\nEnter expression (or exit): ")
    if s == "exit":
        break
    print("VALID" if valid(s) else "INVALID")