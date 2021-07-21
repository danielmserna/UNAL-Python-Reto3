def copaAmericaFutebol(equiposParticipantes):
  listaEquipos = list(map(str,equiposParticipantes.split()))
  listaEquiposReturn = [0] * len(listaEquipos)
  listaConteoReturn = [0] * len(listaEquipos)
  unEquipo = 0
  for i in range(1, len(listaEquipos)):
    listaEquiposReturn[unEquipo] = listaEquipos[i-1]
    listaConteoReturn[unEquipo] = int(listaConteoReturn[unEquipo]) + 1
    if listaEquipos[i] != listaEquipos[i-1]:
      unEquipo+=1
    if i == int(len(listaEquipos))-1:
      listaConteoReturn[unEquipo] = int(listaConteoReturn[unEquipo]) + 1
      listaEquiposReturn[unEquipo] = listaEquipos[i]
  
  print(' '.join([i for i in listaEquiposReturn if i != 0]))
  print('\n')
  print(' '.join([str(i) for i in listaConteoReturn if i != 0]))

copaAmericaFutebol(input(""))

