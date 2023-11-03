import tkinter as tk
import pyautogui
import time

"""
Nome do Programa: [Automatização Sefaz-PI]
Autor: [Wesley Fuchs]
Data de Criação: [30/10/2023]

Este programa foi criado para automatizar as solicitações de exportação de documentos no Sefaz PI

Instruções de Uso: Ao clicar começar, você tera 10s para clicar em 'Agendar Exportação',
assim a tela ficara no local correto para que o codigo funcione sem problemas
- 

Histórico de Versões:
- [Versão 1.0 (31/10/2023): Automatiza as solicitações de exportação de documentos de entrada (NFC-e)]
- [Versão 2.0 (03/11/2023): Automatiza as solicitações de exportação de documentos de entrada (NF-e)]

"""

# Lista das datas que serão utilizadas
# date_sets = [("01/01/2023", "31/01/2023"), ("01;02;2023", "28;02;2023")]
# date_sets = [("01;01;2023", "31;01;2023")]
date_sets = [
    ("01/11/2023", "30/11/2023"),
    ("01/10/2023", "31/10/2023"),
    ("01/09/2023", "30/09/2023"),
    ("01/08/2023", "31/08/2023"),
    ("01/07/2023", "31/07/2023"),
    ("01/06/2023", "30/06/2023"),
    ("01/05/2023", "31/05/2023"),
    ("01/04/2023", "30/04/2023"),
    ("01/03/2023", "31/03/2023"),
    ("01/02/2023", "28/02/2023"),
    ("01/01/2023", "31/01/2023"),
    ("01/12/2022", "31/12/2022"),
    ("01/11/2022", "30/11/2022"),
    ("01/10/2022", "31/10/2022"),
    ("01/09/2022", "30/09/2022"),
    ("01/08/2022", "31/08/2022"),
    ("01/07/2022", "31/07/2022"),
    ("01/06/2022", "30/06/2022"),
    ("01/05/2022", "31/05/2022"),
    ("01/04/2022", "30/04/2022"),
    ("01/03/2022", "31/03/2022"),
    ("01/02/2022", "28/02/2022"),
    ("01/01/2022", "31/01/2022"),
    ("01/12/2021", "31/12/2021"),
    ("01/11/2021", "30/11/2021"),
    ("01/10/2021", "31/10/2021"),
    ("01/09/2021", "30/09/2021"),
    ("01/08/2021", "31/08/2021"),
    ("01/07/2021", "31/07/2021"),
    ("01/06/2021", "30/06/2021"),
    ("01/05/2021", "31/05/2021"),
    ("01/04/2021", "30/04/2021"),
    ("01/03/2021", "31/03/2021"),
    ("01/02/2021", "28/02/2021"),
    ("01/01/2021", "31/01/2021"),
    ("01/12/2020", "31/12/2020"),
    ("01/11/2020", "30/11/2020"),
    ("01/10/2020", "31/10/2020"),
    ("01/09/2020", "30/09/2020"),
    ("01/08/2020", "31/08/2020"),
    ("01/07/2020", "31/07/2020"),
    ("01/06/2020", "30/06/2020"),
    ("01/05/2020", "31/05/2020"),
    ("01/04/2020", "30/04/2020"),
    ("01/03/2020", "31/03/2020"),
    ("01/02/2020", "29/02/2020"),
    ("01/01/2020", "31/01/2020"),
    ("01/12/2019", "31/12/2019"),
    ("01/11/2019", "30/11/2019"),
    ("01/10/2019", "31/10/2019"),
    ("01/09/2019", "30/09/2019"),
    ("01/08/2019", "31/08/2019"),
    ("01/07/2019", "31/07/2019"),
    ("01/06/2019", "30/06/2019"),
    ("01/05/2019", "31/05/2019"),
    ("01/04/2019", "30/04/2019"),
    ("01/03/2019", "31/03/2019"),
    ("01/02/2019", "28/02/2019"),
    ("01/01/2019", "31/01/2019"),
    ("01/12/2018", "31/12/2018"),
    ("01/11/2018", "30/11/2018")
]
    

def automatizar_NFCe():  
    """Para cada set de datas em 'date_set' > Por meio de tabs ira chegar no campo de data 'Data Inicial' > digitar a data >
    tab para ir ao proximo campo 'Data Final' > digitar a data > tab para ir ao botão 'Agendar Exportação' > barra_de_espaço 
    para pressionar o botão > ira aguardar 5s para a proxima iteração do loop"""  

    # Tempo para o usuario clicar no lugar certo
    time.sleep(10)

    for data in date_sets:
        time.sleep(3)

        # 11 tabs para checkbox 'Data inicial'
        for _ in range(11):
            pyautogui.press('tab')
    
        # Escrever a 'Data Inicial'
        pyautogui.typewrite(data[0], interval=0.1)
        # time.sleep(1)
        
        # Selecionar o campo 'Data Final'
        pyautogui.press('tab')
        # time.sleep(1)

        # Escrever a 'Data Final'
        pyautogui.typewrite(data[1], interval=0.1)
        # time.sleep(1)

        # Selecionar o botão 'Agendar Exportacao'
        pyautogui.press('tab')
        time.sleep(1)

        # Pressionar o botão'
        pyautogui.press('space')
        time.sleep(2)

    status_label.config(text="Ação concluída!")


def automatizar_NFe():
    """Para cada set de datas em 'date_set' > Por meio de tabs e right_arrow 
    ira chegar na caixa 'Solicitar Emitente' > 
    tab e right_arrow para chegar na caixa 'Tipo de nota: Saida' > 
    tab para o campo 'Data Inicial' > tab para o campo 'Data Final' > 
    tab para ir ao botão 'Agendar Exportação' > barra_de_espaço 
    para pressionar o botão > ira aguardar para a proxima iteração do loop"""

    # Tempo para o usuario clicar no lugar certo
    time.sleep(10)

    for data in date_sets:
        time.sleep(3)

        # 6 tabs para 'Tipos de Consulta'
        for _ in range(6):
            pyautogui.press('tab')
    
        time.sleep(1)

        # Selecionar checkbox 'Contribuente como Emitente'
        pyautogui.press('right')

        time.sleep(2)

        # 3 tabs para 'Tipo de nota:'
        for _ in range(3):
            pyautogui.press('tab')

        # Selecionar checkbox 'Saida'
        for _ in range(2):
            pyautogui.press('right')

        # 3 tabs para o campo de 'Data Inicial'
        for _ in range(3):
            pyautogui.press('tab')

        # Escrever a 'Data Inicial'
        pyautogui.typewrite(data[0], interval=0.1)
        
        # Selecionar o campo 'Data Final'
        pyautogui.press('tab')

        # Escrever a 'Data Final'
        pyautogui.typewrite(data[1], interval=0.1)
        # time.sleep(1)

        # Selecionar o botão 'Agendar Exportacao'
        pyautogui.press('tab')
        time.sleep(1)

        # Pressionar o botão
        pyautogui.press('space')
        time.sleep(2)

    status_label.config(text="Ação concluída!")

# Configurações da janela do tkinter
window = tk.Tk()
window.title("Automatização Sefaz-PI")
window.geometry("300x150")

nfce_button = tk.Button(window, text="Start NFC-e", command=automatizar_NFCe)
nfe_button = tk.Button(window, text="Start NF-e", command=automatizar_NFe)
status_label = tk.Label(window, text="")

nfce_button.pack(fill="both", pady=15, padx=40)
nfce_button.configure(border=2)
nfe_button.pack(fill="both", pady=15, padx=40)
nfe_button.configure(border=2)
status_label.pack()

window.mainloop()
