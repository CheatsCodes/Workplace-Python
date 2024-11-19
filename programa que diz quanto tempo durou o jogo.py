horaInicial = int(input('Informe a hora inicial do jogo;'))
minutoInicial = int(input('Informe o minuto inicial do jogo;'))
horaFinal = int(input('Informe a hora final do jogo;'))
minutoFinal = int(input('Informe o minuto final do jogo;'))

horarioInicial = horaInicial * 60+ minutoInicial
horarioFinal= horaFinal *60 +minutoFinal

if horarioInicial < horarioFinal : duração = horarioFinal - horarioInicial
else: duração = 24*60 - horarioInicial + horarioFinal

print('Horas:', duração//60)
print('Minutos:', duração%60)
