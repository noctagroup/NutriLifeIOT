import serial
import time

# Configura a porta serial (verifique qual é a porta do micro:bit no Gerenciador de Dispositivos)
porta_serial = serial.Serial('COM8', 115200)  # Altere 'COM8' para a porta correta

while True:
    # Ler os dados enviados pela serial
    if porta_serial.in_waiting > 0:
        dados = porta_serial.readline().decode('utf-8').strip()
        
        print(f"Número de passos recebido: {dados}")

        # Abrir o arquivo no modo de escrita para substituir o conteúdo anterior
        with open("dados_pedometro.txt", "w") as arquivo:
            arquivo.write(f"{dados}\n")
            arquivo.flush()  # Salva os dados no arquivo imediatamente

    # Espera um pouco antes de verificar novamente
    time.sleep(0.1)
