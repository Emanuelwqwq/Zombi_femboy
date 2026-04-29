import random
import time
import os
comeco = input("bem vindo ao apocalipse, voce gostaria de jogar? (sim ou não)\n")

if comeco == 'sim' or 's':
    nome = input("qual seu nome?\n")
    print("bem vindo ao seu pior pesadelo")
    time.sleep(2)
    os.system('cls')
else:
    print("Adeus")
    os.system('cls')
    exit()

while comeco == 'sim' or 's':
    print(f"\nvocê tem 35 pontos de status disponiveis, voce pode colocar em ataque e vida, qual valor voce vai colocar em cada? (esses pontos não podem ser alterados)\n")
    ataque = int(input("ataque: "))
    vida = int(input("vida: "))
    if ataque + vida == 35:
        print("vamos para o combate!")      
        vida_max = vida
        time.sleep(2)
        os.system('cls')
        break
    else:
        os.system('cls')
        print("os pontos precisam somar 35, tente novamente")


print(f"\nvocê {nome} é um sobrevivente a esse caos eminente esta andando pela cidade silenciosa, enquanto anda tentando não chamar atenção, porque cada ruido pode atrair uma daquelas besta, mas do nada voce se ve frente a um zumbi e é obrigado a entrar em combate\n")
time.sleep(20)
os.system('cls')
print("Tutorial de combate: voce tem seu turno para atacar e o zumbi tem o dele, o dano causado é igual ao ataque do personagem, no começo de toda batalha vai mostrar o nome a vida e o ataque do zumbi quanto o seu, a batalha termina quando a vida de um dos dois chegar a 0 ou menos, o outro vence, se voce vencer ganha 10 pontos que podem ser usados para melhorar seu ataque ou vida\n")
time.sleep(20)
os.system('cls')
vida_zumbi1 = random.randint(35, 50)
ataque_zumbi1 = random.randint(5, 8)

print(f"zumbi femboy: \nvida: {vida_zumbi1} \nataque: {ataque_zumbi1}")
print(f"{nome}: \nvida: {vida} \nataque: {ataque}\n")
time.sleep(7)
os.system('cls')

while vida > 0 and vida_zumbi1 > 0:
    acao = input(f"{nome} ataca, oque voce vai fazer?(atacar ou acariciar)\n")

    if acao == "atacar":
        vida_zumbi1 -= ataque
        print(f"voce causou {ataque} de dano, a vido do zumbi femboy agora é: {vida_zumbi1}")

    elif acao == "acariciar":
        print("voce acariciou o zumbi femboy e ele ficou feliz e seu dano foi reduzido em 10%")
        ataque_zumbi1 = int(ataque_zumbi1 * 0.9)
        print(f"agora o ataque do zumbi femboy é: {ataque_zumbi1}")

        if ataque_zumbi1 < 1:
            ataque_zumbi1 = 1
            print(f"o ataque do zumbi femboy não pode ser menor que 1, agora é: {ataque_zumbi1}")

    else:
        print("ação invalida, tente novamente")
        continue

    if vida_zumbi1 > 0:
        vida -= ataque_zumbi1
        time.sleep(3)
        print(f"o zumbi atacou e causou {ataque_zumbi1} de dano, sua vida agora é: {vida}")

    if vida <= 0:
        print("voce morreu, o zumbi femboy venceu")
        print("FIM DE JOGO")
        os.system('cls')
        exit()

    
    if vida_zumbi1 <= 0:
        time.sleep(3)
        os.system('cls')
        print("\nparabens, voce matou o zumbi femboy e venceu a batalha, voce ganhou 10 pontos de melhoria e sua vida foi restaurada")
        
        
        time.sleep(3)

        incrementa = int(input("quantos pontos voce quer colocar em ataque? (o resto vai para a vida)\n"))

        ataque += incrementa
        vida_max += (10 - incrementa)
        vida = vida_max
        print(f"seu ataque agora é: {ataque} e sua vida agora é: {vida}")
        time.sleep(3)
        os.system('cls')

print("\napos a batalha contra essa aberação, você continua sua jornada, na verdade voce sempre esteve em buscar de algo, algo que salvaria a humanidade, uma cura que esta localizada em um lugar subteraneo no centro da cidade, você continua caminhando ate chegar em um predio que parecia abandonado por fora mas voce sabe que por dentro tem algo que nenhum humano deveria ver, algo inimaginavel, você entra no predio mas logo na entrada voce observa um zumbi gigante denominado de zumbi Tomboy, agora seu objetivo é matalo ou talvez não\n")
time.sleep(25)
os.system('cls')
print("você tem uma nova ação disponivel(aperto de bunda), essa ação tem um efeito especial, Descubra!\n")
time.sleep(7)
zombi_tomboy_vida = random.randint(60, 85)
zombi_tomboy_ataque = random.randint(5,8)

print(f"zumbi tomboy: \nvida: {zombi_tomboy_vida} \nataque: {zombi_tomboy_ataque}")
print(f"{nome}:\nvida: {vida}\nataque: {ataque}")
time.sleep(5)
os.system('cls')

afeto = 0
afeto_max = 3

while vida > 0 and zombi_tomboy_vida > 0:
    acao = input(f"\n{nome} ataca, oque voce vai fazer?(atacar, acariciar ou apertar)\n")
    if acao == "atacar":
        zombi_tomboy_vida -= ataque
        print(f"voce causou {ataque} de dano, a vida do zumbi tomboy agora é: {zombi_tomboy_vida}")

    elif acao == "acariciar":
        print("voce acariciou o zumbi tomboy e ele ficou feliz e seu dano foi reduzido em 10%")
        zombi_tomboy_ataque = int(zombi_tomboy_ataque * 0.9)
        print(f"agora o ataque do zumbi tomboy é: {zombi_tomboy_ataque}")

        if zombi_tomboy_ataque < 2:
            zombi_tomboy_ataque = 2
            print(f"o ataque do zumbi tomboy não pode ser menor que 2, agora é: {zombi_tomboy_ataque}")

    elif acao == "apertar":
        print ("voce fez algo inimaginavel, o zombi tomboy ficou estranho")
        time.sleep(3)
        
        chance = random.randint(1 , 100)
        if chance <= 80:
            afeto += 1
        
    else: 
        print("ação invalida, tente novamente")
        continue

    if afeto == afeto_max:
        os.system('cls')
        time.sleep(2)
        print("\no zumbi tomboy se apaixonou por voce e decidiu se juntar a você, todos os status dela agora é seu")
        ataque += zombi_tomboy_ataque
        vida_max += zombi_tomboy_vida
        vida = vida_max
        break
    
    if zombi_tomboy_vida > 0:
        vida -= zombi_tomboy_ataque
        time.sleep(3)
        print(f"o zumbi tomboy atacou e causou {zombi_tomboy_ataque} de dano, sua vida agora é: {vida}")
        
    if vida <= 0:
        print("voce morreu, o zumbi tomboy venceu")
        print("FIM DE JOGO")
        os.system('cls')
        exit()

    if zombi_tomboy_vida <= 0:
        print("\nparabens, você matou o zumbi tomboy e venceu a batalha, mas sente que algo esta faltando")
        os.system('cls')
        break

if afeto == afeto_max:
    print(f"seus status agora são: {ataque} de ataque e {vida} de vida, com a ajuda do zumbi tomboy voce continua sua jornada em busca da cura")
    time.sleep(15)
    os.system('cls')
else:
    time.sleep(5)
    print("voce olha para o zumbi tomboy morto e sente tristeza, por algum motivo")

print("\ncontinuação a fazer")