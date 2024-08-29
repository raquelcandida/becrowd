sal = float(input())
ir1 = (0.0 if (sal <= 2000) else ( 80.0 if (sal > 3000) else ((sal - 2000) * 0.8)))
ir2 = (0.0 if (sal <= 3000) else ( 270.0 if (sal > 4500) else ((sal - 3000) * 0.18)))
ir3 = (0.0 if (sal <= 4500) else ((sal - 4500) * 0.28))
imp = ir1 + ir2 + ir3
print ('isento' if (imp == 0) else f'R$ {imp:.2f}')