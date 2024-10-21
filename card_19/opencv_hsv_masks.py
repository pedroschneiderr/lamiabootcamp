import cv2 # importa o opencv
import numpy as np

cam = cv2.VideoCapture(0) # cria um objeto de captura de video da webcam



while True: # cria um loop infinito para a captura dos frames
    _, frame = cam.read() # _: booleana que representa se o frame foi capturado com sucesso; frame: numpy array 3D que representa o frame

    # convertendo o frame de BGR para HSV:
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define o intervalo de uma cor em HSV para criar uma máscara
    low_red = np.array([161, 159, 84])
    high_red = np.array([179, 255, 255])

    # criando a máscara vermelha (que só exibe pixels vermelhos, deixando os outros em preto)
    red_mask = cv2.inRange(hsv_frame, low_red, high_red) # aplica a máscara ao frame hsv_frame
    red = cv2.bitwise_and(frame, frame, mask=red_mask) # aplica o operador lógico AND pixel por pixel, entre a imagem frame a sua versão com a máscara vermelha. Apenas os pixels vermelhos terão ambos os valores diferentes de 0 em ambas as imagens, fazendo com que apenas eles apareçam

    # criando uma máscara azul
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # criando uma máscara verde
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # criando uma máscara que exclui o branco
    low = np.array([0, 42, 0]) # mantém a saturação mais alta
    high = np.array([179,255,255])
    mask = cv2.inRange(hsv_frame, low, high)
    no_white = cv2.bitwise_and(frame, frame, mask=mask)


    #cv2.imshow("Frame", frame) # "Frame":titulo para a janela; frame: imagem a ser exibida
    cv2.imshow("No white", no_white)

    key = cv2.waitKey(1) # cria um objeto que registra teclas pressionadas pelo usuário durante a execução do programa
    if key == 27: # se a tecla pressionada for "Esc"
        break

