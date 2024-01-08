### Definição: É um objeto que representa a coleção de um ou mais objetos.
#Cada objeto tem a sua chave e valor.Assim para acessar cada valor de determinado objeto,
#basta chamarmos sua chave. Os dicionários são iniciados e terminados por chave {}

### Criando Dicionários:

dict1={'chave1':'valor1',
       'chave2':'valor2',
       'chave3':'valor3'}

#Checkar se realmente é um dicionário:
print(type(dict1))

#Aqui declaramos o que é a chave e qual é o seu valor:

dict2=dict(a=1,
           b=2,
           c=3,
           d='a')

#Declaramos uma lista de tuplas:

### Definição de tuplas: Tuplas são bem similares as listas em questão de definição 
# entretando existe uma discrepancia aparente e que tuplas são imutaveis 

dict3 = [('a', 1), ('b', 2), ('c', 3)]

# Convertendo a lista de tuplas em um dicionário
dict3_formatted = dict(dict3)


dict4={'chave1':['valor1',2,3],
       'chave2':[2,'idade','nome']}

dict5={'id':[1,2,3],
       'user':{'nome':['Caio','Rodrigo','Rafael'],
               'idade':[29,30,29]}}

dict6=dict(zip(['chave1','chave2','chave3'],
               ['valor1','valor2','valor3']))

dict7 = {'nomes': ('Caio', 'Rafael'),
         'idade': (29, 30)}

### Acessando valores do dicionário: 

# Get () é um método usado para pegar o valor de uma dada chave em um dicionário
# se a chave estiver no dicionário, 
#caso ela não exista, o método retorna None ou o valor padrão passado por parâmetro

print(dict1.get('chave2'))

for chave in dict1.keys():
    print(chave, dict1[chave])

### Juntando dicionário:
    
#Método Update: atualiza um dicionário adicionando pares chave-valor
    # de outro dicionário ou de uma sequência de pares chave-valor

dict1.update(dict2)

 #Adicionando uma nova chave:

dict1["NOVA CHAVE"]=1000

#Adicionando uma nova chave com UPDATE:

dict1.update({'OTHER KEY':'OTHER KEY'})

### Métodos:

dict2.clear()
print(dict2)