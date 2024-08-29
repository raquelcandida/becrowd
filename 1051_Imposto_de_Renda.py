sal = float(input())
ir1 = 0.0
ir2 = 0.0
ir3 = 0.0
if 0.00 < sal <= 2000.00:
    print(f'Isento')
else:
    v1 = sal - 2000
    if v1 <= 1000:
        ir1 = v1 * 0.08
    else:
        ir1= 1000 * 0.08

    v2 = sal - 3000
    if v2 >= 0.0:
        if v2 <= 1500:
            ir2=v2 * 0.18
        else:
            ir2=1500 * 0.18

    v3=sal - 4500
    if v3 >= 0.0:
        ir3=v3 * 0.28

    print(f'R$ {ir1+ir2+ir3:.2f}')