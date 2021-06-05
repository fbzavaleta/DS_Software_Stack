##################################
#Field: Data Science             #
#Area : Lineal Algebra           #
#Autor: MBA Eng.Francis Benjamin #
#Data: 29/11/2020                #
##################################

import DS.errores as e
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
                return 1

    def sum(self, inputs:list):
        
        if vectores().set_vector_module(inputs) != 0:

            Su = np.zeros( len(inputs[0]) , dtype=int)
            for sumandos in inputs:
                Su += np.array( sumandos )
            return Su
        else:
            return e.E_LEN

    def substraction(self, inputs:list , operador:str):

        if vectores().set_vector_module(inputs) != 0:

            Subs = np.zeros( len(inputs[0]) , dtype=int)
            for subtraendo in inputs:
                Subs -= np.array( subtraendo )
            return Subs
        else:
            return e.E_LEN

    
    def prod_cruz(self, inputs:list):
        
        if vectores().set_vector_module(inputs) != 0:

            vector1 = np.array(inputs[0])
            vector2 = np.array(inputs[1])

            return np.dot( vector1 , vector2 )

        else:
            return e.E_LEN


    def quick_operation(self, inputs:list):

        vecA = np.array(inputs[0])
        vecB = np.array(inputs[1])

        operation = {

            'modA'     : np.linalg.norm(vecA),
            'modB'     : np.linalg.norm(vecB),
            'cosAngle' : np.dot(vecA,vecB) / ( np.linalg.norm(vecA) / np.linalg.norm(vecB) ),
            'angle'    : np.arccos( np.dot(vecA,vecB) / ( np.linalg.norm(vecA) * np.linalg.norm(vecB) ) )
        }

        return operation


class matrix():

    def __init__(self):

        self.self = self

    def operaciones(self, input_:list):

        dic_oper = {}

        dic_oper["exp"] = np.exp(input_)
        dic_oper["transf"] = np.array(input_).T 

    