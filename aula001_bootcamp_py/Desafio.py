CONSTANTE_BONUS = 1000

# 1) Solicite ao usuário que digite seu nome

nome_usuario = input("Digite seu nomer: ")

# 2) Solicite ao usiáro que digite o valor do seu salário
# Converta a entrada para um numero de ponto flutuante

salario_usuario = float(input("Digite seu salário: "))

# 3) Solicite ao usuario que digite o valor do bonus recebido
# Converte a entrada para um numero de pontos flutuante

bonus_usuario = float(input("Digite o valor do bonus: "))

# Calcule o valor do bonus final

valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprima ums msg personalizada para o usuário

print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")

