### Definição de Listas : Um objeto que é representado por uma sequência de outros objetos. 
### Separados por virgula, e são iniciados e terminados por []

### Criando listas : 

lst1 = [1, 2, 3, 4, 5,1,1,1]
lst2 = [6, 7, 8, 9]
lst3 = [10, 11, 12, 13, 14, 15]
lst4=[16,17,18,19,21,20]
lst5=[]

# Determinando o número de elementos em cada lista
num_elementos_lst1 = len(lst1)
num_elementos_lst2 = len(lst2)
num_elementos_lst3 = len(lst3)
num_elementos_lst4 = len(lst4)
num_elementos_lst5 = len(lst5)

# Imprimindo o número de elementos em cada lista
print("Número de elementos em lst1:", num_elementos_lst1)
print("Número de elementos em lst2:", num_elementos_lst2)
print("Número de elementos em lst3:", num_elementos_lst3)
print("Número de elementos em lst2:", num_elementos_lst4)
print("Número de elementos em lst3:", num_elementos_lst5)

for element in range(4):
    print(element)
    if element !=0:
        lst5.append(element)
    print(lst5)

### Colocando valores diferentes em listas:

lst6=['a','b','c','d','e']
lst7=[1,3,5,7,'z']

print("Acessando valores na lista:")
#Acessando valores na lista: 
print(lst6[0])
print(lst7[3])

### Juntando listas:

print(lst4)
print(lst5)
print("Juntando as duas listas:")
print(lst4+lst5)

print("Verificando se um objeto pertence a lista")
## Verificando se um objeto pertence a lista:
check = "A" in lst6
print(check)

### Verificando se um elemento esta contido em alguma das listas: 
print("Verifique se o número esta presente em alguma das listas: \n")
def verificar_numero():
    # Solicita ao usuário para digitar um número
    numero = int(input("Digite um número para verificar se pertence a alguma das listas de 1 a 6: "))
    
    # Verifica em qual lista o número está presente
    if numero in lst1:
        print(f"O número {numero} está na lista 1.")
    elif numero in lst2:
        print(f"O número {numero} está na lista 2.")
    elif numero in lst3:
        print(f"O número {numero} está na lista 3.")
    elif numero in lst4:
        print(f"O número {numero} está na lista 4.")
    elif numero in lst5:
        print(f"O número {numero} está na lista 5.")
    elif numero in lst6:
        print(f"O número {numero} está na lista 6.")
    else:
        print(f"O número {numero} não está em nenhuma das listas.")

# Chamada da função
verificar_numero()

### Métodos:

### Método Pop: Responsável por remover elementos da lista, 
#se você não colocar a ordem que ele quer remover ele vai remover o último elemento da lista
print(lst5)
print(lst5.pop())
print(lst5)

### Método remove: Responsável por remover elementos da lista,
# você so precisa colocar o parametro do que quer remover e ele vai na posição exata

print(lst5)
print(lst5.remove(2))
print(lst5)


### Método sort: Ordenar listas em Python 

print(lst4)
print(lst4.sort())
print(lst4)

### Método count: Ver quantas vezes aquele elemento aparece:

print(lst1)
print(lst1.count(1))
