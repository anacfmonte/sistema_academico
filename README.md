#Aluna: Ana Clara Ferreira Monte 

salario_inicial = 2000
ano_contrato = 1995
ano_atual = int(input("Insira o ano atual: "))
cont = 1997

porcentagem = 1.5/100
aumento_salarial = salario_inicial

while cont <= ano_atual:
    aumento_salarial*= 1+porcentagem
    porcentagem*=2
    cont+=1
print(f"{ano_atual}:{aumento_salarial:.2f}")
