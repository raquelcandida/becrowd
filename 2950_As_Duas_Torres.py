# Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para calcular o ICM
# para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos.

distancia, r1, r2 = input().split(' ')

icm = float(distancia) / (float(r1) + float(r2))

print(f'{icm:.2f}')