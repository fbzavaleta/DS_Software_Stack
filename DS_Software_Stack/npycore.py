##################################
#Field: Data Science             #
#Area : Lineal Algebra           #
#Autor: MBA Eng.Francis Benjamin #
#Data: 29/11/2020                #
##################################

import DS_Software_Stack.errores as e
import numpy as np
'''
Clase Vectores     : Reune las funciones básicas de operación con 
                     vectores.

Fun Operaciones: Aritmetica básica con vectores
             -Input : Inputs  : Lista con estrucctura de datos(list)
                      operador: identificiador de operacion: sum y sub (string)

             -Output: resultado de operación(number)
'''

class vectores():

    def __init__(self):

        self.self = self


    def set_vector_module(self, inputs_:list):
        qtd = len(inputs_) -1

        for pos in range(0,qtd ):

            if len(inputs_[pos]) != len(inputs_[pos+1]):
                return 0
            else:
                return np.zeros( len(inputs_[0]) , dtype=int)

    def sum(self, inputs:list , operador:str):

        su = vectores().set_vector_module(inputs)

        if su != 0:
            for sumandos in inputs:
                Su += np.array( sumandos )
            return Su
        else:
            return e.E_LEN

    def substraction(self, inputs:list , operador:str):

        Subs = vectores().set_vector_module(inputs)

        if Subs != 0:

            for subtraendo in inputs:
                Subs -= np.array( subtraendo )
            return Subs
        else:
            return e.E_LEN

    
    def producto_punto(self, inputs:list):
        return zip(inputs)




