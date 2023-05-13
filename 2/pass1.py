from sys import exit
motOpCode = {
    "MOV": 1,
    "ADD": 2,
    "SUB": 3,
    "MUL": 4,
    "DIV": 5,
    "AND": 6,
    "OR": 7,
    "LOAD": 8,
    "STORE": 9,
    "JMP": 10,
    "JNZ": 11,
    "HALT": 12
}

motSize = {
    "MOV": 1,
    "ADD": 1,
    "SUB": 2,
    "MUL": 2,
    "DIV": 2,
    "AND": 2,
    "OR ": 2,
    "LOAD": 3,
    "STORE": 3,
    "JMP": 3,
    "JNZ": 3,
    "HALT": 1
}

l = []
locationcounter = []
machineCode = []
lc = 0
current = 0
count = 0
n = int(input("Enter the no of instruction lines : "))
for i in range(n):
    instructions = input("Enter instruction line {} : ".format(i + 1))
    l.append(instructions)
l = [x.upper() for x in l]
for i in range(n):
    x = l[i]
    if " " in x:
        s1 = ''.join(x)
        a, b = s1.split()
        if a in motOpCode:		# Check if Mnemonics is present in MOT or not
            value = motOpCode.get(a)
            size = motSize.get(a)
            previous = size
            lc += current
            current = previous
            locationcounter.append(lc)
            if b.isalpha() is True:
                machineCode.append(str(value))
            else:
                temp = list(b)
                for i in range(len(temp)):
                    if count == 2:
                        temp.insert(i, ',')
                        count = 0
                    else:
                        count = count + 1
                s = ''.join(temp)
                machineCode.append(str(value) + "," + s)
        else:
            print("Instruction is not in Op Code Table.")
            exit(0)				# EXIT if Mnemonics is not in MOT
    else:
        if x in motOpCode:
            value = motOpCode.get(x)
            size = motSize.get(x)
            previous = size
            lc += current
            current = previous
            locationcounter.append(lc)
            machineCode.append(value)
        else:
            print("Instruction is not in Op Code Table.")
            exit(0)

print("Location counter 	Instruction	    OpCode")
for i in range(n):
    print("{}                 {}          {}".format(locationcounter[i], l[i], machineCode[i]))