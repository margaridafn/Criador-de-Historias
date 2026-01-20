print(" * " * 10)
print("     Criador de Histórias     ")
print(" * " * 10, end="\n\n")

nome = input("Insira o nome do personagem principal: ")
lugar = input("Insira o local onde a história se passa: ")
adjetivo = input("Insira um adjetivo para descrever o personagem: ")
verbo = input("Insira um verbo sobre que o personagem faz: ")
tempo = input("Insira o tempo em que a história se passa: ", end="\n\n")

print("A criar a sua história...", end="\n\n")

print("Uma História em", lugar, sep="**", end="\n")
print("Era uma vez um(a)", adjetivo," chamado(a)", nome, end=" ")
print("que viajava por", lugar,", e que fazia", verbo + ".", end="\n")
print("Tudo isso aconteceu", tempo + ".", end="\n\n")