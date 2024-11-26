import tkinter as tk
import random
import math

# Função para calcular a distância euclidiana entre dois pontos
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Função para atualizar a posição do garçom
def mover_garcom():
    global pontos_vermelhos, garcom_posicao, distancia_total

    if not pontos_vermelhos:
        print(f"Todos os pontos foram atendidos!")
        print(f"Distância total percorrida pelo garçom: {distancia_total:.2f} metros")
        return

    atendidos = 0  # Contador para os 6 pontos atendidos

    while atendidos < 14 and pontos_vermelhos:
        # Encontra o ponto mais próximo do garçom
        ponto_mais_proximo = min(pontos_vermelhos, key=lambda p: distancia(garcom_posicao, p))

        # Calcula a distância percorrida até o ponto
        distancia_ate_ponto = distancia(garcom_posicao, ponto_mais_proximo)
        distancia_total += distancia_ate_ponto

        # Move o garçom até o ponto mais próximo
        canvas.move(garcom, ponto_mais_proximo[0] - garcom_posicao[0], ponto_mais_proximo[1] - garcom_posicao[1])
        canvas.update()
        canvas.after(500)  # Animação (500ms por movimento)

        # Atualiza a posição do garçom
        garcom_posicao = ponto_mais_proximo

        # Muda o ponto para verde
        canvas.itemconfig(pontos_canvas[ponto_mais_proximo], fill="green")
        pontos_vermelhos.remove(ponto_mais_proximo)
        atendidos += 1

    # Calcula a distância de retorno à base
    distancia_ate_base = distancia(garcom_posicao, (0, 0))
    distancia_total += distancia_ate_base

    # Volta para a base
    canvas.move(garcom, -garcom_posicao[0], -garcom_posicao[1])
    canvas.update()
    canvas.after(500)  # Animação (500ms por movimento)
    garcom_posicao = (0, 0)

    # Chama a função novamente até atender todos os pontos
    mover_garcom()

# Configurações iniciais
largura = 25  # Largura do salão (25 células)
altura = 25   # Altura do salão (25 células)
pontos_verdes = 300  # Número de pontos no salão

# Variável para acumular a distância total percorrida (em metros)
distancia_total = 0

# Criação da janela
janela = tk.Tk()
janela.title("Simulação do Garçom")
canvas = tk.Canvas(janela, width=600, height=600, bg="white")
canvas.pack()

# Desenha o quadrado do salão
canvas.create_rectangle(0, 0, largura * 25, altura * 25, outline="black", width=2)

# Distribui os pontos no quadrado
pontos_canvas = {}
pontos_vermelhos = []
for _ in range(pontos_verdes):
    x = random.randint(0, largura * 25 - 5)
    y = random.randint(0, altura * 25 - 5)
    ponto = (x, y)
    pontos_vermelhos.append(ponto)
    ponto_id = canvas.create_oval(x, y, x + 5, y + 5, fill="red", outline="")
    pontos_canvas[ponto] = ponto_id

# Cria o garçom (círculo)
garcom_posicao = (0, 0)
garcom = canvas.create_oval(0, 0, 10, 10, fill="blue", outline="")

# Inicia a movimentação do garçom
mover_garcom()

janela.mainloop()
