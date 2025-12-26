larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg * alt
print('Sua parede tem dimensão de {}x{} e sua área e de {}m².'.format(larg,alt,área))
tinta = área / 2
print('para pintar essa parde, você precisará de {}l de tinta.'.format(tinta))