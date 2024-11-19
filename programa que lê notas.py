print ('Informe a nota:')
nota = float(input())
if nota<0 or nota>10:
    print('Erro. entrada invalida.')
    print('A nota deve estar no intervalo [0;10]')
else:
    if nota>=9 and nota<=10: print('Conceito A')
    if nota>=7 and nota<9: print('Conceito B')
    if nota>=5 and nota<7: print('Conceito C')
    if nota>=3 and nota<5: print('Conceito D')
    if nota>=0 and nota<3: print('Conceito E')