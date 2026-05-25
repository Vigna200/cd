import re
def constant_folding(code):
    lines = code.split("\n")
    result = []
    for line in lines:
        match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', line)
        if match:
            a = int(match.group(1))
            op = match.group(2)
            b = int(match.group(3))
            if op == '+':
                val = a + b
            elif op == '-':
                val = a - b
            elif op == '*':
                val = a * b
            elif op == '/':
                val = a // b   
            line = re.sub(r'(\d+)\s*([\+\-\*/])\s*(\d+)', str(val), line)
        result.append(line)
    return "\n".join(result)


# INPUT (FIXED)
code = """
x = 2 + 3
y = 4 * 5
z = x + y
"""

print("Original:\n", code)
print("Folded:\n", constant_folding(code))
