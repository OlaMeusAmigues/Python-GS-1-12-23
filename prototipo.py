def escolhas(mensagem, opcoes):
    escolha = input(mensagem)
    while not escolha in opcoes:
        print(f"Opção inválida, escolha entre: {opcoes}")
        escolha = input(mensagem)
    return escolha

def so_inteiros(mensagem, maior_que_algo, menor_que_algo, referencia_menor, referencia_maior):
    entrada = input(mensagem)
    while not entrada.isnumeric():
        print("Apenas inteiros positivos!")
        entrada = input(mensagem)
    if maior_que_algo == True:
        while not int(entrada) > referencia_menor:
            print(f"Digite um número a cima de {referencia_menor}!")
            entrada = so_inteiros(mensagem, True, False, referencia_menor, referencia_maior)
    if menor_que_algo == True:
        while not int(entrada) < referencia_maior:
            print(f"Digite um número abaixo de {referencia_maior}!")
            entrada = so_inteiros(mensagem, False, True, referencia_menor, referencia_maior)
    return int(entrada)



pergunta_cadeira = "\tQual a quantidade de cadeiras? "
#pergunta_ocupaçao  dentro do código 
opcoes_ocupacao = ["0", "1"]
pegunta_voltar = ("Você deseja:\n"
                    "\t0 - Atualizar ocupação\n"
                    "\t1 - Atualizar número de cadeiras\n"
                    "\t2 - Atualizar níveis de preocupação\n"
                    "\t3 - Atualizar número de cadeiras e níveis de preocupação\n"
                    "\t4 - Fechar programa\n"
                    "Resposta: ")
opcoes_voltar = ['0','1','2', '3', '4']
pergunta_modo = ("Você deseja iniciar:\n"
                 "\t0 - Modo de preenchimento rápido\n"
                 "\t1 - Modo de preenchimento completo\n"
                 "Resposta: ")
opcoes_modo = ['0', '1']
pergunta_modo_rapido = "\tQuantas cadeiras estão ocupadas: "
pergunta_quant_niveis = ("Os níveis serão organizados em ordem crescente após declarados\n"
                         "\tQuantos níveis de preocupação existem: ")
#pergunta_nivel   dentro do código
voltar = '3'


while True:
    lugares_ocupados = []

    if voltar == '3' or voltar == '1':
        cadeiras = so_inteiros(pergunta_cadeira, True, False, 1, 1)#definir/redefinir número de cadeiras

    if voltar == '3' or voltar == '2':
        niveis = so_inteiros(pergunta_quant_niveis, True, False, 0, 0)
        lista_niveis = []
        for count in range(niveis):
            lista_niveis.append( so_inteiros(f"\tQual a {count + 1}ª porcentagem a ser declarada? ", True, True, 0, 100) )
        for count_1 in range(niveis):
            for count_2 in range(count_1, niveis):
                if (lista_niveis[count_2] < lista_niveis[count_1]):
                    sup = lista_niveis[count_1]
                    lista_niveis[count_1] = lista_niveis[count_2]
                    lista_niveis[count_2] = sup
                    
    while True:
        quant_ocupados = 0

        modo = escolhas(pergunta_modo, opcoes_modo)

        if modo == '1':
            for count in range(1, cadeiras + 1):
                pergunta_ocupacao = (f"A {count}ª cadeira está ocupada?"
                                    f"\n\t0 - Sim"
                                    f"\n\t1 - Não"
                                    f"\nResposta: ")
                resposta = escolhas(pergunta_ocupacao, opcoes_ocupacao)
                if resposta == opcoes_ocupacao[0]:#sim
                    lugares_ocupados.append(True)
                    quant_ocupados += 1
                else:
                    lugares_ocupados.append(False)
            print()
            for count in range(cadeiras):
                if lugares_ocupados[count] == False:
                    print(f"A {count + 1}ª cadeira está desocupada")
        else:
            quant_ocupados = so_inteiros(pergunta_modo_rapido, False, True, cadeiras + 1, cadeiras + 1)
        print()
        
        porcent_ocupados = round(quant_ocupados*100/cadeiras, 2)

        print(f"\tOcupação em ({porcent_ocupados}%)"
              f"\n\t{quant_ocupados}/{cadeiras} de cadeiras ocupadas")
        for count in range(niveis-1, -1, -1):
            if porcent_ocupados>=lista_niveis[count]:
                print(f"\tAlerta de Nível {count+1} atingido({lista_niveis[count]}%)!\n")
                break
        
        voltar = escolhas(pegunta_voltar, opcoes_voltar)
        if not voltar == opcoes_voltar[0]:#1, 2, 3 ou 4
            break
    if voltar == opcoes_voltar[4]:#4
        break
