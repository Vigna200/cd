def strength_reduction(code):
    lines = code.split("\n")
    result = []
    for line in lines:
        if "=" in line and "*" in line:
            left, right = line.split("=")
            left = left.strip()
            right = right.strip()
            parts = right.split("*")
            if len(parts) == 2:
                var = parts[0].strip()
                num = parts[1].strip()
                if num.isdigit():
                    n = int(num)
                    new_expr = " + ".join([var] * n)
                    result.append(f"{left} = {new_expr}")
                    continue
        result.append(line)
    return "\n".join(result)
# INPUT
code = """
for i in range(3):
    y = i * 4
"""
print("Original:\n", code)
print("Optimized:\n", strength_reduction(code))
