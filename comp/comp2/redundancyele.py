def redundancy_elimination(code):
    lines = code.split("\n")
    result = []
    seen = {}   # store computed expressions
    for line in lines:
        if "=" in line:
            left, right = line.split("=")
            left = left.strip()
            right = right.strip()

            # if already computed → reuse
            if right in seen:
                result.append(f"{left} = {seen[right]}")
            else:
                seen[right] = left
                result.append(line)
        else:
            result.append(line)
    return "\n".join(result)

# INPUT
code = """
a = 5
b = 10
x = a + b
y = a + b
z = x + y
"""

print("Original:\n", code)
print("Optimized:\n", redundancy_elimination(code))
