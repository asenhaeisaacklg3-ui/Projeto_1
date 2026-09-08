from random import randint
from time import sleep
print('-=-'*20)
print('Olá, Vamos jogar jokenpô')
print("-=-"*20)
computador = randint[0,1,2]
print('''Agora faça sua escolha
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = input("Faça sua escolha: ")
print("Jo")
sleep(1)
print('Ken')
sleep(1)
print("pô")
sleep(1)

if jogador == 0 and computador == 1:
    print("Vitória do computador")
elif jogador == 1 and computador == 2:
    print('Vitória do computador')
elif jogador == 2 and computador == 0:
    print("Vitória do computador")
elif jogador == 0 and computador == 2:
    print("Vitória do jogador")
elif jogador == 1 and computador == 0:
    print('Vitória do jogador')
elif jogador == 2 and computador == 1:
    print('Vitória do jogador')
else:
    print('Empate')
print("-=-"*20)
print(f'Computador escolheu: {computador}')
print(f'Jogador escolheu: {jogador}')
print("-=-"*20)