def strength_reduction(code):
    lines=code.split("\n")
    res=[]
    for line in lines:
        if '=' in line and '*' in line:
            l,r=line.split('=')
            l=l.strip()
            r=r.strip()
            parts=r.split('*')
            if len(parts)==2:
                var=parts[0].strip()
                num=parts[1].strip()
                if num.isdigit():
                    num=int(num)
                    expr='+'.join([var]*num)
                    res.append(f'{l} = {expr}')
            else:
                res.append(line)
        else:
            res.append(line)
    return '\n'.join(res)
code = """
for i in range(3):
    y = i * 4
"""
print("Original:\n", code)
print("Optimized:\n", strength_reduction(code))
