"""
Created on Sat Sep 19 11:32:07 2020

@author: Camilo
"""
import unittest
import clasicoalocuantico
from numpy import matrix
class unit_calculadora(unittest.TestCase):

    def test_canicas(self):
        self.assertEqual(clasicoalocuantico.canicas(matrix([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]),matrix([[1],[0],[1],[0],[0],[1]]),2),[['False'], ['False'], ['False'], ['False'], ['False'], ['True']])

    def test_clasicoproba(self):
        self.assertEqual(clasicoalocuantico.clasicoproba(matrix([[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]]),matrix([[1/6],[1/6],[2/3]]),1),[[0.5833333333333334],[0.25],[0.16666666666666666]])
 
    def test_grafico(self):
        self.assertEqual(clasicoalocuantico.grafico([[1, 0], [1/2, 0], [1/2, 0], [1/6, 0], [1/6, 0], [1/3, 0], [1/6, 0], [1/6, 0]]), None)

    
unittest.main()