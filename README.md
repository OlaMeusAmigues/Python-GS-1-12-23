# Nomes/Rm
- Guilherme Santiago da Silva   RM-552321
- Gustavo Gouvêa Soares         RM-553842



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



# Detalhes
  O projeto consiste na leitura automática de cadeiras ocupadas em um ambiente para emitir um alerta de preocupação baseado em seu nível de ocupação. A leitura do ambiente será realizado através de um circuito Arduíno [Link do Tinkercad](https://www.tinkercad.com/things/j8fB9hAidMW-copy-of-prototipo-fila-zero?sharecode=tAsmiBubC6UIdh47A9eoEdCNaOpWQvlZMAgWjoF1_18) e os dados coletados serão processados em Python.
    
  O código em Python precisa dos níveis de alerta (apenas inteiros maiores que 1) definidos antes da execução, ao ser executado ele pergunta ao usuário o número de cadeiras do ambiente (apenas inteiros maiores que 1), pergunta o modo de preenchimento da quantidade de cadeiras ocupadas (rápido ou completo) e retorna o nível de ocupação do ambiente personalizado de acordo com o modo de preenchimento.
