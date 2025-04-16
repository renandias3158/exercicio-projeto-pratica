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
'''arry = []
nome = []
idade = []
while True:
    name = input("Insira o nome (ou digite 'sair' para encerrar): ")
    if name.lower() == 'sair':
        break
    nome.append(name)
    age = int(input("Insira a idade (ou digite 0 para encerrar): "))
    if age == 0:
        break
    idade.append(age)
    arry.append((name, age))  
print("As idades e nomes inseridos foram:")
for n, i in arry:
    print(f"Nome: {n}, Idade: {i}")'''
'''questao 2'''
'''
soma = 0
for numero in range(1, 51):
    if numero % 2 == 0:
        soma += numero  
print("A soma dos números pares de 1 a 50 é:", soma)'''
'''questao 3'''
'''
total_homens = 0
total_mulheres = 0
menores_trabalhando = 0
soma_renda_homens = 0
soma_renda_mulheres = 0
menor_renda = float('inf')
nome_menor_renda = ""
total_nao_trabalham = 0
soma_idade = 0
total_pessoas = 0
while True:
    nome = input("Insira o nome (ou digite 'FIM' para encerrar): ")
    if nome.upper() == "FIM":
        break
    idade = int(input("Insira a idade (0 a 100): "))
    while idade < 0 or idade > 100:
        idade = int(input("Idade inválida. Insira a idade (0 a 100): "))
    sexo = input("Insira o sexo (M/F): ").upper()
    while sexo not in ['M', 'F']:
        sexo = input("Sexo inválido. Insira o sexo (M/F): ").upper()
    trabalha = input("Trabalha? (V/F): ").upper()
    while trabalha not in ['V', 'F']:
        trabalha = input("Resposta inválida. Trabalha? (V/F): ").upper()
    salario_minimos = float(input("Quantos salários mínimos recebe por mês? "))
    if sexo == 'M':
        total_homens += 1
        soma_renda_homens += salario_minimos
    else:
        total_mulheres += 1
        soma_renda_mulheres += salario_minimos
    if idade < 18 and trabalha == 'V':
        menores_trabalhando += 1
    if trabalha == 'V' and salario_minimos < menor_renda:
        menor_renda = salario_minimos
        nome_menor_renda = nome
    if trabalha == 'F':
        total_nao_trabalham += 1
    soma_idade += idade
    total_pessoas += 1
media_idade = soma_idade / total_pessoas if total_pessoas > 0 else 0
media_renda_homens = soma_renda_homens / total_homens if total_homens > 0 else 0
media_renda_mulheres = soma_renda_mulheres / total_mulheres if total_mulheres > 0 else 0
print("\nResultados da pesquisa:")
print(f"Quantidade de homens entrevistados: {total_homens}")
print(f"Quantidade de mulheres entrevistadas: {total_mulheres}")
print(f"Quantidade de pessoas menores de 18 anos que trabalham: {menores_trabalhando}")
print(f"Renda média dos homens: {media_renda_homens:.2f} salários mínimos")
print(f"Renda média das mulheres: {media_renda_mulheres:.2f} salários mínimos")
print(f"Nome e renda da pessoa que trabalha e que tem a menor renda: {nome_menor_renda}, {menor_renda:.2f} salários mínimos")
print(f"Quantidade de pessoas que não trabalham: {total_nao_trabalham}")
print(f"Média de idade dos entrevistados: {media_idade:.2f} anos")'''
'''questao 4'''
