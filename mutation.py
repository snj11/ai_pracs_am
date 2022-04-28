import random

gene = input("Enter genes in binary representation: ")
mutation_prob = float(input("Enter mutation probability: "))
n = len(gene)
str = ""
for i in range(n):
    random_prob = random.random()
    if random_prob > mutation_prob:
        str+="1"
    else:
        str+="0"
print("Probability vector : ", str)
for i in range(len(gene)):
    if str[i] == "1":
        if gene[i] == "1":
            gene = gene[:i] + "0" + gene[i+1:]
        else:
            gene = gene[:i] + "1" + gene[i+1:]
print("New gene : ", gene)

