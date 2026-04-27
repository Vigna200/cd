# Peephole Optimization in Python
def peephole_optimize(code):
    optimized = []
    for line in code:
        line = line.strip()
        # Remove useless operations
        if "+ 0" in line:
            line = line.replace(" + 0", "")
        if "- 0" in line:
            line = line.replace(" - 0", "")
        if "* 1" in line:
            line = line.replace(" * 1", "")
        if "/ 1" in line:
            line = line.replace(" / 1", "")
        # Multiplication by 2 -> addition
        if "* 2" in line:
            parts = line.split("=")
            left = parts[0].strip()
            right = parts[1].replace("* 2", "").strip()
            line = f"{left} = {right} + {right}"
        # Remove multiplication by 0
        if "* 0" in line:
            left = line.split("=")[0].strip()
            line = f"{left} = 0"
        # Remove duplicate consecutive instructions
        if optimized and optimized[-1] == line:
            continue
        optimized.append(line)
    return optimized
# Input intermediate code
code = [
    "a = b + 0",
    "c = d * 1",
    "e = f * 2",
    "g = h * 0",
    "x = y - 0",
    "z = k / 1",
    "m = n + 0",
    "m = n + 0"
]

print("Original Code:")
for line in code:
    print(line)

optimized_code = peephole_optimize(code)

print("\nOptimized Code:")
for line in optimized_code:
    print(line)