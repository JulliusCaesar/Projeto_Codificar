# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg


def popup_combo(values, default_value=None, title=None, content=None):   
    
    
    if default_value is not None:
        if default_value in values:
            default_index = values.index(default_value)
            default_value = values[default_index]
        else:
            default_value = default_value

    # Definindo nosso layout
    layout = [
        [
            sg.Text(content),
        ],
        [
            sg.Combo(values, default_value, key="-VALUE-")
        ],
        [
            sg.Button("OK"), sg.Button("Cancel"),
        ],
    ]
    
    # Definindo o titulo da janela
    title = title

    # Criar a popup e lê os eventos/valores dela
    popup_event, popup_value = sg.Window(title, layout, finalize=True).read(close=True)
    
    # Retorna a nossa janela
    if popup_event == "OK":
        return popup_value["-VALUE-"]
    else:
        return popup_value["-VALUE-"]