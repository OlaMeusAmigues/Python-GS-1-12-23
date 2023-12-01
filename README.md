# Nomes/Rm
- Guilherme Santiago da Silva   RM-552321
- Gustavo Gouvêa Soares         RM-553842


# Detalhes
  O projeto consiste na leitura automática de cadeiras ocupadas em um ambiente para emitir um alerta de preocupação baseado em seu nível de ocupação. A leitura do ambiente será realizado através de um circuito Arduíno [Link do Tinkercad](https://www.tinkercad.com/things/j8fB9hAidMW-copy-of-prototipo-fila-zero?sharecode=tAsmiBubC6UIdh47A9eoEdCNaOpWQvlZMAgWjoF1_18) e os dados coletados serão processados em Python.
    
  O código em Python perguntará a quantidade e os valores dos níveis de alerta, a quantidade de cadeiras e modo de preenchimento de ocupação das cadeiras (Rápido ou Completo) antes de processar os dados coletados pelo arduíno. Enquanto não há a comunicação do Arduíno com o código em Python, os dados dos estados de ocupação serão preenchidos manualmente, após preenchidos, será retornado a quantidade e porcentagem de cadeiras ocupadas do ambiente junto com um nível de alerta, caso necessário, personalizado de acordo com o modo de preenchimento escolhido.



# Requisitos
## -Automação
- Através do circuito em arduíno será realizada a contagem em tempo real do número de cadeiras ocupadas
- Através do processamento em Python serão relacionados os dados de ocupação com seus respectivos níveis de preocupação
## -Precisão
- A contagem de assentos ocupados será realizada por um sensor ultrassônico a cima de cada assento, com um tempo de espera padrão de 5 segundos de para evitar falsas mudanças de disponível para ocupado
## -Prevenção
- Através da contagem em tempo real do nível de ocupação busca-se garantir a menor quantidade de funcionários necessários para garantir um bom atendimento ao cliente, reduzindo, simultanemente, tempo de fila, estresse da espera em filas, probabilidade de agravamentos e desistências e gastos com funcionários.


  
# Dependências
- Circuito Arduíno com Código Fonte em C++ [Link do Tinkercad](https://www.tinkercad.com/things/j8fB9hAidMW-copy-of-prototipo-fila-zero?sharecode=tAsmiBubC6UIdh47A9eoEdCNaOpWQvlZMAgWjoF1_18)
- Modo de envio dos dados do Arduíno para o Código fonte em Python



# Instruções de uso
- Ao iniciar o código será perguntado ao usuário a quantidade de cadeiras do ambiente (número inteiro maior que 1)
- Em seguida será perguntado ao usuário a quantidade de níveis de alerta (número inteiro maior que 0)
- Depois, serão registrados cada porcentagem de alerta (inteiros maiores que 0 e menores que 100)
- Logo após, será possível escolher o modo de preenchimento das cadeiras, sendo Rápido o mais adequado para visualizar apenas o nível de ocupação e de alerta e Completo o mais adequado para, além da função anteriror, indicar assentos disponíveis
- A partir daqui, será simulada a interação do arduíno com Python, feita provisóriamente pelo próprio usuário
- Caso escolha Rápida seja escolhida será apenas pedido a quantidade de lugares ocupados(inteiro maior ou igual a zero e menor que o número de cadeiras)
- Caso escolha Completa seja escolhida será perguntado cadeira por cadeira se ela está ocupada
- Caso escolha Completa seja escolhida também será emitido no terminal as cadeiras livres
- Independente da escolha será emitido a quantidade de cadeiras ocupadas, a porcentagem de ocupação e um nível de alerta, caso necessário
- Depois de processados os dados será possível Atualizar ocupação(resetando apenas a quantidade de cadeiras ocupadas), Atualizar número de cadeiras(resetando tudo menos os níveis de preocupação), Atualizar níveis de preocupação(resetando tudo menos o número de cadeiras), Atualizar número de cadeiras e níveis de preocupação(resetando tudo) e Fechar programa
