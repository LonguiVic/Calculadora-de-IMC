# Calculo de IMC - Indice de Massa Corporal
# Qual é a sua altura:
# Qual é o seu peso em kg:

# MENOR QUE 18.5 - MAGREZA
# ENTRE 18.5 E 24.9 - NORMAL
# ENTRE 25 E 29.9 - SOBREPESO
# ENTRE 30 E 39.9 - OBESIDADE
# MAIOR QUE 40.0 - OBESIDADE GRAVE

altura = float(input('Qual é a sua altura: '))
altura2 = pow(altura, 2)
peso = int(input('Qual é o seu peso em kg: '))
imc = peso / altura2
imc_arredondado = round(imc, 2)

if imc_arredondado < 18.5:
    print(f'Seu resultado foi {imc_arredondado} - Magreza')
elif 18.5 <= imc_arredondado < 24.9:
    print(f'Seu resultado foi {imc_arredondado} - Normal')
elif 25 <= imc_arredondado < 29.9:
    print(f'Seu resultado foi {imc_arredondado} - Sobrepeso')
elif 30 <= imc_arredondado < 39.9:
    print(f'Seu resultado foi {imc_arredondado} - Obesidade')
elif imc_arredondado >= 40:
    print(f'Seu resultado foi {imc_arredondado} - Obesidade Grave')
