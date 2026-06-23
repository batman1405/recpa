# QUESTÃO 04 – Fatorial (4 pontos)
# ---------------------------------------------------------

# Solicite ao usuário um número inteiro positivo e calcule
# seu fatorial utilizando um laço de repetição.

# Exemplo:

# Digite um número: 5

# Fatorial = 120

# Pois:

# 5! = 5 × 4 × 3 × 2 × 1

# Observação:
# O programa deve validar se o número informado é positivo.

numero = int (input("Digite um numero inteiro: "))

while numero <= 0:
    numero = int(input())
for i in range (numero + 1):

    mult *= i

    print (mult)
