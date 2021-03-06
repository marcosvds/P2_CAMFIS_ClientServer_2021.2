#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Engenharia de Computação Insper
# Camada Física da Computação 2021.1
# Aluno: Marcos Vinícius da Silva
# 03/09/2021
# Projeto Client-Server
# Camada de Enlace Client
####################################################

# Importa pacote de tempo
import time

# Interface Física
from client_interfaceFisica import *

# enlace Tx e Rx
from client_enlaceTx import TX

class enlace(object):
    
    def __init__(self, name):
        self.fisica      = fisica(name)
        self.tx          = TX(self.fisica)
        self.connected   = False

    def enable(self):
        self.fisica.open()
        self.tx.threadStart()

    def disable(self):
        self.tx.threadKill()
        time.sleep(1)
        self.fisica.close()

    def sendData(self, data):
        self.tx.sendBuffer(data)
