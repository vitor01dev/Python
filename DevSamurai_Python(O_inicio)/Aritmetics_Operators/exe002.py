# Calcule a soma dos numeros do 10 ao 14

soma = sum(range(10, 15))
print(soma)

# Calcule a média entre os números 10,15,20

PONTOS = [10,15,20]

def avg():
    return sum(PONTOS) / len(PONTOS)

print(avg())

## Calcule a média das notas escolares definindo um peso para cada nota

NOTAS = [10, 8, 9]
PESOS = [0.5, 0.3, 0.2]
def media_ponderada():
    total = sum(n * p for n, p in zip(NOTAS, PESOS))
    return total / sum(PESOS)
print(media_ponderada())

## Qual o menor valor da lista?
VALORES = [50.2, 32.6, 89.90, 12.90, 24.99]
print(min(VALORES))

## Avalie se os números digitados são pares ou ímpares
def par_ou_impar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
numero = int(input("Digite um número: "))
resultado = par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")

## Verifique se o menor preço dessa lista é menor que R$20.00
menor_preco = min(VALORES)
if menor_preco < 20.00:
    print(f"O menor preço da lista é R${menor_preco}, que é menor que R$20.00.")
else:
    print(f"O menor preço da lista é R${menor_preco}, que é maior que R$20.00.")
