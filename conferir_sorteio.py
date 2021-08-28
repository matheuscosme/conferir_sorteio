from random import randint
from time import sleep


class Cartela:
    def __init__(self, total):
        self.total = total
        self.jogos = []
        self.vencedor = []
    

    @property
    def jogos(self):
        return self.__jogos

    #RECEBE OS JOGOS QUE O USUÁRIO FEZ
    @jogos.setter
    def jogos(self, valor):
        valor = []
        while len(valor) < self.total:
            while True:
                jogo_atual = input("Digite cada dezena com dois dígitos separadas por espaço: ")
                if len(jogo_atual) >= 17:
                    break
                else:
                    print('Quantidade de dezenas inválida ou entrada incorreta!')
            valor.append(self.conversor(jogo_atual))
        self.__jogos = valor

    #CONVERTE A LISTA DE STRING PARA UMA LISTA DE INTEIROS
    def conversor(self, list):
        temp_list = list.split()
        new_list = []
        for i in temp_list:
            while True:
                if i.isdigit() and int(i) > 0 and int(i) <= 60 and int(i) not in new_list:
                    new_list.append(int(i))
                    break
                else:
                    print(f'Entrada {i} inválida')
                    i = input('Digite um valor válido: ')
        return sorted(new_list)


 
    @property
    def vencedor(self):
        return self.__vencedor

    #RECEBE O JOGO VENCEDOR DA SEMANA
    @vencedor.setter
    def vencedor(self, valor):
        valor = input('--------------->Digite os números sorteados dessa semana: ')
        self.__vencedor = self.conversor(valor)


#CONFERÊNCIA DO SORTEIO
def confere(jogos, vencedor):
    for jogo in jogos:
        sleep(0.5)
        print(f'Conferindo Jogo: {jogo}')
        n = 0
        acertos = 0
        for i in jogo:
            n += 1
            if i in vencedor:
                print(f'{i} - \033[92m  ✓   \033[0m    ', end = '', flush=True)
                sleep(0.3)
                acertos += 1
            else:
                print(f'{i} - \033[91m  x    \033[0m  ', end = '', flush=True)
                sleep(0.3)
            if n == len(jogo):
                print(f'\nNº de Acertos: \033[1;93m {acertos} \033[0m ')
                print('-------------------------------------------------------------')
                print()



##PROGRAMA PRINCIPAL##

qnt_jogos = int(input('Quantos jogos você fez essa semana: '))
jogo_do_dia = Cartela(qnt_jogos)
print(f' SEUS JOGOS: {jogo_do_dia.jogos}')
sleep(0.2)
print()
print(f'NÚMEROS SORTEADOS: {jogo_do_dia.vencedor}')
sleep(0.2)

print('------CONFERINDO RESULTADOS------')
sleep(1)

confere(jogo_do_dia.jogos, jogo_do_dia.vencedor)