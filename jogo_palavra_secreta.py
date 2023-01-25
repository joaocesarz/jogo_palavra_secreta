# Simples algoritimo para jogo de palavra secreta.

secreto = 'palavra_secreta_da_sua_escolha'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')


    if chances == 0:
        print('Você Perdeu!!')
        break

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UUHHULLL, A letra "{letra}" Contem na palavra secreta.')
    
    else:
        print(f'AAFFzzz, A letra "{letra}" NÃO contem na palavra secreta.')
        digitadas.pop()

    
    secreto_temporario = ''


    for i in secreto:
        if i in digitadas:
            secreto_temporario += i 
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'A palavra secreta ficou assim {secreto_temporario}')
    else:
        print(f'A palavra secreta ficou assim {secreto_temporario}')


    if letra not in secreto:
        chances -= 1
        
        print(f'Você tem "{chances}".')
   
