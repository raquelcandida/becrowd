hora_inicial, min_inicial, hora_final, min_final = input().split(' ')

total_min_i = (int(hora_inicial) * 60) + int(min_inicial)
total_min_f = (int(hora_final) * 60) + int(min_final)
total_duracao = int(total_min_f) - int(total_min_i)

if total_duracao <= 0:
    total_duracao += 1440

duracao_hora = total_duracao // 60
duracao_min = total_duracao % 60

print(f'O JOGO DUROU {duracao_hora} HORA(S) E {duracao_min} MINUTO(S)')