import pandas as pd
import pyautogui
import pyperclip
import time

URL_FORMULARIO = "https://docs.google.com/forms/d/e/1FAIpQLSc27JUHD-OfQVKfHsfOE9BmJz-fdJ1fv3EGDIY33A4c08GZcA/viewform"

# Ler o arquivo CSV
df = pd.read_csv("notas.csv", dtype=str)

pyautogui.PAUSE = 0.5

print("Iniciando em 5 segundos... Mude para a janela do navegador em TELA CHEIA!")
time.sleep(5)

for index, row in df.iterrows():
    # 1. Abrir/recarregar o formulário
    pyautogui.hotkey('ctrl', 'l')
    pyperclip.copy(URL_FORMULARIO)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(3.5)  # Aguarda carregar a página completamente

    # 2. Pular o cabeçalho e os avisos do Google (3 TABs adicionais)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')  # Este 4º TAB faz cair exatamente na 1ª caixa de resposta (RA)

    # 3. Preencher os campos na sequência correta
    # Campo 1: RA
    pyperclip.copy(str(row['RA']))
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # Campo 2: Nome
    pyautogui.press('tab')
    pyperclip.copy(str(row['Nome']))
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # Campo 3: Nota 1
    pyautogui.press('tab')
    pyperclip.copy(str(row['Nota 1']))
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # Campo 4: Nota 2
    pyautogui.press('tab')
    pyperclip.copy(str(row['Nota 2']))
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # Campo 5: TF01
    pyautogui.press('tab')
    pyperclip.copy(str(row['TF01']))
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # Campo 6: TF02
    pyautogui.press('tab')
    pyperclip.copy(str(row['TF02']))
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # Botão Enviar (Submit)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2.5)

print("Preenchimento concluído com sucesso!")