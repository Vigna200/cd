def symbol_table():
    table = {}
    mem = 1000
    keywords = {
        "int":"int",
        "float":"float",
        "char":"char",
        "double":"double"
    }
    while True:
        ch = input("\n1.Insert 2.Delete 3.Search 4.Display 5.Exit : ")
        if ch == '1':
            name = input("Enter lexeme: ")
            if name in table:
                print("Already exists")
            else:
                if name in keywords:
                    table[name] = ("Keyword", keywords[name], "-")
                else:
                    dtype = input("Enter datatype: ")
                    table[name] = ("Identifier", dtype, mem)
                    mem += 4
                print("Inserted")
        elif ch == '2':
            name = input("Enter lexeme to delete: ")
            if name in table:
                del table[name]
                print("Deleted")
            else:
                print("Not found")
        elif ch == '3':
            name = input("Enter lexeme to search: ")
            if name in table:
                v = table[name]
                print(f"{name} -> Category:{v[0]}, Datatype:{v[1]}, Memory:{v[2]}")
            else:
                print("Not found")
        elif ch == '4':
            print("\n{:<10} {:<12} {:<10} {:<10}".format(
                "Lexeme","Category","Datatype","Memory"))
            print("-"*45)
            for k,v in table.items():
                print("{:<10} {:<12} {:<10} {:<10}".format(
                    k,v[0],v[1],v[2]))
        elif ch == '5':
            break
        else:
            print("Invalid choice")
symbol_table()
