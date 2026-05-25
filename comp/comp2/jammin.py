def loop_jamming(code):
    lines = code.strip().split("\n")
    loops = {}
    result = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("for"):
            loop = line
            body = []
            i += 1
            while i < len(lines) and lines[i].startswith("    "):
                body.append(lines[i])
                i += 1
            if loop not in loops:
                loops[loop] = []
            loops[loop].extend(body)
        else:
            result.append(lines[i])
            i += 1
    for loop, body in loops.items():
        result.append(loop)
        result.extend(body)
    return "\n".join(result)
code = """
for i in range(3):
    print(i)

for i in range(3):
    print(i*i)

for i in range(3):
    print(i+1)
"""
print(loop_jamming(code))