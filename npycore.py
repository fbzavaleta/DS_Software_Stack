##############################
#Autor: Francis Benjamin     #
#Fecha: 29/11/2020           #
##############################
import numpy as np

'''
Clase Vectores     : Reune las funciones básicas de operación con 
                     vectores.

Funcion Operaciones: Aritmetica básica con vectores
             -Input : Inputs  : Lista con estrucctura de datos(list)
                      operador: identificiador de operacion: sum y sub (string)

             -Output: resultado de operación(number)
'''

class vectores():

    def __init__(self):

        self.self = self
     

    def operaciones(self, inputs:list , operador:str):

        qtd = len(inputs) -1
        flag = 0

        for pos in range(0,qtd ):

            if len(inputs[pos]) != len(inputs[pos+1]):
                print("No es posible operar vectores de diferente módulo")
                flag = 1
                break

        modulo = len(inputs[0])
        Su = np.zeros( modulo, dtype=int)

        if operador == "sum" and flag != 1:

            for sumandos in inputs:
                Su += np.array( sumandos )
            return Su

        elif operador == "sub" and flag != 1:

            for sumandos in inputs:
                Sub -= np.array( sumandos )
            return Sub