import unittest
from sorting import Sort

class TestBubble(unittest.TestCase):
   
    def test_bubble_1(self):
       bubble = Sort() 
       listaDesordenada = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
       listaOrdenada = bubble.BubbleSort(listaDesordenada)
       self.assertEqual(listaOrdenada, [0, 7, 9, 16, 21, 36, 40, 66, 71, 73])

    def test_bubble_2(self):
       bubble = Sort()
       listaDesordenada = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
       listaOrdenada = bubble.BubbleSort(listaDesordenada)
       self.assertEqual(listaOrdenada, [0, 1, 2, 2, 4, 6, 8, 9, 23, 25])
    
    def test_bubble_3(self):
       bubble = Sort()
       listaDesordenada = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
       listaOrdenada = bubble.BubbleSort(listaDesordenada)
       self.assertEqual(listaOrdenada, [0, 5, 6, 9, 15, 21, 25, 25, 35, 40])   

if __name__ == "__main__":
   unittest.main()        