#EXPERIENCIAS
total_cobaias=0
total_ratos=0
total_sapos=0
total_coelhos=0
perc_ratos=0.00
perc_sapos=0.00
perc_coelhos=0.00

n=int(input())

if 1 <= n <= 15:
    for i in range(0, n):
        qtd_cobaias, tipo_cobaias=input().split(" ")
        if (tipo_cobaias.upper() == "R"):
            total_ratos=total_ratos + int(qtd_cobaias)
        elif (tipo_cobaias.upper() == "S"):
            total_sapos=total_sapos + int(qtd_cobaias)
        elif (tipo_cobaias.upper() == "C"):
            total_coelhos=total_coelhos + int(qtd_cobaias)

        total_cobaias=total_cobaias + int(qtd_cobaias)

if total_cobaias > 0:
    perc_ratos=(float(total_ratos) * 100) / total_cobaias
    perc_sapos=(float(total_sapos) * 100) / total_cobaias
    perc_coelhos=(float(total_coelhos) * 100) / total_cobaias

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {perc_coelhos:.2f} %')
print(f'Percentual de ratos: {perc_ratos:.2f} %')
print(f'Percentual de sapos: {perc_sapos:.2f} %')