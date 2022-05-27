#########################################################################
#                   Prof. Nuncio Perrella                               #
#                   Instituto Mauá de Tecnologia                        #
#                   Assemblador para Processador BIP                    #
#                   Maio 2022                                           #
#########################################################################

i=0
file1 = open('code_imt.txt', 'r')

Lines = file1.readlines()
file = open('code_imt.txt', 'w')

n =int( input(" Até qual numero? :"))
t1 = 0
t2 = 1
t3 = 0

while t3 <= n:
    file.write(str(hex(t3)[2:])+"\n")
    print(hex(t3)[2:])
    
    t3 = t1 + t2
    t1 = t2
    t2 = t3

result = open('asmimt.cdm', 'w')

conversion = {"HLT":" : 00",
              "STO":" : 1",
              "LD":" : 2",
              "LDI":" : 3",
              "ADD":" : 4",
              "ADDI":" : 5",
              "SUB":" : 6",
              "SUBI":" : 7"}

count = 0
n = 0
# Strips the newline character
for line in Lines:
    try:
        split = line.strip().split(" ")
        result.write(str(hex(n)).upper()[2:] + conversion[split[0]] + split[1] + "\n")
        print(line.strip())
        n = n+1
    except:
        pass
result.close()