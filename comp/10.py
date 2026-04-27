import re
def optimize_code_motion(code):
    lines = code.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # check for loop
        if line.strip().startswith("for"):
            indent = len(line) - len(line.lstrip())
            loop_var = re.findall(r'for (\w+)', line)[0]
            body = []
            i += 1
            # collect loop body
            while i < len(lines) and (len(lines[i]) - len(lines[i].lstrip()) > indent):
                body.append(lines[i])
                i += 1
            invariant = []
            variant = []
            # separate invariant and variant
            for stmt in body:
                if "=" in stmt and loop_var not in stmt:
                    invariant.append(stmt.strip())
                else:
                    variant.append(stmt)
            # move invariant outside loop
            for stmt in invariant:
                result.append(" " * indent + stmt)
            result.append(line)
            result.extend(variant)
            continue  # skip normal increment
        else:
            result.append(line)
        i += 1
    return "\n".join(result)


# INPUT
code = """
n = 5
a = 10
b = 20
for i in range(n):
    y = a * b
    z = y + i
    print(z)
"""

print("Original Code:\n", code)
print("Optimized Code:\n", optimize_code_motion(code))
