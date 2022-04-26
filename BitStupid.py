global ACC

def BitStupid(program, acc, in_loop=False):
    ACC = acc
    program = program.split("\n")
    if type(program) == str: program = [program]
    if in_loop:
        while ACC == 1:
            for i in program:
                for j in range(len(i)):
                    if i[j] == ",": ACC = int(input("#: "))
                    elif i[j] == ".": print(ACC)
                    elif i[j] == ":": BitStupid(i[j+1:], ACC, in_loop=True)
    else:
        for i in program:
            for j in range(len(i)):
                if i[j] == ",": ACC = int(input("#: "))
                elif i[j] == ".": print(ACC)
                elif i[j] == ":": BitStupid(i[j+1:], ACC, in_loop=True)

BitStupid("Program Here", 0)


