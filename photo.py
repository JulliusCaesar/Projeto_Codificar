import io
import PySimpleGUI as sg
from PIL import Image

def resize_image(imagepath, size=(450,750)):
    image = Image.open(imagepath)
    image = image.resize(size)
    
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes = image_bytes.getvalue()
    
    return image_bytes
try:
    with open("theme.txt") as file:
        theme = file.read()
except FileNotFoundError:
    with open("theme.txt", 'w') as file:
        file.write("DarkTeal6")

def create_photo_window(title=None, theme=theme):    
    # Definindo o nosso tema
    sg.theme(theme)
    image = "foto_carol.png"
    image = resize_image("foto_carol.png")

    layout = [
        [
            sg.Image(data=image, size=(450, 750)),
        ],
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Anjo?"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout,element_justification='center', finalize=True, )
    
    # Retorna a nossa janela
    return window
