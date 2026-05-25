def peephole(code):
    lines = code.split("\n")
    res = []
    for line in lines:
        if "+ 0" in line:
            line = line.replace("+ 0", "")
        elif "* 1" in line:
            line = line.replace("* 1", "")
        res.append(line)
    return "\n".join(res)
code = """
a = b + 0
c = d * 1
e = a + c
"""
print("Optimized Code:\n")
print(peephole(code))