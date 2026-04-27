import re
def fold(code):
    lines=code.split('\n')
    res=[]
    for line in lines:
        match=re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)',line)
        if match:
            a=int(match.group(1))
            op=match.group(2)
            b=int(match.group(3))
            if op=='+':
                val=a+b
            elif op=='-':
                val=a-b
            elif op=='*':
                val=a*b
            else:
                val=a//b
            line=re.sub(r'(\d+)\s*([\+\-\*/])\s*(\d+)',str(val),line)
        res.append(line)
    return '\n'.join(res)
# INPUT (FIXED)
code = """
x = 2 + 3
y = 4 * 5
z = x + y
"""

print("Original:\n", code)
print("Folded:\n", fold(code))
