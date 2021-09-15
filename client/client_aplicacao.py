#####################################################
# Engenharia de Computação Insper
# Camada Física da Computação 2021.1
# Aluno: Marcos Vinícius da Silva
# 03/09/2021
# Projeto Client-Server
####################################################

# esta é a camada superior, de aplicação do seu software de comunicação serial UART.
# para acompanhar a execução e identificar erros, construa prints ao longo do código!

import random
from client_interfaceFisica import start_bit, stop_bit
from client_enlace import *
import binascii


#from enlace import *
import numpy as np
import time

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
# para saber a sua porta, execute no terminal:
# python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

# use uma das 3 opcoes para atribuir à variável a porta usada
# serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
# serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                  # Windows (variacao de)


def main():
    try:
        # declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        # para declarar esse objeto é o nome da porta.
        com1 = enlace('COM3')

        # Ativa comunicacao. Inicia os threads e a comunicação seiral
        # Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        com1.enable()
        print("-----------------------------------")
        print("1. Comunicação aberta com sucesso!")
        print("-----------------------------------")

        # aqui você deverá gerar os dados a serem transmitidos.
        # seus dados a serem transmitidos são uma lista de bytes a serem transmitidos. Gere esta lista com o
        # nome de txBuffer. Ela sempre irá armazenar os dados a serem enviados. txBuffer = imagem em bytes!

        # Lista com possíveis comandos a serem enviados na transmissão em formato hexadecimal.
        # Muitas vezes quando queremos expressar o conteúdo de um byte de memória (8 bits) é conveniente expressá-lo em hexadecimal, sendo apenas 2 dígitos.
        lista_comandos = [b'\x00\xff', b'\x00', b'\x0f', b'\xf0', b'\xff\x00', b'\xff']
        print("\n   Lista com os 6 possíveis comandos: {}" .format(lista_comandos))

        # Número aleatório que nos dira quantos comandos serão enviados.
        # O método randint do módulo random retorna um intero aleatório dentro do intervalo definido nos atributos.
        num_comandos = random.randint(10, 30)
        print("\n   Número aleatório de quantos comandos serão enviados: {}" .format(num_comandos))

        # Lista aleatória com comandos (bytes) a serem transmitidos no corpo da transmissão (payload)
        # O método choices do módulo random retorna uma lista de tamanho k, aleatória de uma população antes definida.
        lista_payloads = random.choices(lista_comandos, weights=None, cum_weights=None, k=num_comandos)
        print("\n   Lista aleatória com comandos a serem transmitidos: {}" .format(lista_payloads))
        print("\n")

        # Criando txBuffer. Vamos juntar o start_bit e o stop_bit ao payload
        print("-----------------------")
        print("2. Carregando TxBuffer.")
        print("-----------------------")
        print("\n")

        # Conferência do star_byte
        binary_start_bit = bin(int.from_bytes(start_bit, byteorder='little'))  # vira string
        print("   Start bit: {}" .format(binary_start_bit))
        print("\n")

        # Conferência do payload
        payload = b''
        for comando in lista_payloads:
            payload += comando
        print("   Payload: {}" .format(payload))
        print("\n")

        # Conferência do stop_bit
        binary_stop_bit = bin(int.from_bytes(stop_bit, byteorder='little'))
        print("   Stop bit: {}" .format(binary_stop_bit))
        print("\n")

        # Criando txBuffer
        txBuffer = b''
        txBuffer += start_bit + payload + stop_bit

        # Conferência do txBuffer.
        print("   Bytes carregados em Tx: {}" .format(txBuffer))
        print("\n")

        # Conferência do tamanho do txBuffer, ou seja, quantos bytes serão enviados.
        tamTxBuffer = len(txBuffer)
        print("   Tamanho do txBuffer: {} bytes" .format(tamTxBuffer))
        print("\n")

        # Conferência do tipo do txBuffer
        tipoTxBuffer = type(txBuffer)
        print("   Tipo do txBuffer: {}" .format(tipoTxBuffer))
        print("\n")

        # finalmente vamos transmitir os tados. Para isso usamos a funçao sendData que é um método da camada enlace.
        # faça um print para avisar que a transmissão vai começar.
        # tente entender como o método send funciona!
        # Cuidado! Apenas trasmitimos arrays de bytes! Nao listas!

        print("---------------------------------")
        print("3. A transmissão está começando.")
        print("---------------------------------")
        print("\n")

        com1.sendData(np.asarray(txBuffer))

        # É necessário colocar um timer aqui para ter tempo, se estiver trabalhando com um arduino (porta real). Nesse caso, é preciso colocar um timer: time.sleep(0.1)
        time.sleep(0.2)

        # A camada enlace possui uma camada inferior, TX possui um método para conhecermos o status da transmissão
        # Tente entender como esse método funciona e o que ele retorna

        txSize = com1.tx.getStatus()
        print("    Status da transmissão: {}".format(txSize))
        print("\n")

        # Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        # Observe o que faz a rotina dentro do thread RX
        # print um aviso de que a recepção vai começar.

        # print("---------------------------")
        #print("4. A recepção vai começar.")
        # print("---------------------------")
        # print("\n")

        # Será que todos os bytes enviados estão realmente guardados? Será que conseguimos verificar?
        # Veja o que faz a funcao do enlaceRX  getBufferLen

        # acesso aos bytes recebidos
        #txLen = len(txBuffer)
        #rxBuffer, nRx = com1.getData(txLen)

        # faça aqui uma conferência do tamanho do seu RxBuffer, ou seja, quantos bytes serão enviados.
        #tamRxBuffer = len(rxBuffer)
        #print("    Tamanho do rxBuffer: {}" .format(tamRxBuffer))
        # print("\n")

        #print("Bytes carregados em Rx: \n {}" .format(rxBuffer))
        # print("\n")

        # Escreve arquivo cópia
        # print("------------------------------")
        #print("5. Salvando dados no arquivo.")
        # print("------------------------------")

        # print("\n")
        #print("    Endereço da imagem recebida: {}" .format(imagemRecebida))
        # print("\n")
        #file = open(imagemRecebida, 'wb')
        # file.write(rxBuffer)

        # print("----------------------------")
        #print("6. Arquivo de imagem salvo.")
        # print("----------------------------")
        # print("\n")

        # Fecha arquivo de imagem
        # file.close()

        # Encerra comunicação
        print("--------------------------------------")
        print("7. Comunicação encerrada com sucesso!")
        print("--------------------------------------")
        com1.disable()

    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()


    # so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
