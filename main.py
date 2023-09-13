import os
# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from view import create_main_window

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
            file_path = sg.popup_get_file("Como deseja salvar o arquivo", save_as=True)
            
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write(values["-CONTENT-"])
            
            file_name = os.path.basename(file_path)
            full_file_name = file_path
            refresh_window()   
            
        elif "::open" in event:
            file_path = sg.popup_get_file("Selecione um arquivo para abrir")
            
            with open(file_path, 'r', encoding="utf-8") as file:
                content = file.read()
            
            file_name = os.path.basename(file_path)
            full_file_name = file_path
            refresh_window()
            
            window['-CONTENT-'].update(content)
            update_status_bar(content)
        
        elif "::credits" in event:
            sg.popup_no_buttons("créditos: ByLearn \nAluno: Julio César")
        
        elif "::version" in event:
            sg.popup("Versão: 2.0.0")
        
        elif "::size" in event:
            font_size = create_font_popup("Tamanho da Fonte", "Insira o tamanho da fonte")
            refresh_window()
        
        elif "::family" in event:
            font_family = create_font_popup("Familia da Fonte", "Insira a Familia da fonte")
            # x = sg.popup_get_text() outra forma dr criatr uma popup
            refresh_window()
        
        elif "::theme" in event:
            current_theme = popup_combo(sg.theme_list(), current_theme, "Tema Padrão", "Selecione um Tema")
            refresh_window()
        
        elif event == '-CONTENT-':
           update_status_bar(values["-CONTENT-"]) 
            
        print(event, "==>", values)
        

    # Encerrar a janela
    window.close()