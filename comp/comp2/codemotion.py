def codemotion(code):
    outside = []
    inside = []
    i = 0
    for lines in code:
        if 'for' in lines:
            i += 1
            inside.append(lines)
            break
        outside.append(lines)
        i += 1
    for lines in code[i:]:
        if 'i' not in lines and '=' in lines:
            outside.append(lines)
        else:
            inside.append(lines)
    return outside, inside
code = """
for i in range(n):
    x = x + 1
    y = x + z
"""
code = code.strip().split("\n")
outside, inside = codemotion(code)
print("Optimized Code:\n")
for line in outside:
    print(line)
for line in inside:
    print(line)