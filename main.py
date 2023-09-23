import os
# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg
from view import create_main_window
from popups import popup_combo
from codificar_decodificar import codificar_codigo, decodificar_codigo
from photo import create_photo_window


current_theme = "DarkTeal6"
font_family = "Arial"
font_size = 10
file_name = "Novo Arquivo"
full_file_name = file_name
chars = 0
lines = 1

def update_status_bar(content):
    chars = len(content.strip().replace('\n', ''))
    lines = len(content.strip().split('\n'))
    
    status_bar_text = (f"Arquivo Atual: {full_file_name} | O arquivo tem um total de {chars} caracteres e {lines} linhas |")

    window['-STATUSBAR-'].update(status_bar_text)

def refresh_window():
    global window
    
    content = values["-CONTENT-"]
    size = window.size
    location = window.current_location()
    window.close()
    
    window = create_main_window(title=f"Codificador de texto para a Carol - {file_name}", theme=current_theme, size=size,
                                location=location, font=(font_family, font_size))
    
    window["-CONTENT-"].update(content)
    update_status_bar(content)

if __name__ == "__main__":

    # Definindo a janela inicial
    window = create_main_window()

    # Loop da leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()
        
        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break
        
        elif "::new" in event:
            confirm = sg.popup("Você tem certeza?", custom_text=("Sim", "Não"), title="Atenção!")
            if confirm == "Sim":
                window["-CONTENT-"].update("")
                update_status_bar("")
        
        # if event.endswith("::open") pode ser usado quando houver palavras parecidas
        elif "::save" in event:
            try:
                file_path = sg.popup_get_file("Como deseja salvar o arquivo", save_as=True)
                with open(file_path, 'w', encoding="utf-8") as file:
                    file.write(values["-CONTENT-"])
                file_name = os.path.basename(file_path)
                full_file_name = file_path
                refresh_window()
            except TypeError:
                refresh_window()
            except FileNotFoundError:
                refresh_window()  
            
        elif "::open" in event:
            try:
                file_path = sg.popup_get_file("Selecione um arquivo para abrir")
                with open(file_path, 'r', encoding="utf-8") as file:
                    content = file.read()
                file_name = os.path.basename(file_path)
                full_file_name = file_path
                refresh_window()
                window['-CONTENT-'].update(content)
                update_status_bar(content)
            except TypeError:
                refresh_window()
            except FileNotFoundError:
                refresh_window() 
        
        elif "::credits" in event:
            sg.popup_no_buttons("créditos: Julio César\nAno: 2023")
        
        elif "::version" in event:
            sg.popup("Versão: 1.0.0")
        
        elif "::size" in event:
            font_size = sg.popup_get_text("Tamanho da Fonte", "Insira o tamanho da fonte")
            if font_size == None:
                font_size = 10
            if font_size == "":
                font_size = 10
            refresh_window()
        
        elif "::family" in event:
            font_family = sg.popup_get_text("Familia da Fonte", "Insira a Familia da fonte")
            if font_family == None:
                font_family = "Arial"
            if font_family == "":
                font_family = "Arial"
            refresh_window()
        
        elif "::code" in event:
            texto = values["-CONTENT-"]
            texto = codificar_codigo(texto)
            window["-CONTENT-"].update(texto)
        
        elif "::decode" in event:
            texto = values["-CONTENT-"]
            texto = decodificar_codigo(texto)
            window["-CONTENT-"].update(texto)
        
        elif "::theme" in event:
            current_theme = popup_combo(sg.theme_list(), current_theme, "Tema Padrão", "Selecione um Tema")
            refresh_window()
        
        elif "::carol" in event:
           create_photo_window()
            
        
        elif event == '-CONTENT-':
           update_status_bar(values["-CONTENT-"]) 
            
        print(event, "==>", values)
        

    # Encerrar a janela
    window.close()