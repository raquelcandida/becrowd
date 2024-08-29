a, b, c = input().split(" ")
if float(a) == 0.0:
  print('Impossivel calcular')
else:
  delta = float(float(b)**2)-(4*float(a)*float(c))
  if delta < 0:
     print('Impossivel calcular')
  elif delta == 0:
     print(f'Impossivel calcular')
  else:
    x1 = (-float(b)+(delta**0.5))/(2.0*float(a))
    x2 = (-float(b)-(delta**0.5))/(2.0*float(a))
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')