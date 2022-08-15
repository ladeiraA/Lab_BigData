import statistics

def ler_fasta(arquivo):
    sequencia = ''
    lista = []
    with open(arquivo, 'r') as fasta:
            sequencia = ''
            for linha in fasta:
                if not linha.startswith('>'):
                    sequencia += linha
            lista.append(sequencia)
    return lista

# testando...
print("Executando")
lista = ler_fasta("sequence.fasta")
lista = "".join(lista)

A = 0
C = 0
T = 0
G = 0
for i in lista:
    if i == "A":
        A = A + 1
    if i == "C":
        C = C + 1
    if i == "T":
        T = T + 1
    if i == "G":
        G = G + 1


print("Letra A é repetida:",A,"e sua media é:",(A/(A + C + T + G)))
print("-")
print("Letra C é repetida:",C,"e sua media é:",(C/(A + C + T + G)))
print("-")
print("Letra T é repetida:",T,"e sua media é:",(T/(A + C + T + G)))
print("-")
print("Letra G é repetida:",G,"e sua media é:",(G/(A + C + T + G)))
