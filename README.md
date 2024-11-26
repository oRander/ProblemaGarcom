<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Problema do Garçom - README</title>
</head>
<body>
    <h1>Problema do Garçom</h1>
    <p>Esse projeto foi desenvolvido como parte da disciplina <strong>Programação Paralela e Distribuída</strong> do curso de Ciência da Computação. O objetivo é simular o trabalho de um garçom em uma festa, servindo taças para os convidados de forma eficiente.</p>

    <h2>Descrição do Problema</h2>
    <p>O cenário envolve um garçom em uma festa com 300 convidados espalhados por um salão de 25x25 metros. O garçom deve servir taças para os convidados de forma eficiente, usando uma bandeja que comporta até 6 taças. A bandeja deve ser equilibrada enquanto o garçom se movimenta pelo salão, servindo as taças aos convidados.</p>

    <h2>Objetivo</h2>
    <p>Simular o processo do garçom se movendo pelo salão, atendendo os 6 convidados mais próximos a cada vez e retornando à base para pegar mais taças. O objetivo é calcular a distância percorrida pelo garçom enquanto ele atende os convidados.</p>

    <h2>Lógica do Algoritmo</h2>
    <p>O código foi desenvolvido para executar o processo de forma <strong>sequencial</strong>, ou seja, o garçom realiza as ações uma após a outra em uma única sequência de passos. O algoritmo segue os seguintes passos:</p>
    <ul>
        <li>O garçom começa no canto superior esquerdo do salão.</li>
        <li>Ele identifica os 6 convidados mais próximos e se move até cada um deles.</li>
        <li>Após servir as taças, ele marca o ponto como atendido.</li>
        <li>O garçom retorna à base para pegar novas taças e repete o processo até atender todos os convidados.</li>
        <li>A distância percorrida é calculada a cada movimento.</li>
    </ul>

    <h2>Sequencialidade</h2>
    <p>O código atual é <strong>sequencial</strong>, o que significa que as operações são executadas uma após a outra, sem divisão de tarefas em múltiplos processadores ou threads. Ou seja:</p>
    <ul>
        <li>O garçom encontra os pontos mais próximos de forma sequencial.</li>
        <li>A posição do garçom é atualizada a cada movimento.</li>
        <li>As interações com a interface gráfica (onde o garçom é desenhado) também são realizadas de forma sequencial.</li>
    </ul>

    <h2>Implementação</h2>
    <p>O código foi implementado usando a linguagem Python e a biblioteca Tkinter para criar a interface gráfica. O processo de movimentação do garçom e o cálculo da distância percorrida são feitos de maneira linear, sem utilização de threads ou multiprocessamento, o que caracteriza o código como sequencial.</p>

    <h2>Conclusão</h2>
    <p>O problema foi resolvido com sucesso de maneira sequencial, garantindo a funcionalidade esperada. Em um cenário real, onde a eficiência é fundamental, seria interessante considerar a implementação de paralelismo para simular múltiplos garçons ou otimizar os cálculos de movimentação. Abaixo estão as distâncias totais percorridas pelo garçom, dependendo do número de taças servidas:</p>
    <ul>
        <li><strong>01 taças</strong> - Distância total percorrida pelo garçom: 284666.49 metros</li>
        <li><strong>02 taças</strong> - Distância total percorrida pelo garçom: 146631.39 metros</li>
        <li><strong>04 taças</strong> - Distância total percorrida pelo garçom: 80931.93 metros</li>
        <li><strong>06 taças</strong> - Distância total percorrida pelo garçom: 54413.38 metros</li>
        <li><strong>08 taças</strong> - Distância total percorrida pelo garçom: 44849.61 metros</li>
        <li><strong>10 taças</strong> - Distância total percorrida pelo garçom: 36102.84 metros</li>
        <li><strong>12 taças</strong> - Distância total percorrida pelo garçom: 30874.76 metros</li>
        <li><strong>14 taças</strong> - Distância total percorrida pelo garçom: 28890.51 metros</li>
    </ul>
    <p>Esses valores demonstram a relação entre o número de taças servidas e a distância total percorrida pelo garçom. Quanto mais taças ele carrega, maior é a distância percorrida para atender os convidados, o que indica que a logística de movimentação e a capacidade de servir mais taças deve ser otimizada.</p>
