# Verificação da idade do usuário!
idade = 0
try:
    idade = int(input("Digite sua idade: ")) # Vai armazenar o valor da idade em uma variável
except ValueError: # Se a idade for inválida aqui vai captar e mostrar o erro!
    raise ValueError("Digite idade válida!")

# Vai imprimir se você é maior ou não de idade para receber a carteira de habilitação!
# Operador ternário: "código rodado se verdadeiro" if "condição" else "código rodado se falso"
print(f"Você tem {idade}, já pode receber a carteira de motorista (CNH)!" if idade >= 18 else f"Você tem {idade}, não pode tirar a carteira de motorista!")