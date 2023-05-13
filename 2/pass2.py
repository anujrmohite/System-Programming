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
symbol = []
symbolValue = []
lc = 0
current = 0
count = 0
temp = []
n = int(input("Enter the no of instruction lines : "))
for i in range(n):
    instructions = input("Enter instruction line {} : ".format(i + 1))
    l.append(instructions)
l = [x.upper() for x in l]
for i in range(n):
    x = l[i]
    if "NEXT:" in x:
        s1 = ''.join(x)
        a, b, c = s1.split()
        a = a[:4]
        l[i] = b + " " + c
        symbol.append(a)
        x = l[i]
        if b in motOpCode:
            value = motOpCode.get(b)
            size = motSize.get(b)
            if len(str(size)) == 1:
                temp = "000" + str(size)
            elif len(str(size)) == 2:
                temp = "00" + str(size)
            elif len(str(size)) == 3:
                temp = "0"+str(size)
        else:
            print("Instruction is not in Op Code.")
            exit(0)
        symbolValue.append(temp)
        previous = size
        lc += current
        current = previous
        locationcounter.append(lc)
        if c.isalpha() is True:
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
    elif " " in x:
        s1 = ''.join(x)
        a, b = s1.split()
        if a in motOpCode:
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
            print("Instruction is not in Op Code.")
            exit(0)
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
            print("Instruction is not in Op Code.")
            exit(0)
print("Symbol Table  :  \n")
print("\n Symbol           Value(Address)")
for i in range(len(symbol)):
    print(" {}              {}".format(symbol[i], symbolValue[i]))

print("\n Pass-1 machine code output without reference of the symbolic address : \n")
print("Relative Address	Instruction	    OpCode")
for i in range(n):
    if "NEXT" in l[i]:
        print("{}                                 {}	              {}, - ".format(
            locationcounter[i], l[i], machineCode[i]))
    else:
        print("{}                                 {}	              {} ".format(
            locationcounter[i], l[i], machineCode[i]))

print("\n Pass-2 output: Machine code output \n ")
print("Relative Address	Instruction	    OpCode")
for i in range(n):
    if "NEXT" in l[i]:
        for j in range(len(symbol)):
            if "NEXT" in symbol[j]:
                pos = j
                print("{}                                 {}	              {} , {}".format(
                    locationcounter [i], l[i], machineCode[i], symbolValue[pos]))
    else:
        print("{}                                 {}	              {} ".format(
            locationcounter[i], l[i], machineCode[i]))

