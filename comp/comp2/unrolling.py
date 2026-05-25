import re
def loop_unrolling(code):
    lines = code.split("\n")
    result = []
    for i in range(len(lines)):
        line = lines[i]
        if "for" in line and "range" in line:
            indent = len(line) - len(line.lstrip())
            n = int(re.search(r'range\((\d+)\)', line).group(1))
            body = lines[i + 1].strip()
            j = 0
            while j < n:
                result.append(" " * indent + re.sub(r'\bi\b', str(j), body))
                if j + 1 < n:
                    result.append(" " * indent + re.sub(r'\bi\b', str(j + 1), body))
                j += 2
        else:
            result.append(line)
    return "\n".join(result)
# INPUT
code = """
n = 4
for i in range(4):
    print(i)
"""
print("Original Code:\n", code)
print("Unrolled Code:\n", loop_unrolling(code))
