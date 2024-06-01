import pyautogui as py
import time 
from time import sleep
py.PAUSE = 2.5

py.click(x=1036, y=1060) #vai na planilha
py.click(x=100, y=242) #clica na primeira nota da planilha
py.hotkey('ctrl', 'c') # copia a nota
py.click(x=892, y=1052) #abrir o protheus na barra de tarefa
py.click(x=369, y=32) #aba da pré nota
py.click(x=1643, y=149) #campo de pesquisa de nota 
py.hotkey('ctrl', 'v') # cola a nota
py.click(x=1831, y=151) #vai pesquisar a nota
py.click(x=416, y=161) #outras ações
py.click(x=389, y=241) #estornar classificação
time.sleep(3.5)
py.click(x=1862, y=150) #estorna a nota
py.press("down") #vai para a nota de baixo 
for c in range(43):
    py.click(x=416, y=161) #outras ações
    py.click(x=389, y=241) #estornar classificação
    time.sleep(3.5)
    py.click(x=1862, y=150) #estorna a nota
    time.sleep(3.5)
    py.press("down") #vai para a nota de baixo 
py.click(x=1036, y=1060) #vai na planilha
py.click(x=100, y=242) #clica na primeira nota da planilha
py.hotkey('ctrl', 'c') # copia a nota
py.click(x=892, y=1052) #abrir o protheus na barra de tarefa
py.click (x=588, y=40) #clica na aba documentos de entrada
py.click(x=1643, y=149) #campo de pesquisa de nota 
py.hotkey('ctrl', 'v') # cola a nota
py.click(x=1831, y=151) #vai pesquisar a nota
py.click(x=1036, y=1060) #vai na planilha
py.click(x=226, y=244) #clica na TES
py.hotkey('ctrl', 'c') # copia a TES
py.click(x=892, y=1052) #abrir o protheus na barra de tarefa
py.click(x=154, y=156) #vai classificar a nota
time.sleep(4)
py.click(x=1161, y=313) #clica no campo da TES
py.press("enter") 
py.hotkey('ctrl', 'v') # cola a TES
py.click(x=1036, y=1060) #vai na planilha
py.press("right") #vai na celula da referencia 
py.hotkey('ctrl', 'c') # copia a referencia
py.press("down")
py.press("left")
py.click(x=892, y=1052) #abrir o protheus na barra de tarefa  ##
py.click(x=268, y=831) #vai no campo obs
py.click(x=475, y=310) #clica na area da obs
py.press("enter")
py.hotkey('ctrl', 'v') # cola a referencia
py.press("enter")
py.click(x=1864, y=153) #salva o lançamento
time.sleep(3.5)
py.press("down")
for c in range (43):
    py.click(x=1036, y=1060) #vai na planilha
    py.hotkey('ctrl', 'c') # copia a TES
    py.click(x=892, y=1052) #abrir o protheus na barra de tarefa
    py.click(x=154, y=156) #vai classificar a nota
    time.sleep(4)
    py.click(x=1161, y=313) #clica no campo da TES
    py.press("enter") 
    py.hotkey('ctrl', 'v') # cola a TES ##
    py.click(x=268, y=831) #vai no campo obs
    py.click(x=1036, y=1060) #vai na planilha
    py.press("right") #vai na celula da referencia 
    py.hotkey('ctrl', 'c') # copia a referencia
    py.press("down")
    py.press("left")
    py.click(x=892, y=1052) #abrir o protheus na barra de tarefa
    py.click(x=475, y=310) #clica na area da obs
    py.press("enter")
    py.hotkey('ctrl', 'v') # cola a referencia
    py.press("enter")
    py.click(x=1864, y=153) #salva o lançamento
    time.sleep(3.5)
    py.press("down")





