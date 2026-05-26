def loop_jamming(code):
    lines = code.strip().split("\n")
    loops = {}
    
    for line in lines:
        if line.startswith("for"):
            current_loop = line
            loops[current_loop] = []
        else:
            loops[current_loop].append(line)

    result = []

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