salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

percentual_aumento = 0

if salario_atual <= 280.00:
    percentual_aumento = 20
elif 280.00 < salario_atual <= 700.00:
    percentual_aumento = 15
elif 700.00 < salario_atual <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

inflacao = 3.8 / 100
valor_aumento_real = valor_aumento * (1 - inflacao)

print("\n--- RESULTADO ---")
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")
print(f"Valor do aumento real (descontado a inflação): R$ {valor_aumento_real:.2f}")
