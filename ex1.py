import os
os.system('cls')

agenda = []

compromisso = input('Digite algum compromisso ou não para sair?:  ')

while compromisso != 'não':
    agenda.append(compromisso)
    compromisso = input('Mais compromissos?  ')

achou = False
x = 0

compromisso_procurado = input('Digite o compromisso que deseja buscar: ')

while x < len(agenda):
    if agenda[x] == compromisso_procurado: 
        achou = True
        break
    x += 1

if achou:
    print(f'Compromisso: {compromisso_procurado}, achado na posição {x + 1}')
else:
    print('Compromisso não encontrado')