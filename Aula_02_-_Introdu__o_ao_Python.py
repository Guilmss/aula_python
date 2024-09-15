# exercio 1
pessoa = {}

nome = input("digite o primeiro nome: ")
pessoa["nome"] = nome

ultimo_nome = input("digite o ultimo nome: ")
pessoa["ultimo_nome"] = ultimo_nome

idade = int(input("digite idade: "))
pessoa["idade"] = idade

curso = input("nome do curso: ")
pessoa["curso"] = curso

endereco = input("digite endereço: ")
pessoa["endereco"] = endereco

op = input("o que você quer saber sobre a pessoa ? ")

print(pessoa[op])



# questão A
print(pessoa)

# questão B
print(pessoa["nome"])
print(pessoa["ultimo_nome"])
print(pessoa["idade"])
print(pessoa["curso"])
print(pessoa["endereco"])

# questão C
del pessoa['curso']

# questão D
pessoa["ultimo_nome"] = "lopes"

# questão E
print(pessoa)

# questão F
print(pessoa["endereco"])

# questão G
pessoa2 = pessoa.copy()
pessoa2["nome"] = "seila"
pessoa2["idade"] = 40

# questão H
print(pessoa2)