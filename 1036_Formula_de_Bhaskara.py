a = float(input("Insira o valor de a: "))
if a == 0 or a == 0.0:
  print(f'O valor de a: {a}, a equação não é do segundo grau')
else:
  b = float(input("Insira o valor de b: "))
  c = float(input("Insira o valor de c: "))
  delta = b**2 - (4*a*c)
  if delta < 0:
     print(f'O valor de delta é: {delta:.2f} negativo, e  não possui raizes reais')
  elif delta == 0:
     x1 = (-b+(delta**0.5))/(2*a)
     x2 = (-b-(delta**0.5))/(2*a)
     print(f'O valor de delta é: {delta:.2f} zero, e a equação possui apenas uma raiz real')
     print(f'O valor de x1 é: {x1:.2f}')
     print(f'O valor de x2 é: {x2:.2f}')
  else:
    x1 = (-b + (delta**0.5))/(2*a)
    x2 = (-b - (delta**0.5))/(2*a)
    print(f'O valor de delta é: {delta:.5f}')
    print(f'O valor de x1 é: {x1:.5f}')
    print(f'O valor de x2 é: {x2:.5f}')