
def add_line_numbers(code):
    lines = code.strip().splitlines()
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line}")
        
code = """
x = 10
y = 20
print(x + y)
"""

print("Code with Line Numbers:\n")
add_line_numbers(code)
