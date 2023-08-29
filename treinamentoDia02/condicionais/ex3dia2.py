# Armazenando o valor da velocidade do carro!
velocidade = input("Digite a velocidade do carro: ")

# Verificação da velocidade do usuário!
try:
    velocidade = float(velocidade) # Vai armazenar o valor da velocidade em uma variável
except ValueError: # Se a velocidade for inválida aqui vai captar e mostrar o erro!
    raise ValueError("Valor inválido para a velocidade!")

# Verificando se o usuário ultrapassou a velocidade!
multa = True if velocidade > 80 else False

# Criando uma função que receba como parâmetro a velocidade do carro
# A função vai retornar o valor da multa baseado na velocidade ultrapassada.
aplicarMulta = lambda velocidade_do_carro: (velocidade_do_carro-80) * 7

# Vai imprimir se o usuário foi ou não multado com base na variável multa.
if multa:
    valor_a_pagar = aplicarMulta(velocidade) # Armazena o valor da multa.
    print(f"Você foi multado em R${valor_a_pagar} por ultrapassar a velocidade.")
elif (velocidade < 0): # Verifica se a velocidade é válida!
    print("Velocidade inválida, digite um número maior que 0.")
else:
    print("Você não foi multado!")
    