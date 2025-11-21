# 1º Passo: Instalar o Pyatogui com o comando: 
# pip install pyautogui

# Crie uma atomação que abra automaticamente um navegador

# Importamos a biblioteca para o script em uso
import pyautogui

# 'Press' é um comando que utilizamos 
# para pressionar a tecla desejada
pyautogui.press('Win') # para pressionar a tecla windows

# 'sleep' é um comando que utilizamos para deixar o código
#  em espera por alguns segundos
pyautogui.sleep(1)

# 'Write' é um comando que utilizamos para passae o que queremos
# escrever
pyautogui.write('Google Chrome')

pyautogui.press('Enter')