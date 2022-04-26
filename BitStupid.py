# Esolang Page: esolangs.org/wiki/Bit_Stupid

def BitStupid(program, in_loop=False, default_acc=0):
    acc = default_acc
    program = program.split("\n")
    if type(program) == str: program = [program]
    if in_loop:
        while acc == 1:
            for i in program:
                for j in range(len(i)):
                    if i[j] == ",": acc = int(input("#: "))
                    elif i[j] == ".": acc = print(acc)
                    elif i[j] == ":": acc = BitStupid(i[j+1:], True, acc)
    else:
        for i in program:
            for j in range(len(i)):
                if i[j] == ",": acc = int(input("#: "))
                elif i[j] == ".": acc = print(acc)
                elif i[j] == ":": acc = BitStupid(i[j+1:], True, acc)

BitStupid("Program Here!")
                    
