import calculadora
def main():
    a,b = 2, 3

    soma = calculadora.soma(a,b)
    print(f'{a} + {b} = {soma}')

    subtracao = calculadora.subtrai(a,b)
    print(f'{a} - {b} = {subtracao}')

    multiplicacao = calculadora.multiplicacao(a,b)
    print(f'{a} * {b} = {multiplicacao}')

    divisao = calculadora.dividir(a,b)
    print(f'{a} / {b} = {divisao}')
main()