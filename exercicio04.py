n1=float(input('Digite um numero real: '))
n2=float(input('Digite outro numero real: '))
resultado=n1+n2
print('A soma entre {} e {} é igual a: {}'.format(n1, n2, resultado))

n3=int(input('Digite um numero: '))
n4=int(input('Digite outro numero: '))
resultado2=n3+n4
print('A soma entre {} e {} é igual a: {}'.format(n3, n4, resultado2))

tipo_resultado = type(resultado)
tipo_resultado2 = type(resultado2)

print("O tipo de resultado é:", tipo_resultado)
print("O tipo de resultado2 é:", tipo_resultado2)