</body>
</html>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Problema do Garçom - README</title>
</head>
<body>
    <h1>Problema do Garçom</h1>
    <p>Esse projeto foi desenvolvido como parte da disciplina <strong>Programação Paralela e Distribuída</strong> do curso de Ciência da Computação. O objetivo é simular o trabalho de um garçom em uma festa, servindo taças para os convidados de forma eficiente.</p>

    <h2>Descrição do Problema</h2>
    <p>O cenário envolve um garçom em uma festa com 300 convidados espalhados por um salão de 25x25 metros. O garçom deve servir taças para os convidados de forma eficiente, usando uma bandeja que comporta até 6 taças. A bandeja deve ser equilibrada enquanto o garçom se movimenta pelo salão, servindo as taças aos convidados.</p>

    <h2>Objetivo</h2>
    <p>Simular o processo do garçom se movendo pelo salão, atendendo os 6 convidados mais próximos a cada vez e retornando à base para pegar mais taças. O objetivo é calcular a distância percorrida pelo garçom enquanto ele atende os convidados.</p>

    <h2>Lógica do Algoritmo</h2>
    <p>O código foi desenvolvido para executar o processo de forma <strong>sequencial</strong>, ou seja, o garçom realiza as ações uma após a outra em uma única sequência de passos. O algoritmo segue os seguintes passos:</p>
    <ul>
        <li>O garçom começa no canto superior esquerdo do salão.</li>
        <li>Ele identifica os 6 convidados mais próximos e se move até cada um deles.</li>
        <li>Após servir as taças, ele marca o ponto como atendido.</li>
        <li>O garçom retorna à base para pegar novas taças e repete o processo até atender todos os convidados.</li>
        <li>A distância percorrida é calculada a cada movimento.</li>
    </ul>

    <h2>Sequencialidade</h2>
    <p>O código atual é <strong>sequencial</strong>, o que significa que as operações são executadas uma após a outra, sem divisão de tarefas em múltiplos processadores ou threads. Ou seja:</p>
    <ul>
        <li>O garçom encontra os pontos mais próximos de forma sequencial.</li>
        <li>A posição do garçom é atualizada a cada movimento.</li>
        <li>As interações com a interface gráfica (onde o garçom é desenhado) também são realizadas de forma sequencial.</li>
    </ul>

    <h2>Implementação</h2>
    <p>O código foi implementado usando a linguagem Python e a biblioteca Tkinter para criar a interface gráfica. O processo de movimentação do garçom e o cálculo da distância percorrida são feitos de maneira linear, sem utilização de threads ou multiprocessamento, o que caracteriza o código como sequencial.</p>

    <h2>Conclusão</h2>
    <p>O problema foi resolvido com sucesso de maneira sequencial, garantindo a funcionalidade esperada. Em um cenário real, onde a eficiência é fundamental, seria interessante considerar a implementação de paralelismo para simular múltiplos garçons ou otimizar os cálculos de movimentação. Abaixo estão as distâncias totais percorridas pelo garçom, dependendo do número de taças servidas:</p>
    <ul>
        <li><strong>01 taças</strong> - Distância total percorrida pelo garçom: 284666.49 metros</li>
        <li><strong>02 taças</strong> - Distância total percorrida pelo garçom: 146631.39 metros</li>
        <li><strong>04 taças</strong> - Distância total percorrida pelo garçom: 80931.93 metros</li>
        <li><strong>06 taças</strong> - Distância total percorrida pelo garçom: 54413.38 metros</li>
        <li><strong>08 taças</strong> - Distância total percorrida pelo garçom: 44849.61 metros</li>
        <li><strong>10 taças</strong> - Distância total percorrida pelo garçom: 36102.84 metros</li>
        <li><strong>12 taças</strong> - Distância total percorrida pelo garçom: 30874.76 metros</li>
        <li><strong>14 taças</strong> - Distância total percorrida pelo garçom: 28890.51 metros</li>
    </ul>
    <p>Esses valores demonstram a relação entre o número de taças servidas e a distância total percorrida pelo garçom. Quanto mais taças ele carrega, maior é a distância percorrida para atender os convidados, o que indica que a logística de movimentação e a capacidade de servir mais taças deve ser otimizada.</p>
</body>
</html>
