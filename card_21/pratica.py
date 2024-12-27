import cv2 # importa o opencv
import numpy as np

cam = cv2.VideoCapture(0) # cria um objeto de captura de video da webcam


while True: # cria um loop infinito para a captura dos frames
    _, frame = cam.read() # _: booleana que representa se o frame foi capturado com sucesso; frame: numpy array 3D que representa o frame

    # convertendo o frame de BGR para HSV:
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # criando uma máscara roxa
    low_purple = np.array([260, 50, 72])
    high_purple = np.array([320, 255, 255])
    purple_mask = cv2.inRange(hsv_frame, low_purple, high_purple)
    purple = cv2.bitwise_and(frame, frame, mask=purple_mask)

    # criando uma máscara laranja
    low_orange = np.array([18, 40, 90])
    high_orange = np.array([27, 255, 255])
    orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
    orange = cv2.bitwise_and(frame, frame, mask=orange_mask)


    #cv2.imshow("Frame", frame) # "Frame":titulo para a janela; frame: imagem a ser exibida
    cv2.imshow("No purple", purple)

    key = cv2.waitKey(1) # cria um objeto que registra teclas pressionadas pelo usuário durante a execução do programa
    if key == 27: # se a tecla pressionada for "Esc"
        break