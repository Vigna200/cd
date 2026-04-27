def loop_jamming(code):
    lines = code.split("\n")
    result = []

    i = 0
    while i < len(lines):

        # check first loop
        if lines[i].strip().startswith("for"):
            loop1 = lines[i]
            body1 = lines[i + 1].strip()

            # find next non-empty line
            j = i + 2
            while j < len(lines) and lines[j].strip() == "":
                j += 1

            # check second loop
            if j < len(lines) and lines[j].strip().startswith("for"):
                loop2 = lines[j]
                body2 = lines[j + 1].strip()

                # if both loops are same → jam them
                if loop1.strip() == loop2.strip():
                    result.append(loop1)
                    result.append("    " + body1)
                    result.append("    " + body2)

                    i = j + 2
                    continue

        # normal line
        result.append(lines[i])
        i += 1

    return "\n".join(result)


# INPUT
code = """
for i in range(3):
    print(i)

for i in range(3):
    print(i*i)
"""

print("Original Code:\n", code)
print("Jammed Code:\n", loop_jamming(code))
