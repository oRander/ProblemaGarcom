# Problema do Garçom

Este projeto foi desenvolvido como parte da disciplina **Programação Paralela e Distribuída** do curso de Ciência da Computação. O objetivo é simular o trabalho de um garçom em uma festa, servindo taças para os convidados de forma eficiente.

## Descrição do Problema

O cenário envolve um garçom em uma festa com 300 convidados espalhados por um salão de 25x25 metros. O garçom deve servir taças para os convidados de forma eficiente, usando uma bandeja que comporta até 6 taças. A bandeja deve ser equilibrada enquanto o garçom se movimenta pelo salão, servindo as taças aos convidados.

## Objetivo

Simular o processo do garçom se movendo pelo salão, atendendo os 6 convidados mais próximos a cada vez e retornando à base para pegar mais taças. O objetivo é calcular a distância percorrida pelo garçom enquanto ele atende os convidados.

## Lógica do Algoritmo

O código foi desenvolvido para executar o processo de forma **sequencial**, ou seja, o garçom realiza as ações uma após a outra em uma única sequência de passos. O algoritmo segue os seguintes passos:

- O garçom começa no canto superior esquerdo do salão.
- Ele identifica os 6 convidados mais próximos e se move até cada um deles.
- Após servir as taças, ele marca o ponto como atendido.
- O garçom retorna à base para pegar novas taças e repete o processo até atender todos os convidados.
- A distância percorrida é calculada a cada movimento.

## Sequencialidade

O código atual é **sequencial**, o que significa que as operações são executadas uma após a outra, sem divisão de tarefas em múltiplos processadores ou threads. Ou seja:

- O garçom encontra os pontos mais próximos de forma sequencial.
- A posição do garçom é atualizada a cada movimento.
- As interações com a interface gráfica (onde o garçom é desenhado) também são realizadas de forma sequencial.

## Implementação

O código foi implementado usando a linguagem Python e a biblioteca Tkinter para criar a interface gráfica. O processo de movimentação do garçom e o cálculo da distância percorrida são feitos de maneira linear, sem utilização de threads ou multiprocessamento, o que caracteriza o código como sequencial.

## Apresentação

[Apresentação em vídeo](https://www.youtube.com/watch?v=pJ69EBeFQ-k)


## Conclusão

O problema foi resolvido com sucesso de maneira sequencial, garantindo a funcionalidade esperada. Em um cenário real, onde a eficiência é fundamental, seria interessante considerar a implementação de paralelismo para simular múltiplos garçons ou otimizar os cálculos de movimentação. Abaixo estão as distâncias totais percorridas pelo garçom, dependendo do número de taças servidas:

- **01 taças** - Distância total percorrida pelo garçom: 284666.49 metros
- **02 taças** - Distância total percorrida pelo garçom: 146631.39 metros
- **04 taças** - Distância total percorrida pelo garçom: 80931.93 metros
- **06 taças** - Distância total percorrida pelo garçom: 54413.38 metros
- **08 taças** - Distância total percorrida pelo garçom: 44849.61 metros
- **10 taças** - Distância total percorrida pelo garçom: 36102.84 metros
- **12 taças** - Distância total percorrida pelo garçom: 30874.76 metros
- **14 taças** - Distância total percorrida pelo garçom: 28890.51 metros

Esses valores demonstram a relação entre o número de taças servidas e a distância total percorrida pelo garçom. Quanto mais taças ele carrega, maior é a distância percorrida para atender os convidados, o que indica que a logística de movimentação e a capacidade de servir mais taças deve ser otimizada.
