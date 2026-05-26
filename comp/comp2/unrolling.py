def loop_unrolling(code):
    lines = code.strip().split("\n")
    result = []

    for i in range(len(lines)):
        line = lines[i]

        if line.startswith("for") and "range" in line:
            n = int(line.split("range(")[1].split(")")[0])

            body = lines[i + 1].strip()

            for j in range(n):
                result.append(body.replace("i", str(j)))
        elif not line.startswith("print"):
            result.append(line)

    return "\n".join(result)


code = """
for i in range(4):
    print(i)
"""

print(loop_unrolling(code))