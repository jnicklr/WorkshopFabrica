# armazena o valor numérico escolhido em uma variável!

numero = input("Digite um número: ")

# Faz uma verificação dos números!

antecessor = 0
sucessor = 0
try:
    antecessor = int(numero) - 1
    sucessor = int(numero) + 1
except ValueError:
    raise ValueError("Digite um número válido!")
    
# imprime os valores de incremento e decremento direto na formatação do print!

print(
    f"O antecessor do número {numero} é {antecessor}.\nO sucessor do número {numero} é {sucessor}."
)