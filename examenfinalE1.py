# Escribir un programa el cual contendra el abecedario en un tipo de fato lista,
# Elimien de esta varibale las letras que ocupen posiciones que sean multiplos de 3, y pintar en pantalla el resultado

abcedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def multi3(n1):
    if n1 % 3 == 0:
        return True
    else:
        return False
p=0
for x in range(len(abcedario),1,-1):
    if multi3(x) == True:
        print("borrado:", abcedario[x])
        del abcedario[x]
    else:
        # print("no Borrados:",abcedario[x])
        pass
        
print("No borrado:",abcedario)