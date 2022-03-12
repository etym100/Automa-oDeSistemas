# Como instalar
!pip install pyautogui
!pip install pyperclip

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

# Passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
pyautogui.click(x=878, y=676, clicks=2)
time.sleep(2)

# Passo 3: Fazer o download do relatório
pyautogui.click(x=1000, y=919)
pyautogui.click(x=3323, y=406)
pyautogui.click(x=2875, y=1401)
time.sleep(5)

# Passo 4: Calcular os indicadores
import pandas as pd

tabela = pd.read_excel(r"C://Users/joaol/Downloads/Vendas - Dez.xlsx")
display(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# Passo 5: Entrar no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# Passo 6: Enviar por e-mail o resultado
pyautogui.click(x=217, y=483)
time.sleep(7)

pyautogui.write("pythonimpressionador+diretoria@gmail.com")
pyautogui.press("tab") # seleciona o email
# escreve outro email
# tab
# escreve outro email
# tab
pyautogui.press("tab") # pula pro campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v") # escrever o assunto
pyautogui.press("tab") #pular pro corpo do email

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
LiraPython"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar

# apertar Ctrl Enter
pyautogui.hotkey("ctrl", "enter")

# Use esse código para descobrir qual a posição de um item que queira clicar
# Lembre-se: a posição na sua tela é diferente da posição na minha tela
#time.sleep(5)
#pyautogui.position()