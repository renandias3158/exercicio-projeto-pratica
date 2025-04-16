#exercicio sobre condicionais:
"""questao 1 """
"""
numero = input("insira um numero\n-")
int(numero)
calculo = numero % 2
if calculo != 0:
    print("o numero é impar!")
elif calculo == 0:
    print("o numero é par!")
#end file;
"""
"""questao 2"""
"""
media1 = input("insira a sua primeira nota\n-")
float(media1)
media2 = input("insira a sua segunda nota\n-")
float(media2)
media3 = input("insira a sua terceira nota\n-")
float(media3)
calc = (media1 + media2 + media3 / 3)
if calc < 4:
    print("voce esta reprovado!")
elif calc >= 4 and calc < 7:
    print("voce terá que fazer a prova final!")
elif calc > 7:
    print("voce esta aprovado!")
"""
"""questao 3"""
"""
idade = input("qual a sua idade, nadador?")
int(idade)
if idade >= 5 and idade <= 7:
    print("a sua categoria é a Junior!")
elif idade >= 8 and idade <= 12:
    print("a sua categoria é a Infantil!")
elif idade >= 13 and idade <= 18:
    print("a sua categoria é a Pré!")
elif idade >18:
    print("a sua categoria é a Avançada!")
"""
"""questao 4"""
'''
valor1 = input("qual o primeiro valor?\n-->")
float(valor1)
operador = input("escolha um operador:\nsoma = 1\nsubtracao = 2\ndivisao = 3\nmultiplicao = 4 \n-->")
int(operador)
valor2 = input("qual o segundo valor\n-->")
float(valor2)
if operador == 1:
    print(valor1 + valor2)
elif operador == 2:
    print(valor1 - valor2)
elif operador == 3:
    divisao = print(valor1 / valor2)
    if divisao == 0:
        print("valor INVALIDO!")
elif operador == 4:
    print(valor1*valor2)
elif operador != (1,2,3,4):
    print("operador INVALIDO")
'''
'''questao 5'''
'''arry = []
valor1 = input("insira o primeiro valor!\n-->")
float(valor1)
valor2 = input("insira o segundo valor!\n-->")
float(valor2)
valor3 = input("insira o terceiro valor!\n-->")
arry.append(valor1,valor2,valor3)
arry.sort()
print(arry)'''
'''questao 6'''
'''
valor = input("insira um numero entre 20 e 39!\n-->")
int(valor)
if valor < 20 or valor > 39:
    print("Valor inválido!!")
elif valor == 20:
    print("vinte")
elif valor == 21:
    print("vinte e um")
elif valor == 22:
    print("vinte e dois")
elif valor == 23:
    print("vinte e trés")
elif valor == 24:
    print("vinte e quatro")
elif valor == 25:
    print("vinte e cinco")
elif valor == 26:
    print("vinte e seis")
elif valor == 27:
    print("vinte e sete")
elif valor == 28:
    print("vinte e oito")
elif valor == 29:
    print("vinte e nove")
elif valor == 30:
    print(("trinta")
elif valor == 31:
    print("trinta e um")
elif valor == 32:
    print("trinta e dois")
elif valor == 33:
    print("trinta e trés")
elif valor == 34:
    print("trinta e quatro")
elif valor == 35:
    print("trinta e cinco")
elif valor == 36:
    print("trinta e seis")
elif valor == 37:
    print("trinta e sete")
elif valor == 38:
    print("trinta e oito")
elif valor == 39:
    print("trinta e nove")'''
'''questao 7'''
'''
valor = int(input("Insira o valor: ")) 
cont = 1
fatorial = 1  
if valor < 0:
    print("Fatorial não é definido para números negativos.")
elif valor == 0:
    print("O fatorial de 0 é igual a 1.")
else:
    while cont <= valor:
        fatorial *= cont 
        cont += 1  
    print(f"O valor em fatorial é igual a: {fatorial}") '''
#repetições
'''questao 1'''
arry = []
nome = []
idade = []
while idade != 0:
    name = input("insira o nome!")
    nome.append(name)
    nome.sort()
    age = int(input("insira a idade!"))
    idade.append(age)
    idade.sort()
    arry.append(nome,idade)
print("as idades e nomes insirados foram:\n-->{arry}")
