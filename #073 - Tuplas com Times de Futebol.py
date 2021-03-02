times = ('São Paulo','Internacional','Atlético-MG','Flamengo', 'Palmeiras','Grêmio','Fluminense',
         'Santos', 'Corinthias', 'Atletico-PR')

print('A) Os 5 primeiros são {}'.format(times[0:5]))
print('B) Os ultimos 4 colocados são {}'.format(times[6:]))
print('C) {}'.format(sorted(times)))
print('D) O corinthias está na {} posição'.format(times.index('Corinthias')+1))